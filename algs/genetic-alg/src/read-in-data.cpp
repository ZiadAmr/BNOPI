
#include "read-in-data.hpp"
#include <string>
// #include <json/json.h>
#include <nlohmann/json.hpp>
#include <iostream>

using namespace std;
using namespace nlohmann;


int read_in_stops(ifstream &stops_file, map<int, Stop> &stops)
{
	json data = json::parse(stops_file);
	// auto x = data["stops"];

	for (const auto stop_js : data["stops"])
	{
		string name = stop_js["name"].get<string>();
		int id = stop_js["id"].get<int>();
		double lat = stop_js["lat"].get<double>();
		double lon = stop_js["lon"].get<double>();

		Stop stop(name, id, lat, lon);
		stops.insert({id, stop});
	}
	return 0;
}

int read_in_links(ifstream &links_file, list<Link> &links, map<int, Stop> &stops)
{

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
		auto start_it = stops.find(startid);
		if (start_it == stops.end()) {
			cerr << "Connection graph references stop with id " << startid << ", not found in stops" << endl;
			return 1; 
		}
		auto end_it = stops.find(endid);
		if (end_it == stops.end()) {
			cerr << "Connection graph references stop with id " << endid << ", not found in stops" << endl;
			return 1; 
		}

		Stop *start = &(start_it->second);
		Stop *end = &(end_it->second);

		Link link(id, name, length, start, end);
		links.push_back(link);

		start->out_edges.push_back(&links.back());
		end->in_edges.push_back(&links.back());

	}

	return 0;
}

int create_graph(ifstream &stops_fs, ifstream &links_fs, Graph **graph)
{

	*graph = new Graph(map<int, Stop>(), list<Link>());

	// call above functions
	int err;
	if (read_in_stops(stops_fs, (*graph)->stops))
		return 1;
	stops_fs.close();

	list<Link> links;
	if (read_in_links(links_fs, (*graph)->links, (*graph)->stops))
		return 1;
	links_fs.close();

	// sort stops and set contiguous ids.
	(*graph)->set_cids();

	return 0;
}


std::string routenet_to_string(RouteNet& rn) {

	int id_counter = 0;

	json j;

	json routes = json::array();

	for (Route &r : rn) {
		
		json route;

		int id = id_counter++;
		route["id"] = id;
		// set the name of the route to firststop => laststop.
		// if there are no stops in the route then just make it the id.
		if (r.size() == 0) {
			route["name"] = std::to_string(id);
		} else {
			route["name"] = r.front()->start->name + " => " + r.back()->end->name;
		}
		
		// create list of stops and links
		json stops = json::array();
		json links = json::array();
		for (Link* link: r) {
			links.push_back(link->id);
			stops.push_back(link->start->id);
		};
		// add the last stop.
		if (r.size() != 0) {
			stops.push_back(r.back()->end->id);
		}

		route["stops"] = stops;
		route["links"] = links;

		// add route to routes
		routes.push_back(route);

	}

	j["routes"] = routes;

	return j.dump();
}

OD::Matrix read_in_od_matrix(std::ifstream &od_matrix_fs, Graph& graph) {

	// parse JSON
	json data = json::parse(od_matrix_fs);

	// TODO
	// ignore snapshots for now.
	// just import the demands of the first one.

	json demands;
	for (auto& s : data["snapshots"].items()) {
		demands = s.value()["demands"];
		break;
	}

	return OD::Matrix(demands, graph);
}

