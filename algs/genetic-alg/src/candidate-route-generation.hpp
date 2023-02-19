#pragma once
#include <vector>
#include "common.hpp"
#include "link.hpp"

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
RouteNet generateRouteSet(int minRouteSize, int maxRouteSize, int numberOfRoutes, Population population);
Population generatePopulation(int minRouteSize, int maxRouteSize, int numberOfRoutes, int populationSize);