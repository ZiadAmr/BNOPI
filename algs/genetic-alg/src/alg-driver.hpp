#pragma once
#include "common.hpp"

/**
 * @brief Abstract driver class for algorithms
 *
 */
class AlgDriver
{
public:
	/**
	 * @brief Create a new generation of offspring and replace parents
	 * 
	 */
	virtual void step() = 0;

	/**
	 * @brief Get the best route network
	 * 
	 * @return RouteNet 
	 */
	virtual RouteNet get_best_routenet() = 0;

private:

	/**
	 * @brief Function to determine when to stop doing steps
	 * 
	 * @return true 
	 * @return false 
	 */
	virtual bool stopping_condition_met() = 0;

public:

	/**
	 * @brief Do a complete run of the algorithm
	 * 
	 */
	void run() {
		while (!stopping_condition_met()) {
			step();
		}
	}

};
