#pragma once
#include <vector>
#include "link.hpp"
#include <iostream>

extern bool verbose;

typedef std::vector<Link *> Route;
typedef std::vector<Route> RouteNet;
typedef std::vector<RouteNet> Population;

struct AlgSettings
{
	int max_route_stops;
	int min_route_stops;
	int num_routes;
	int population_size;
};