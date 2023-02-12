#include "smo.hpp"
#include "link.hpp"
#include "stop.hpp"
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

SMODriver::SMODriver(Population initial_population, AlgSettings& settings): settings(settings) {
	// convert Population to DPopulation (add `inverted` bit to represent which end of the route we are adding to)
	for (RouteNet route_net: initial_population) {
		DRouteNet d_route_net;
		for (Route route: route_net) {
			d_route_net.push_back({false, route});
		}
		population.push_back(d_route_net);
	}
}

void SMODriver::step() {
	// TODO
}

Population SMODriver::get_population() {
	return DPopulation_to_Population(population);
}










RouteNet& SMODriver::DRouteNet_to_RouteNet(DRouteNet &drn) {
	RouteNet rn;
	for (DRoute dr: drn)
		rn.push_back(dr.r);
	return rn;
}

Population& SMODriver::DPopulation_to_Population(DPopulation &dp) {
	Population p;
	for (DRouteNet drn: dp){
		RouteNet rn = DRouteNet_to_RouteNet(drn);
		p.push_back(rn);
	}
	return p;
}



void SMODriver::make_small_change(DRouteNet &route_net) {

	// choose one of the routes
	int n = (int) rand() * route_net.size();
	make_small_change(route_net[n]);
}

void SMODriver::make_small_change(DRoute &route) {

	// check which options are valid
	bool allowed_to_add_link = route.r.size() < settings.max_route_stops;
	bool allowed_to_remove_link = route.r.size() > settings.min_route_stops;

	if (!allowed_to_add_link)
		remove_link(route);
	
	else if (!allowed_to_remove_link)
		if (!add_link(route))
			invert_order(route);

	else {
		if (rand() > 0.5) {
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
	int choice = (int)rand() * next_edges.size();
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