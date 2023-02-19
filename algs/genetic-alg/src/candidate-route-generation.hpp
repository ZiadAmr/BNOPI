#pragma once
#include <vector>
#include "common.hpp"
#include "link.hpp"
#include "graph.hpp"

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
RouteNet generateRouteSet(int minRouteSize, int maxRouteSize, int numberOfRoutes);
Population generatePopulation(int minRouteSize, int maxRouteSize, int numberOfRoutes, int populationSize);