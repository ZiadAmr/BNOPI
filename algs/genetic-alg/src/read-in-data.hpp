#pragma once

#include <list>
#include <map>
#include <fstream>
#include "stop.hpp"
#include "link.hpp"
#include "graph.hpp"
#include "od-matrix.hpp"
#include "common.hpp"

// Read in the stops and store them in a hashmap.
int read_in_stops(std::ifstream &stops_file, std::map<int, Stop> &stops);

// Read in the links and store them in a hashmap.
// Requires the stops to be previously read in, as links store the stops at either end.
int read_in_links(std::ifstream &links_file, std::list<Link> &links, std::map<int, Stop> &stops);

// Create graph data structure from json files.
int create_graph(std::ifstream &stops_fs, std::ifstream &links_fs, Graph **graph);

OD::Matrix read_in_od_matrix(std::ifstream &od_matrix_fs, Graph& graph);

// serialize a route network for file output
std::string routenet_to_string(RouteNet& rn);