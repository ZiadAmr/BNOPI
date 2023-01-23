#!/bin/python3

# downloads a file from OSM containing all the ways that buses can drive on in a radius, as well as the nodes they run on.
# run with -h option for help

import argparse
import requests


def float_in_range(n0, n1):
	def in_range(x):
		try:
			x = float(x)
		except ValueError:
			raise argparse.ArgumentTypeError(f"{repr(x)} not a floating-point literal")
		if not n0 <= x <= n1:
			raise argparse.ArgumentTypeError(
				f"{repr(x)} not in range [{str(n0)}, {str(n1)}]")
		return x
	return in_range


parser = argparse.ArgumentParser(
    prog=__file__,
    description='Downloads road data from OSM.')


parser.add_argument(
	'radius', help="Radius centered on (lat, lon) within which to get roads", type=float)
parser.add_argument(
	"latitude", help="Latitude in range [-90, 90]", type=float_in_range(-90, 90))
parser.add_argument(
	"longitude", help="Longitude in range [-180, 180]", type=float_in_range(-180, 180))

parser.add_argument("-o", dest="output", type=argparse.FileType("wb"),
                    action="store", required=False, metavar="outputfile", help="The filename of the output json file. Defaults to roads.json", default="roads.json")

args = parser.parse_args()


query = f"""[out:json];

// put all the ways in a set named "a"
way(around:{args.radius:},{args.latitude:},{args.longitude:})->.a;

// union these results
(
	way.a  [highway~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|road|busway|service"];
	way.a[highway="proposed"][proposed~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|road|busway|service"];
	way.a[highway="construction"][construction~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|road|busway|service"];
);

// expand set "_" (default set) to include nodes
(._;>;);

out;"""

response = requests.get(
	f"https://overpass-api.de/api/interpreter?data={query}")

if response.status_code != 200:
	raise RuntimeError(f"Request failed with exit code {response.status_code}.")

args.output.write(response.content)
