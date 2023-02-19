#include "candidate-route-generation.hpp"
using namespace std;

// remember to do exception handling from the genetic-algorithm.cpp

RouteNet generateRouteSet(int minRouteSize, int maxRouteSize, int numberOfRoutes, Graph stop_connection)
{

    return RouteNet();
}

Population generatePopulation(int minRouteSize, int maxRouteSize, int numberOfRoutes, int populationSize, Graph stop_connection)
{
    Population population;
    for (int i = 0; i < populationSize; i++)
    {

        auto candidate = generateRouteSet(minRouteSize, maxRouteSize, numberOfRoutes, stop_connection);

        if (candidate.empty())
        {
            throw "Invalid parameter for graph";
        }

        population.push_back(candidate);
    }

    return population;
}
