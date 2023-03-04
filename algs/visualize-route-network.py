#!/bin/python3

import matplotlib.pyplot as plt
import argparse
import json
from math import pi, radians
from random import random

parser = argparse.ArgumentParser(
    prog=__file__,
    description='Display a route network in matplotlib')
parser.add_argument("connection_graph", metavar="connection-graph", type=argparse.FileType("r"),
                    action="store", help="stop conenction graph")
parser.add_argument("route_network", metavar="route-network", type=argparse.FileType("r"),
                    action="store", help="route network to display")
parser.add_argument("stops", type=argparse.FileType("r"),
                    action="store", help="bus stops")

parser.add_argument("-r", "--real-links", dest="real_links", action="store_true",
                    help="display the paths the links take in real life, rather than just straight lines between stops.")

args = parser.parse_args()

graph = json.loads(args.connection_graph.read())
routenet = json.loads(args.route_network.read())
link_d = {link["id"]: link for link in graph["links"]}
points_d = {point["id"]: point for point in graph["points"]}
stops = json.loads(args.stops.read())
stop_d = {stop["id"]:stop for stop in stops["stops"]}

# display each route network as a line with points on for the stops. Also arrows for the direction
# linewidth decreases each time
width = 10

cols = [tuple((random() for _ in range(3))) for _ in routenet["routes"]]
# decreasing line widths
widths = [10 - 7*i/len(routenet["routes"]) for i in range(len(routenet["routes"]))]

for route, col, width in zip(routenet["routes"], cols, widths):

    
	for stopid, linkid in zip(route["stops"], route["links"]):
		link = link_d[linkid]
	
		# draw lines between the stop
		lat_pts = [points_d[point]["lat"] for point in link["points"]]
		lon_pts = [points_d[point]["lon"] for point in link["points"]]
		plt.plot(lon_pts, lat_pts, color=col, lw=width)


for route, col, width in zip(routenet["routes"], cols, widths):

	for stopid in route["stops"]:
		stop = stop_d[stopid]
		link = link_d[linkid]

		# draw circle where the stop is
		plt.plot(stop["lon"], stop["lat"], marker="o", markersize=width,
		         markeredgecolor=col, markerfacecolor=col)

plt.show()