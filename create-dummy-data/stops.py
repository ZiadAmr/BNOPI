#!/bin/python3

import json

# command to download stops:
# wget -O coventry-stops.json "https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0Anode%28around%3A7000.0%2C52.4128%2C-1.5090%29%5Bhighway%3Dbus_stop%5D%3B%0Aout%3B"

# [out:json];
# node(around:7000.0,52.4128,-1.5090)[highway=bus_stop];
# out;

print("parse json")
with open("coventry-stops.json", "r") as f:
	data = json.loads(f.read())

stops = []

print("create dicts")
count = 0
for el in data["elements"]:

	name = el["tags"]["name"] if "name" in el["tags"] else str(el["id"])

	stop = {"name": name,
				"id": el["id"],
				"lat": el["lat"],
				"lon": el["lon"]}
	stops.append(stop)

	# count += 1
	# if count > 10: break

print("dump json")
with open("stops.json", "w") as f:
	f.write(json.dumps({"stops":stops}))
