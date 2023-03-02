#include "smo.hpp"
#include "link.hpp"
#include "stop.hpp"
#include "objective.hpp"
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

SMODriver::SMODriver(Population initial_population, AlgSettings& settings, int niter): settings(settings), niter(niter) {
	// convert Population to DPopulation (add `inverted` bit to represent which end of the route we are adding to)
	for (RouteNet route_net: initial_population) {
		DRouteNet d_route_net;
		for (Route route: route_net) {
			d_route_net.push_back({false, route});
		}
		population.push_back(d_route_net);
	}

	// calculate the initial fitness of each network
	for (DRouteNet drn : population) {
		// TOOD call fitness function (net yet implemented)
		float fitness = 0;

		parent_fitness.push_back(fitness);
	}
}

void SMODriver::step() {

	// copy of the parents to mutate
	DPopulation offspring = population;

	// make a small change to each of the networks in the population.
	for (DRouteNet& drn : offspring) {
		make_small_change(drn);
	}

	for (int i = 0; i < population.size(); i++) {

		DRouteNet &parent = population[i];
		DRouteNet &child = offspring[i];

		if (is_duplicate(child, population))
			continue;

		// evaluate fitness of the child
		RouteNet child_rn = DRouteNet_to_RouteNet(child);
		float fitness = objective_function(child_rn);

		// if offspring improves on best-so-far
		if (fitness > best_so_far_fitness) {
			best_so_far_fitness = fitness;
			best_so_far_routenet = child_rn;
		}

		// if better than parent
		// replace parent
		if (fitness > parent_fitness[i]) {
			population[i] = child;
			parent_fitness[i] = fitness;
		}

		// paper also has a course of action if the fitness is the same.
		// find an individual in the population that is dominated by the offspring and replace it with the offspring.
		else if (fitness == parent_fitness[i]) {
			for (int j = 0; j < population.size(); j++) {
				if (parent_fitness[j] < fitness) {
					population[j] = child;
					parent_fitness[j] = fitness;
					break;
				}
			}
		}

	}

	if (verbose) {
		cout << "Step " << it << " complete. Best fitness so far: " << best_so_far_fitness << endl;
	}

	it++;


}

RouteNet SMODriver::get_best_routenet() {
	return best_so_far_routenet;
}

bool SMODriver::stopping_condition_met() {
	return it >= niter;
}


Population SMODriver::get_population() {
	return DPopulation_to_Population(population);
}

bool SMODriver::is_duplicate(DRouteNet& drn, DPopulation& dp) {
	// TODO
	return false;
}


bool SMODriver::is_feasible(DRouteNet& rn) {
	// Because of the inclusion of walking edges it is feasible to walk from any node to any other
	// so all networks are feasible
	return true;
}

float SMODriver::objective_function(RouteNet& rn) {
	// TODO
	return rand()/((float)INT32_MAX);
}


RouteNet SMODriver::DRouteNet_to_RouteNet(DRouteNet &drn) {
	RouteNet rn;
	for (DRoute dr: drn)
		rn.push_back(dr.r);
	return rn;
}

Population SMODriver::DPopulation_to_Population(DPopulation &dp) {
	Population p;
	for (DRouteNet drn: dp){
		RouteNet rn = DRouteNet_to_RouteNet(drn);
		p.push_back(rn);
	}
	return p;
}



void SMODriver::make_small_change(DRouteNet &route_net) {

	// keep making changes until we get a feasible network
	do {
		// choose one of the routes
		int n = (int) rand() % route_net.size();
		make_small_change(route_net[n]);

	} while (!is_feasible(route_net));
}

void SMODriver::make_small_change(DRoute &route) {

	// check which options are valid
	bool allowed_to_add_link = route.r.size() < settings.max_route_stops;
	bool allowed_to_remove_link = route.r.size() > settings.min_route_stops;

	if (!allowed_to_add_link)
		remove_link(route);
	
	else if (!allowed_to_remove_link) {
		if (!add_link(route))
			invert_order(route);
	}

	else {
		if (rand() % 2 == 1) {
			remove_link(route);
		} else {
			if (!add_link(route))
				invert_order(route);
		}
	}

}

bool SMODriver::add_link(DRoute &route)
{
	// get list of edges to select from
	vector<Link *> next_edges;
	if (route.inverted)
		next_edges = route.r.front()->start->in_edges;
	else
		next_edges = route.r.back()->end->out_edges;

	// select an edge at random
	// we don't need to check if the new route is a duplicate since we're assuming the current route is not a duplicate.
	if (next_edges.size() == 0) return false;
	int choice = (int)rand() % next_edges.size();
	Link* new_link = next_edges[choice];

	// add to route
	if (route.inverted)
		route.r.insert(route.r.begin(), new_link);
	else
		route.r.push_back(new_link);
	
	return true;
}



Link* SMODriver::remove_link(DRoute &route) {
	if (route.inverted) {
		Link* removed = route.r.back();
		route.r.pop_back();
		return removed;
	} else {
		Link* removed = route.r[0];
		route.r.erase(route.r.begin());
		return removed;
	}
}

void SMODriver::invert_order(DRoute &route) {
	route.inverted = !route.inverted;
}