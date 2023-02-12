#pragma once
#include "common.hpp"
#include <vector>




typedef std::vector<RouteNet> Population;




/**
 * @brief Driver class for the Simple Multi-Objective (SMO) algorithm
 * 
 */
class SMODriver {
private:
	/**
	 * @brief Directional route. Contains `inverted` bit determinining to which endpoint of the route we can add links.
	 * 
	 */
	struct DRoute {
		bool inverted; // true = backwards
		Route r;
	};

	typedef std::vector<DRoute> DRouteNet; // Directional route network
	typedef std::vector<DRouteNet> DPopulation; // Directional population

	DPopulation population;
	AlgSettings settings;

public:
	/**
	 * @brief Construct a new SMODriver object
	 * 
	 * @param initial_population Initial population of route networks
	 * @param settings Struct containing general settings for the algorithm
	 */
	SMODriver(Population initial_population, AlgSettings &settings);

	/**
	 * @brief Create a new generation of offspring and replace parents
	 * 
	 */
	void step();
	/**
	 * @brief Get the population of route networks.
	 * 
	 * @return Population 
	 */
	Population get_population();

private:
	/**
	 * @brief Convert directional route network to regular route network
	 * 
	 * @param drn 
	 * @return RouteNet& 
	 */
	RouteNet& DRouteNet_to_RouteNet(DRouteNet &drn);

	/**
	 * @brief Convert directional population to regular population
	 * 
	 * @param dp 
	 * @return Population& 
	 */
	Population& DPopulation_to_Population(DPopulation &dp);

	/**
	 * @brief Applies procedure to a route network as described in the paper.
	 * 
	 * @param route_net Route network to make a small change to
	 */
	void make_small_change(DRouteNet &route_net);
	/**
	 * @brief Applies procedure to a route network as described in the paper.
	 *
	 * @param route Route to make a small change to
	 */
	void make_small_change(DRoute &route);


	/**
	 * @brief Add a stop to the end of a route. Choose one of the possibilities at random.
	 * This function allows loops in the route.
	 * 
	 * @param route Route onto which to add a link
	 * @return Boolean denoting whether a link was added successfully.
	 */
	bool add_link(DRoute &route);

	/**
	 * @brief Removes the link from the start.
	 * Does NOT check to see if this is a subroute.
	 * 
	 * @param route Route from which to remove the first link
	 * @return The link that was removed
	 */
	Link* remove_link(DRoute &route);

	/**
	 * @brief Flips the dir bit in the Droute.
	 * 
	 * @param route 
	 */
	void invert_order(DRoute & route);

};


