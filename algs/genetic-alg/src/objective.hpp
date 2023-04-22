#pragma once
#include "link.hpp"
#include "stop.hpp"
#include "common.hpp"
#include "od-matrix.hpp"
#include <vector>
#include <utility>

std::pair<double, double> opt(std::vector<Stop> stops, RouteNet route, std::vector<std::vector<double>> od);
float djikstra(RouteNet routes, std::vector<Stop> stops, int source, int destination);
