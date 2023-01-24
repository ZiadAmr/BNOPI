#!/bin/python3

import matplotlib.pyplot as plt
import argparse
import json
from math import pi, radians

parser = argparse.ArgumentParser(
    prog=__file__,
    description='Display a stop connection graph in matplotlib')
parser.add_argument("connection_graph", metavar="connection-graph", type=argparse.FileType("r"),
                    action="store", help="The stop conenction graph to display")
parser.add_argument("-r", "--real-links", dest="real_links", action="store_true", help="display the paths the links take in real life, rather than just straight lines between stops.")

args = parser.parse_args()

graph = json.loads(args.connection_graph.read())


# we will warp all the points into place in the map.

points = {point["id"]: point for point in graph["points"]}


to_plot = []


if not args.real_links:
	
	for link in graph["links"]:
		
		# get stopping positions of the bus at the start and the end of the link

		# do not plot self-loops.
		if link["points"][0] == link["points"][-1]:
			continue

		start_pt = points[link["points"][0]]
		end_pt = points[link["points"][-1]]

		start_loc = (start_pt["lat"], start_pt["lon"])
		end_loc = (end_pt["lat"], end_pt["lon"])
		to_plot.append((start_loc, end_loc))

else:

	for link in graph["links"]:

		# get stopping positions of the bus at the start and the end of the link

		for start_id, end_id in zip(link["points"], link["points"][1:]):
			start_pt = points[start_id]
			end_pt = points[end_id]
			start_loc = (start_pt["lat"], start_pt["lon"])
			end_loc = (end_pt["lat"], end_pt["lon"])
			to_plot.append((start_loc, end_loc))


# get into right format for plt.plot
start_coords, end_coords = zip(*to_plot)
start_lat, start_lon = zip(*start_coords)
end_lat, end_lon = zip(*end_coords)

plt.plot(start_lon, start_lat, end_lon, end_lat, marker="o", linestyle="solid")



plt.show()




