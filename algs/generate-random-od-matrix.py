#!/usr/bin/env python3

import argparse
import json
import random

def positive_int(x):
	try:
		y = int(x)
	except ValueError:
		raise argparse.ArgumentTypeError(f"{repr(x)} not a number")
	else:
		if y <= 0:
			raise argparse.ArgumentTypeError(f"{repr(x)} not postive")
	return y

parser = argparse.ArgumentParser(
    prog=__file__,
    description='Creates a stop-to-stop origin-destination matrix by randomly assigning the journeys.')
parser.add_argument("stops", type=argparse.FileType("r"),
                    action="store", help="A json file containing the stops. See the stage format specification.")
parser.add_argument("-n", "--num-users", dest="num_users", metavar="N", action="store", required=False,
                    help="Number of passengers in OD matrix. Default is 100", default=100, type=positive_int)
parser.add_argument("-o", dest="output", type=argparse.FileType("w"),
                    action="store", required=False, metavar="outputfile", help="The filename of the output OD matrix file. Defaults to od-matrix.json", default="od-matrix.json")


args = parser.parse_args()


stop_data = json.loads(args.stops.read())
stops_arr = stop_data["stops"]
del stop_data

if len(stops_arr) < 2:
	raise Exception("Number of stops must be >= 2 to create origin/destination demands")

# initialize 2d array
od_matrix = [[0]*len(stops_arr) for _ in range(len(stops_arr))]

# random demands
for _ in range(args.num_users):
	origin = random.randint(0, len(stops_arr)-1)
	destination = random.randint(0, len(stops_arr)-2)
	if destination >= origin:
		destination += 1
	
	od_matrix[origin][destination] += 1

# convert to json
demands = []
for origin_stop, destinations in zip(stops_arr, od_matrix):
	dests = []
	for dest_key, n in enumerate(destinations):
		if n == 0:
			continue
		dest_stop = stops_arr[dest_key]
		dests.append({"id": dest_stop["id"], "n": n})

	# if no destinations from an origin, ignore.
	if len(dests) == 0:
		continue

	demands.append({
		"id": origin_stop["id"],
		"dests": dests
	})

json_obj = {
	"snapshots": [
		{
			"time": "00:00",
			"demands": demands
		}
	]
}

args.output.write(json.dumps(json_obj))

