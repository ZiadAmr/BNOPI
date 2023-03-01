#pragma once
#include <vector>
#include "common.hpp"
#include "link.hpp"
#include "graph.hpp"
#include <algorithm>
#include <random>

class Link;

/**
 * @brief
 *
 * @param minRouteSize
 * @param maxRouteSize
 * @param numberOfRoutes
 * @param population
 * @return RouteNet
 */
RouteNet generateRouteSet(AlgSettings setting, Graph &stop_connection);
Population generatePopulation(AlgSettings setting, Graph &stop_connection);

/**
 * @brief Recursive function that generates a route starting from a stop
 * 
 * @param size How much more we need to traverse to complete the route
 * @param stop_connection The stop connection graph
 * @param stop The stop currently in consideration
 * @param history The links that have already been added
 * @param candidate_route_set The list of routes that we have already generated
 * @return Returns a route if a feasible one is found, otherwise returns null pointer
 */
Route* generateRoute(int size, Graph &stop_connection, Stop* stop, Route &history, RouteNet &candidate_route_set);

/**
 * @brief Function to check if a route is a duplicate route that is already in the candidate route set
 * 
 * @param candidate_route_set The candidate route set so far
 * @param candidate_route The route being checked
 * @return true 
 * @return false 
 */
bool checkDuplicateRoute(RouteNet candidate_route_set, Route &candidate_route);