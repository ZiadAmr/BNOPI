#pragma once
#include "stop.hpp"
#include "link.hpp"
#include <list>
#include <map>

class Graph {

public:
std::map<int, Stop> stops;
std::vector<Stop*> stops_by_id;
std::list<Link> links;

Graph(std::map<int, Stop> stops, std::list<Link> links);

~Graph();

/**
 * @brief Get the total number of stops in the stop connection graph
 * 
 * @return int 
 */
int getSize();

/**
 * @brief Sort stops, creating `stops_by_id`, and add cid to each stop.
 *
 */
void set_cids();


};