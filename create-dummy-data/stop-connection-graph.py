#!/bin/python3

import json
from math import sqrt

# command to download routes:
# wget -O coventry-routes.json "https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0Arelation%28around%3A7000.0%2C52.4128%2C-1.5090%29%5Broute%3D%22bus%22%5D%3B%0A%28._%3B%3E%3B%29%3B%0Aout%3B"

# [out:json];
# relation(around:7000.0,52.4128,-1.5090)[route="bus"];
# (._;>;);
# out;

# add a directed edge between 2 stops if there is a route that has them as a connection.

# ideas in future - move bus stop s onto a node u such that:
#	u is contained in a way w
#	there is a bus route relation that contains both u and w
#	dist(u,s) is at a minimum over all u that satisfy the above 2 properties

##### REQUIRES stops.json to be generated already. We only add connections between stops that appear in stops.json.


with open("stops.json", "r") as f:
	stops = json.loads(f.read())
stop_dict = {stop["id"] : stop for stop in stops["stops"]}
del stops

with open("coventry-routes.json", "r") as f:
	data = json.loads(f.read())


_id = 0
def next_id():
	global _id
	_id += 1
	return _id

links = []

for el in data["elements"]:

	if el["type"] == "relation" and len(el["members"]) > 1:
		
		for n0, n1 in zip(el["members"][:-1], el["members"][1:]):
			if n1["type"] == "way":
				break
			if n0["ref"] not in stop_dict or n1["ref"] not in stop_dict:
				continue
			
			# in future d should also contain a list of nodes between the two stops.
			s0 = stop_dict[n0["ref"]]
			s1 = stop_dict[n1["ref"]]
			d = {
				"id": next_id(),
				"name": s0["name"] + " => " + s1["name"],
				# just use straight line distance for now.
				"length": sqrt((s0["lat"]-s1["lat"])**2+(s0["lon"]-s1["lon"])**2),
				"speed" : {"0:00":30},
				"startid": s0["id"],
				"endid": s1["id"]
			}

			links.append(d)

with open("stop-connections.json", "w") as f:
	f.write(json.dumps({"links":links}))



		

