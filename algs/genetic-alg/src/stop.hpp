#pragma once
#include <string>
#include <vector>

class Link;

class Stop
{

public:
	std::string name;
	int id;
	/* cid is "contiguous id". Index of this stop id in a sorted list of all ids.
	 * Added later in constructor for Graph.
	*/
	int cid;
	double lat, lon;
	std::vector<Link *> out_edges;
	std::vector<Link *> in_edges;

	Stop(std::string name, int id, double lat, double lon) : name(name), id(id), lat(lat), lon(lon){};
	Stop(){};
};