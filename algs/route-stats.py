#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser(
    prog=__file__,
    description='Calculate average length of routes in several route networks')
parser.add_argument("connection_graph", metavar="connection-graph", type=argparse.FileType("r"),
                    action="store", help="stop conenction graph")
parser.add_argument("route_networks", metavar="route-network", type=argparse.FileType("r"),
                    action="store", help="file containing route networks, with one network per line.")
parser.add_argument("stops", type=argparse.FileType("r"),
                    action="store", help="bus stops")


args = parser.parse_args()

graph = json.loads(args.connection_graph.read())
# routenet = json.loads(args.route_networks.read())
link_d = {link["id"]: link for link in graph["links"]}
points_d = {point["id"]: point for point in graph["points"]}
stops = json.loads(args.stops.read())
stop_d = {stop["id"]:stop for stop in stops["stops"]}


for line in args.route_networks.read().split("\n"):
	if line == "":
		continue
	routenet = json.loads(line)

	total_route_length = 0
	for route in routenet["routes"]:
		for linkid in route["links"]:
			total_route_length += link_d[linkid]["length"]
		
	avg_route_length = total_route_length / len(routenet["routes"])

	print(avg_route_length)
		
