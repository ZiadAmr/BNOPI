#pragma once
#include <map>
#include <list>
#include <nlohmann/json.hpp>
#include "stop.hpp"
#include "graph.hpp"

namespace OD {



	struct Destination {
		Stop *stop;
		int n;
	};

	struct Origin {
		Stop *stop;
		std::list<Destination> destinations;
	};

	class Matrix {
		public: 
		std::list<Origin> origins;

		/**
		 * @brief Construct a new Matrix object from json demands
		 * 
		 * @param demands JSON array. Value of "demands" key in OD matrix stage format.
		 * @param graph Stop connection graph
		 */
		Matrix(nlohmann::json &demands, Graph &graph);
	};



}

