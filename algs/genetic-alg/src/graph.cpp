#include "graph.hpp"
#include <algorithm>

Graph::Graph(std::map<int, Stop> stops, std::list<Link> links) : stops(stops), links(links)
{
}

Graph::~Graph()
{
}

int Graph::getSize()
{
    return stops.size();
}

void Graph::set_cids() {
    // sort stops by id.
    // first copy pointers to array
    for (auto &pair : stops)
    {
        Stop *s = &(pair.second);
        stops_by_id.push_back(s);
    }

    // sort by id
    std::sort(stops_by_id.begin(), stops_by_id.end(), [](Stop *a, Stop *b)
              { return a->id < b->id; });

    // add cids to stops
    for (int cid = 0; cid < stops_by_id.size(); cid++)
    {
        stops_by_id[cid]->cid = cid;
    }

}