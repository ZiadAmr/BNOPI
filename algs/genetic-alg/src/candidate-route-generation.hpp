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
RouteNet generateRouteSet(AlgSettings setting, Graph stop_connection);
Population generatePopulation(AlgSettings setting, Graph stop_connection);