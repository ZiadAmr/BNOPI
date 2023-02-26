#include "candidate-route-generation.hpp"
using namespace std;

// remember to do exception handling from the genetic-algorithm.cpp

RouteNet generateRouteSet(AlgSettings setting, Graph stop_connection)
{
    // Prints out the total number of bus stops we have loded
    if (verbose)
    {
        cout << "There are " << stop_connection.getSize() << " many stops in my graph" << endl;
    }

    // A vector that stores the stops so that we can sample from it.
    // When a stop is exhausted it is removed from the vector
    vector<int> non_exhausted_stops;

    for (auto stops : stop_connection.stops)
    {
        non_exhausted_stops.push_back(stops.first);
    }

    std::mt19937 rng(std::random_device{}());

    // Flag to indicate whether we have found the required number of routes
    bool finished = false;
    // Counter to keep track of how many routes have been generated
    int count = 0;
    RouteNet candidate_route_set;

    // Find the routes starting from the bus stops
    while(!finished && !non_exhausted_stops.empty()){

        std::uniform_int_distribution<int> dist(0, non_exhausted_stops.size());
        int random_index = dist(rng);
        Stop random_stop = stop_connection.stops.find(non_exhausted_stops[random_index])->second;
        // Attempt to generate a route starting from random_stop
        Route* potential_route = generateRoute(setting.min_route_stops, stop_connection, &random_stop, Route(), candidate_route_set);
 
        // Check if we have successfully generated a route starting from the random stop
        if(potential_route != nullptr){
            candidate_route_set.push_back(*potential_route);
        }else{
            // If the stop cannot generate a route, remove it from possible route starting points
            non_exhausted_stops.erase(non_exhausted_stops.begin() + random_index);
        }

        // Stopping criterion - When we have generated the desired number of routes
        if (count == setting.num_routes){
            finished = true;
        }
    }


    return candidate_route_set;
}

Route* generateRoute(int size, Graph stop_connection, Stop* stop, Route history, RouteNet candidate_route_set){
    
    // Base case: When we have found a route that is of the given size
    if(size == 0){

        // Check if the route is in the list of routes we have already generated
        if (checkDuplicateRoute(candidate_route_set, history)){
            return nullptr;
        }

        // If route is unique then we will return the found route (Done at the previous function call.
        // Here a simple empty route is returned just as a indicator)
        return new Route();
    }

    // Exhaustively try out all possible out edges and see if there is a route that is feasible
    for(Link* l : stop->out_edges){

        // We assume that a route will never have duplicate links
        if(find(history.begin(), history.end(), l) != history.end()) {
            continue;
        }

        history.push_back(l);
        auto new_history = generateRoute(size--, stop_connection, l->end, history, candidate_route_set);

        if(new_history != nullptr){
            return new_history;
        }else{
            history.pop_back();
        }

    }
    
    return nullptr;
}

bool checkDuplicateRoute(RouteNet candidate_route_set, Route candidate_route){
    bool dupl = false;
    for(auto i : candidate_route_set){
        dupl = true;
        for(int j = 0 ; j < candidate_route.size(); j++){
            if(i[j] != candidate_route[j]){
                dupl = false;
                break;
            }
        }

        if(dupl){
            return dupl;
        }
    }
    return dupl;
}

Population generatePopulation(AlgSettings setting, Graph stop_connection)
{

    // Make sure to do some pre-processing steps to identify if the algorithm will fail

    Population population;
    for (int i = 0; i < setting.population_size; i++)
    {

        auto candidate = generateRouteSet(setting, stop_connection);

        if (candidate.empty())
        {
            throw "Invalid parameter for graph";
        }

        population.push_back(candidate);
    }

    return population;
}
