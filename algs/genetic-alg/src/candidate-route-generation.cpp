#include "candidate-route-generation.hpp"
using namespace std;

// remember to do exception handling from the genetic-algorithm.cpp

RouteNet generateRouteSet(int minRouteSize, int maxRouteSize, int numberOfRoutes, Population population)
{
    return RouteNet();
}

Population generatePopulation(int minRouteSize, int maxRouteSize, int numberOfRoutes, int populationSize)
{
    Population population;
    for (int i = 0; i < populationSize; i++)
    {

        auto candidate = generateRouteSet(minRouteSize, maxRouteSize, numberOfRoutes, population);

        if (candidate.empty())
        {
            throw "Invalid parameter for graph";
        }

        population.push_back(candidate);
    }

    return population;
}