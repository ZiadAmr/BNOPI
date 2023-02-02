#pragma once
#include "stop.hpp"
#include "link.hpp"
#include <list>
#include <map>

class Graph {

public:
std::map<int, Stop> stops;
std::list<Link> links;

Graph(std::map<int, Stop> &stops, std::list<Link> &links);

~Graph();


};