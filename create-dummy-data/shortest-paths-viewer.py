#!/bin/python3

from sys import argv

if len(argv) != 3:
	raise RuntimeError("pass the two stops as command line arguments")

from_stopid_query = int(argv[1])
to_stopid_query = int(argv[2])


with open("shortest_paths_extended.txt", "r") as f:
	shortest_paths = eval(f.read())

for distance, from_stopid, path, to_stopid in shortest_paths:
	if from_stopid == from_stopid_query and to_stopid == to_stopid_query:
		print("distance: " + str(distance))
		print("path: " + str(path))
		print("".join([f"node({nodeid});" for nodeid in path]))
		break



