#pragma once
#include <vector>
#include "link.hpp"

extern bool verbose;

typedef std::vector<Link*> Route;
typedef std::vector<Route> RouteNet;

struct AlgSettings
{
	int max_route_stops;
	int min_route_stops;
	int num_routes;
};