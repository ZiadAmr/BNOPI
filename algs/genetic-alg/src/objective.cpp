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
// then use djikstra's to find the cost of getting to the destination through our transit network
double cost(int i, int j) {return 0;}; 

// for now this considers just one route, extend to the whole transit graph
std::pair<double, double> opt(std::vector<Stop> stops, RouteNet route, std::vector<std::vector<double>> od){
    double Cp = 0;
    for(int i = 0; i < stops.size(); i++){
        for(int j = 0; j < stops.size(); j++){
            Cp += od[i][j] * djikstra(route, stops, i,j);
        }
    }

    double Co = 0; // total length of route, extend for multiple routes later
    for(int i = 0; i < route.size(); i++){
        for(int j = 0; j < route[i].size(); j++){
            Co += route[i][j]->length;
        }
    }

    // paper  talks about tradeoff between Cp an Co using multi-objective optimization algorithm, so I'm returning both
    return std::make_pair(Cp, Co); 
}

float djikstra(RouteNet routes, std::vector<Stop> stops, int source, int destination){
    // 1 - make set of unvisited nodes

    // int *neighbours = new int[stops.size()*stops.size()]();
    std::vector< std::vector<std::pair<int,float>>> adjacency;
    for(int i = 0; i < routes.size(); i++){
        for(int j = 0; j < routes[i].size(); j++){
            int start = routes[i][j]->start->id;
            int end = routes[i][j]->end->id;

            auto start_loc = std::find_if(stops.begin(), stops.end(), [start](const Stop& st){return st.id == start;}) - stops.begin();
            auto end_loc = std::find_if(stops.begin(), stops.end(), [end](const Stop& st){return st.id == end;}) - stops.begin();

            // neighbours[start_loc * end_loc] = i;
            adjacency[start_loc].push_back({end_loc, routes[i][j]->length});
            adjacency[end_loc].push_back({end_loc, routes[i][j]->length});
        }
    }

    std::vector<bool> visited;
    std::vector<float> distance;
    for(int i = 0; i < stops.size(); i++){
        visited.push_back(false);
        distance.push_back(INT32_MAX);
    }
    distance[source]=0;

    for(int i = 0; i < visited.size(); i++){
        if(visited[i] == true){
            for(int j = 0; j < visited.size(); j++){
                if(visited[j] == false && std::find_if(adjacency[i].begin(), adjacency[i].end(),  [j](const std::pair<int, float>& pair){return std::get<0>(pair) == j;}) != adjacency[i].end() ){
                    visited[j] = true;
                    int dist_loc =  (std::find_if(adjacency[i].begin(), adjacency[i].end(),  [j](const std::pair<int, float>& pair){return std::get<1>(pair) == j;}) - adjacency[i].begin());
                    float dist = std::get<1>(adjacency[i][dist_loc]);
                    distance[j] = distance[i] + dist;
                }

                if(j == destination){
                    return distance[j];
                }
            }
        }
    }

}