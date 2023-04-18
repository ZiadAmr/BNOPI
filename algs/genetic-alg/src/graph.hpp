#pragma once
#include "stop.hpp"
#include "link.hpp"
#include <list>
#include <map>

class Graph {

public:
std::map<int, Stop> stops;
std::list<Link> links;

Graph(std::map<int, Stop> stops, std::list<Link> links);

~Graph();

/**
 * @brief Get the total number of stops in the stop connection graph
 * 
 * @return int 
 */
int getSize();


};