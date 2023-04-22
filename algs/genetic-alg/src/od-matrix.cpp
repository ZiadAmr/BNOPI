
#include "od-matrix.hpp"

using namespace OD;
using namespace std;
using namespace nlohmann;

Matrix::Matrix(json &demands, Graph &graph)
{
	for (json demand : demands) {

		Origin origin;
		origin.stop = &graph.stops[demand["id"]];

		for (json dest: demand["dests"]) {
			Destination destination;
			destination.stop = &graph.stops[dest["id"]];
			destination.n = dest["n"];
			origin.destinations.push_back(destination);
		}

		origins.push_back(origin);
	}

}