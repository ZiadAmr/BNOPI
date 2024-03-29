#!/usr/bin/env python3

# downloads a file from OSM containing all the stops in a radius.
# run with -h option for help

import argparse
import requests
import json


def float_in_range(n0, n1):
	def in_range(x):
		try:
			x = float(x)
		except ValueError:
			raise argparse.ArgumentTypeError(f"{repr(x)} not a floating-point literal")
		if not n0 <= x <= n1:
			raise argparse.ArgumentTypeError(f"{repr(x)} not in range [{str(n0)}, {str(n1)}]")
		return x
	return in_range

parser = argparse.ArgumentParser(
    prog=__file__,
    description='Downloads a list of stops from OSM. Uses map data obtained from OpenStreetMap (see openstreetmap.org/copyright).')



parser.add_argument('radius', help="Radius in meters, centered on (lat, lon), within which to get bus stops", type=float)
parser.add_argument("latitude", help="Latitude in range [-90, 90]", type=float_in_range(-90, 90))
parser.add_argument("longitude", help="Longitude in range [-180, 180]", type=float_in_range(-180, 180))

parser.add_argument("-o", dest="output", type=argparse.FileType("w"),
                    action="store", required=False, metavar="outputfile", help="The filename of the output json file. Defaults to stops.json", default="stops.json")

args = parser.parse_args()


query = f"""[out:json];
node(around:{args.radius:},{args.latitude:},{args.longitude:})[highway=bus_stop];
out;"""

response = requests.get(f"https://overpass-api.de/api/interpreter?data={query}")

if response.status_code != 200:
	raise RuntimeError(f"Request failed with exit code {response.status_code}.")





# convert to stage format

data = json.loads(response.content)

stops = []

count = 0
for el in data["elements"]:

	name = el["tags"]["name"] if "name" in el["tags"] else str(el["id"])

	stop = {"name": name,
         "id": el["id"],
         "lat": el["lat"],
         "lon": el["lon"]}
	stops.append(stop)

args.output.write(json.dumps({"stops": stops}))



