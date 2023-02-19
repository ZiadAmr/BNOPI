#include "graph.hpp"

Graph::Graph(std::map<int, Stop> &stops, std::list<Link> &links) : stops(stops), links(links){};

Graph::~Graph()
{
}

int Graph::getSize()
{
    return stops.size();
}