
#include "read-in-data.hpp"
#include <string>
// #include <json/json.h>
#include <nlohmann/json.hpp>

using namespace std;
using namespace nlohmann;

// int read_in_stops(ifstream &stops_file, map<int, Stop> &stops) {
// 	Json::Value root;
// 	stops_file >> root;

// 	const Json::Value stops_js = root["stops"];
// 	if (stops_js.isNull()) return 1;

// 	for (const Json::Value stop_js : stops_js) {
// 		string name = stop_js.get("name", "").asString();
// 		int id = stop_js.get("id", 0).asInt();
// 		double lat = stop_js.get("lat", 0.0).asDouble();
// 		double lon = stop_js.get("lon", 0.0).asDouble();

// 		Stop stop(name, id, lat, lon);
// 		stops.insert({id, stop});
// 	}
// 	return 0;

// }

int read_in_stops(ifstream &stops_file, map<int, Stop> &stops)
{
	json data = json::parse(stops_file);
	// auto x = data["stops"];

	for (const auto stop_js : data["stops"]) {
		string name = stop_js["name"].get<string>();
		int id = stop_js["id"].get<int>();
		double lat = stop_js["lat"].get<double>();
		double lon = stop_js["lon"].get<double>();

		Stop stop(name, id, lat, lon);
		stops.insert({id, stop});
	}
	return 0;
}

int read_in_links(ifstream &links_file, list<Link> &links, map<int, Stop> &stops) {

	// Json::Value root;
	// links_file >> root;

	json data = json::parse(links_file);

	// const Json::Value links_js = root["links"];
	// if (links_js.isNull())
	// 	return 1;
	json links_js = data["links"];

	for (const auto link_js : links_js)
	{
		// string name = link_js.get("name", "").asString();
		// int id = link_js.get("id", 0).asInt();
		// float length = link_js.get("length", 0.0).asFloat();

		// int startid = link_js.get("startid", 0).asInt();
		// int endid = link_js.get("endid", 0).asInt();

		string name = link_js["name"];
		int id = link_js["id"];
		float length = link_js["length"];

		int startid = link_js["startid"];
		int endid = link_js["endid"];
		// find the corresponding stops in the hashmap
		Stop *start = &(stops.find(startid)->second);
		Stop *end = &(stops.find(endid)->second);

		Link link(id, name, length, start, end);

		links.push_back(link);

	}

	return 0;
}

int create_graph(ifstream &stops_fs, ifstream &links_fs, Graph **graph)
{

	// call above functions
	int err;
	map<int, Stop> stops{};
	if (read_in_stops(stops_fs, stops)) return 1;
	stops_fs.close();

	list<Link> links;
	if (read_in_links(links_fs, links, stops)) return 1;
	links_fs.close();

	*graph = new Graph(stops, links);

	return 0;

}