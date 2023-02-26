
#include "../src/common.hpp"
#include "../src/stop.hpp"
#include "../src/read-in-data.hpp"
#include <string>

// int verbose = 0;

int main(int argc, char** argv) {

	Stop stop1("stop1", 1, 0, 0);
	Stop stop2("stop2", 2, 0, 0.001);
	Stop stop3("stop3", 3, 0, 0.002);
	Stop stop4("stop4", 4, 0.001, 0.001);

	Link link1(1, "1=>2", 0.001, &stop1, &stop2);
	Link link2(2, "2=>3", 0.001, &stop2, &stop3);
	Link link3(3, "2=>4", 0.001, &stop2, &stop4);

	stop1.out_edges.push_back(&link1);
	stop2.in_edges.push_back(&link1);
	stop2.out_edges.push_back(&link2);
	stop3.in_edges.push_back(&link2);
	stop2.out_edges.push_back(&link3);
	stop4.in_edges.push_back(&link3);

	Route route1 = {&link1, &link2};
	Route route2 = {&link3};

	RouteNet route_net = {route1, route2};

	std::cout << routenet_to_string(route_net) << std::endl;

}