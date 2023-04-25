#include "objective.hpp"
#include "link.hpp"
#include "stop.hpp"
#include "common.hpp"
#include <vector>
#include <utility>
#include <algorithm>
#include <map>

// need time t for time required to transfer between routes, need theta to measure inconvenience of the transfer
// transit edges have length t + theta
// then use dijkstra's to find the cost of getting to the destination through our transit network
double cost(int i, int j) {return 0;}; 

// // for now this considers just one route, extend to the whole transit graph
std::pair<double, double> opt(std::vector<Stop *> &stops, RouteNet &routenet, OD::Matrix &od_matrix) {

    // std::cout << "Entering OPT \n";
    float Cp = 0;
    for (OD::Origin& origin : od_matrix.origins) {
        for (OD::Destination& destination: origin.destinations) {
            float d = dijkstra(routenet, stops, origin.stop->cid, destination.stop->cid);
            Cp += destination.n * d;
            // std::cout << Cp << "= " << destination.n <<  " * " << d << std::endl;
        }
    }
    // std::cout << "Fist loop done \n";

    double Co = 0; // total length of route, extend for multiple routes later
    for(int i = 0; i < routenet.size(); i++){
        for(int j = 0; j < routenet[i].size(); j++){
            Co += routenet[i][j]->length;
        }
    }

    // paper  talks about tradeoff between Cp an Co using multi-objective optimization algorithm, so I'm returning both
    // std::cout << "OUTPUT: " << Cp << " " << Co << "\n";
    return std::make_pair(Cp, Co);
}

float dijkstra(RouteNet &routes, std::vector<Stop*> &stops, int source, int destination){
    // 1 - make set of unvisited nodes

    // int *neighbours = new int[stops.size()*stops.size()]();
    std::vector< std::vector<std::pair<int,float>>> adjacency(stops.size());
    for(int i = 0; i < routes.size(); i++){
        for(int j = 0; j < routes[i].size(); j++){
            int start = routes[i][j]->start->id;
            int end = routes[i][j]->end->id;

            auto start_loc = std::find_if(stops.begin(), stops.end(), [start](const Stop* st){return st->id == start;}) - stops.begin();
            auto end_loc = std::find_if(stops.begin(), stops.end(), [end](const Stop* st){return st->id == end;}) - stops.begin();

            // neighbours[start_loc * end_loc] = i;
            // adjacency[start_loc].push_back({end_loc, routes[i][j]->length});
            // adjacency[end_loc].push_back({end_loc, routes[i][j]->length});
            // std::cout << end_loc << " -- " << routes[i][j]->length << " ( " << i  << ", " << j << ") out of " << stops.size() << " - "  << routes[i].size()<< std::endl; 
            adjacency[start_loc].push_back(std::make_pair(end_loc, routes[i][j]->length));
            adjacency[end_loc].push_back(std::make_pair(start_loc, routes[i][j]->length));
        }
    }

    std::vector<bool> visited;
    std::vector<float> distance;
    for(int i = 0; i < stops.size(); i++){
        visited.push_back(false);
        distance.push_back(INT32_MAX);
    }
    distance[source]=0;
    visited[source]=true;

    for(int i = 0; i < visited.size(); i++){
        if(visited[i] == true){
            for(int j = 0; j < visited.size(); j++){
                if(visited[j] == false && std::find_if(adjacency[i].begin(), adjacency[i].end(),  [j](const std::pair<int, float>& pair){return std::get<0>(pair) == j;}) != adjacency[i].end() ){
                    visited[j] = true;
                    int dist_loc =  (std::find_if(adjacency[i].begin(), adjacency[i].end(),  [j](const std::pair<int, float>& pair){return std::get<1>(pair) == j;}) - adjacency[i].begin());
                    float dist = std::get<1>(adjacency[i][dist_loc]);
                    distance[j] = distance[i] + dist;
                }

                // std::cout << j << " - " << destination;
                if(j == destination){
                    return distance[j];
                }
            }
        }
    }
    return -1;
}