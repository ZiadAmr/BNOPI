#pragma once
#include <vector>
#include "common.hpp"

class Link;
typedef std::vector<RouteNet *> Population;

RouteNet generateRouteSet(int minRouteSize, int maxRouteSize, int numberOfRoutes, Population population);
Population generatePopulation(int minRouteSize, int maxRouteSize, int numberOfRoutes, int populationSize);