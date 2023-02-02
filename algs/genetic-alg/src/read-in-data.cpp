
#include "read-in-data.hpp"
#include <string>
#include <json/json.h>

using namespace std;

int read_in_stops(ifstream &stops_file, map<int, Stop> &stops) {
	Json::Value root;
	stops_file >> root;

	const Json::Value stops_js = root["stops"];
	if (stops_js.isNull()) return 1;

	for (const Json::Value stop_js : stops_js) {
		string name = stop_js.get("name", "").asString();
		int id = stop_js.get("id", 0).asInt();
		double lat = stop_js.get("lat", 0.0).asDouble();
		double lon = stop_js.get("lon", 0.0).asDouble();

		Stop stop(name, id, lat, lon);

		stops[id] = stop;
	}
	return 0;

}

int read_in_links(ifstream &links_file, list<Link> &links, map<int, Stop> &stops) {

	Json::Value root;
	links_file >> root;

	const Json::Value links_js = root["links"];
	if (links_js.isNull())
		return 1;

	for (const Json::Value link_js : links_js)
	{
		string name = link_js.get("name", "").asString();
		int id = link_js.get("id", 0).asInt();
		float length = link_js.get("length", 0.0).asFloat();

		int startid = link_js.get("startid", 0).asInt();
		int endid = link_js.get("endid", 0).asInt();

		// find the corresponding stops in the hashmap
		Stop *start = &stops[startid];
		Stop *end = &stops[startid];

		Link link(id, name, length, start, end);

		links.push_back(link);

	}

	return 0;
}

int create_graph(string stops_file_loc, string links_file_loc, Graph *graph)
{

	// create file streams
	ifstream stops_fs;
	stops_fs.open(stops_file_loc, fstream::in);
	if (stops_fs.fail()) return errno;

	ifstream links_fs;
	links_fs.open(links_file_loc, fstream::in);
	if (links_fs.fail()) return errno;

	// call above functions
	int err;
	map<int, Stop> stops;
	if (!(err = read_in_stops(stops_fs, stops))) return err;
	stops_fs.close();

	list<Link> links;
	if (!(err = read_in_links(links_fs, links, stops))) return err;
	links_fs.close();

	graph = new Graph(stops, links);
	return 0;

}
