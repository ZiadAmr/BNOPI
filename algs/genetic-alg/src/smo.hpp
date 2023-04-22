#pragma once
#include "common.hpp"
#include "alg-driver.hpp"
#include "od-matrix.hpp"
#include <vector>

/**
 * @brief Driver class for the Simple Multi-Objective (SMO) algorithm
 * 
 */
class SMODriver : public AlgDriver {
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
	OD::Matrix &od_matrix;
	AlgSettings settings;

	std::vector<float> parent_fitness;
	float best_so_far_fitness = 0;
	RouteNet best_so_far_routenet;

	// iteration number
	int it = 0;

	// total iterations
	int niter;

public:
	/**
	 * @brief Construct a new SMODriver object
	 * 
	 * @param initial_population Initial population of route networks
	 * @param settings Struct containing general settings for the algorithm
	 */
	SMODriver(Population initial_population, OD::Matrix &od_matrix, AlgSettings &settings, int niter);

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

	RouteNet get_best_routenet();

private:

	bool stopping_condition_met();

	/**
	 * @brief Check if a network exists in a population that contains the same routes as the query network
	 * 
	 * @param drn Query network
	 * @param dp Population in which to look for duplicates
	 * @return true 
	 * @return false 
	 */
	bool is_duplicate(DRouteNet& drn, DPopulation& dp);

	/**
	 * @brief Check whether a route network is feasible. 
	 * If it isn't, then in `step` we keep calling `make_small_change` until it is.
	 * 
	 * @param rn Route network to check
	 * @return true - feasible
	 * @return false - infeasible
	 */
	bool is_feasible(DRouteNet& rn);

	/**
	 * @brief Evaluates fitness of route network
	 * 
	 * @param rn 
	 * @return float 
	 */
	float objective_function(RouteNet& rn);

	/**
	 * @brief Convert directional route network to regular route network
	 * 
	 * @param drn 
	 * @return RouteNet& 
	 */
	RouteNet DRouteNet_to_RouteNet(DRouteNet &drn);

	/**
	 * @brief Convert directional population to regular population
	 * 
	 * @param dp 
	 * @return Population& 
	 */
	Population DPopulation_to_Population(DPopulation &dp);

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


