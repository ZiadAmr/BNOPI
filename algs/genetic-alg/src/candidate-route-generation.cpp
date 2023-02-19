#include "candidate-route-generation.hpp"
using namespace std;

// remember to do exception handling from the genetic-algorithm.cpp

RouteNet generateRouteSet(AlgSettings setting, Graph stop_connection)
{
    // Prints out the total number of bus stops we have loded
    if (verbose)
    {
        cout << "There are " << stop_connection.getSize() << " many stops in my graph" << endl;
    }

    // A vector that stores the stops so that we can sample from it.
    // When a stop is exhausted it is removed from the vector
    vector<int> non_exhausted_stops;

    for (auto stops : stop_connection.stops)
    {
        non_exhausted_stops.push_back(stops.first);
    }

    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, non_exhausted_stops.size());

    for (int i = 0; i < 10; i++)
    {
        int random_int = dist(rng);
        cout << "The ID of a random stop: " << random_int << endl;
    }

    return RouteNet();
}

Population generatePopulation(AlgSettings setting, Graph stop_connection)
{

    // Make sure to do some pre-processing steps to identify if the algorithm will fail

    Population population;
    for (int i = 0; i < setting.population_size; i++)
    {

        auto candidate = generateRouteSet(setting, stop_connection);

        if (candidate.empty())
        {
            throw "Invalid parameter for graph";
        }

        population.push_back(candidate);
    }

    return population;
}
