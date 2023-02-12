#pragma once
#include <vector>
#include "link.hpp"

typedef std::vector<std::vector<Link>> RouteNet;

struct AlgSettings
{
	int max_route_stops;
	int num_routes;
};