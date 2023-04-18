#include "objective.hpp"
#include "link.hpp"
#include "stop.hpp"
#include <vector>
#include <utility>

// need time t for time required to transfer between routes, need theta to measure inconvenience of the transfer
// transit edges have length t + theta
// then use djikstra's to find the cost of getting to the destination through our transit network
double cost(int i, int j) {return 0;}; 

// for now this considers just one route, extend to the whole transit graph
std::pair<double, double> opt(std::vector<Stop> stops, std::vector<Link> route, std::vector<std::vector<double>> od){
    double Cp = 0;
    for(int i = 0; i < stops.size(); i++){
        for(int j = 0; j < stops.size(); j++){
            Cp += od[i][j] * cost(i,j);
        }
    }

    double Co = 0; // total length of route, extend for multiple routes later
    for(int i = 0; i < route.size(); i++){
        Co += route[i].length;
    }

    // paper  talks about tradeoff between Cp an Co using multi-objective optimization algorithm, so I'm returning both
    return std::make_pair(Cp, Co); 
}