#!/bin/python3

import multiprocessing
from joblib import Parallel, delayed, cpu_count # for parallelizing for loops.
import math
import json
from math import sqrt, inf, sin, cos, atan2, radians
from numbers import Number
from sys import exit
from re import search
from typing import List
from os.path import isfile

def positive_float(x):
	try:
		y = float(x)
	except ValueError:
		raise argparse.ArgumentTypeError(f"{repr(x)} not a number")
	else:
		if y <= 0:
			raise argparse.ArgumentTypeError(f"{repr(x)} not postive")
	return y

import argparse
parser = argparse.ArgumentParser(
    prog=__file__,
    description='Create the stop connection graph from stop and road data.')
parser.add_argument("stops", type=argparse.FileType("r"),
                    action="store", help="A json file containing the stops. See the stage format specification.")
parser.add_argument("roads", type=argparse.FileType("r"),
                    action="store", help="A json file containing the roads. See the stage format specification.")
parser.add_argument("--drive-on-left", dest="drive_on_left", action="store_true", help="Specifies that road users should on the left. If omitted, it is assumed road users drive on the right.")
parser.add_argument("-d", "--max-search-distance", dest="max_search_distance", metavar="dist", action="store", required=False,
                    help="Specifies the maximum distance to search for neighboring stops, in meters. Defaults to 1000.", default=1000, type=positive_float)
parser.add_argument("-o", dest="output", type=argparse.FileType("w"),
                    action="store", required=False, metavar="outputfile", help="The filename of the output json file. Defaults to stop-connection-graph.json", default="stop-connection-graph.json")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true")


args = parser.parse_args()

# !!!!!!!! 
drive_on_left = args.drive_on_left
max_search_distance = args.max_search_distance # metres

print(f"There are {cpu_count()} CPUs.")

# read in data.

stop_data = json.loads(args.stops.read())
stops = {stop["id"]: stop for stop in stop_data["stops"]}
del stop_data
# args.stops.close()
# del args.stops

road_data = json.loads(args.roads.read())
# args.roads.close()
# del args.roads


# TODO need to check for height restrictions
# ================================================================================== command to download routes:

# wget -O coventry-routes.json "https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0Arelation%28around%3A7000.0%2C52.4128%2C-1.5090%29%5Broute%3D%22bus%22%5D%3B%0A%28._%3B%3E%3B%29%3B%0Aout%3B"

# [out:json];
# relation(around:7000.0,52.4128,-1.5090)[route="bus"];
# (._;>;);
# out;

# ================================================================================== command to download roads:

# wget -O coventry-roads.json https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0A%0A%2F%2F%20put%20all%20the%20ways%20in%20a%20set%20named%20%22a%22%0Away%28around%3A7000%2C52.4128%2C-1.5090%29-%3E.a%3B%0A%0A%2F%2F%20union%20these%20results%0A%28%0A%09way.a%20%20%5Bhighway~%22motorway%7Ctrunk%7Cprimary%7Csecondary%7Ctertiary%7Cunclassified%7Cresidential%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Csecondary_link%7Ctertiary_link%7Cliving_street%7Croad%7Cbusway%7Cservice%22%5D%3B%0A%09way.a%5Bhighway%3D%22proposed%22%5D%5Bproposed~%22motorway%7Ctrunk%7Cprimary%7Csecondary%7Ctertiary%7Cunclassified%7Cresidential%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Csecondary_link%7Ctertiary_link%7Cliving_street%7Croad%7Cbusway%7Cservice%22%5D%3B%0A%09way.a%5Bhighway%3D%22construction%22%5D%5Bconstruction~%22motorway%7Ctrunk%7Cprimary%7Csecondary%7Ctertiary%7Cunclassified%7Cresidential%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Csecondary_link%7Ctertiary_link%7Cliving_street%7Croad%7Cbusway%7Cservice%22%5D%3B%0A%29%3B%0A%0A%2F%2F%20expand%20set%20%22_%22%20%28default%20set%29%20to%20include%20nodes%0A%28._%3B%3E%3B%29%3B%0A%0Aout%3B

# [out:json];
#
# // put all the ways in a set named "a"
# way(around:7000,52.4128,-1.5090)->.a;
#
# // union these results
# (
# 	way.a  [highway~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|road|busway|service"];
# 	way.a[highway="proposed"][proposed~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|road|busway|service"];
# 	way.a[highway="construction"][construction~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|road|busway|service"];
# );
#
# // expand set "_" (default set) to include nodes
# (._;>;);
#
# out;









# add a directed edge between 2 stops if there is a route that has them as a connection.

# ideas in future - move bus stop s onto a node u such that:
#	u is contained in a way w
#	there is a bus route relation that contains both u and w
#	dist(u,s) is at a minimum over all u that satisfy the above 2 properties

##### REQUIRES stops.json to be generated already. We only add connections between stops that appear in stops.json.


# finds the point on the line (p0x, p0y)=>(p1x, p1y) that is closest to (cx, cy)
def closest_point_on_line(p0x: Number, p0y: Number, p1x: Number, p1y: Number, cx: Number, cy: Number) -> 'tuple[Number, Number]':
	
	# parametrized vector eqn of line: p = a + bt
	ax = p0x
	ay = p0y
	bx = p1x-p0x
	by = p1y-p0y

	# how far along the line we are:
	t = (bx*(cx-ax)+by*(cy-ay))/(bx**2+by**2)

	# if t out of range [0,1] just return the endpoint
	if t <= 0: return (p0x, p0y, t)
	elif t >= 1: return (p1x, p1y, t)
	else: return (ax+t*bx, ay+t*by, t)

# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
def surface_distance(lat0, lon0, lat1, lon1):

	# hopefully should prevent divide by zero errors
	if lat0 == lat1 and lon0 == lon1: return 0.0

	lat0 = radians(lat0)
	lon0 = radians(lon0)
	lat1 = radians(lat1)
	lon1 = radians(lon1)

	# approximate radius of earth in m
	R = 6373.0 * 1000

	dlon = lon1 - lon0
	dlat = lat1 - lat0

	a = sin(dlat / 2)**2 + cos(lat0) * cos(lat1) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance

# https://stackoverflow.com/questions/1560492/how-to-tell-whether-a-point-is-to-the-right-or-left-side-of-a-line
# Where a = line point 1; b = line point 2; c = point to check against.
def is_left(a, b, c):
    return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) > 0



r_major = 6378137.000
# https://gis.stackexchange.com/questions/156035/calculating-mercator-coordinates-from-lat-lon
def merc(lat, lon):
    x = r_major * math.radians(lon)
    scale = x/lon
    y = 180.0/math.pi * \
    	math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
    return (x, y)

# hand-inverted from the above. hope it's correct!
def amerc(x, y):
	lon = x/r_major * 180.0/math.pi
	# no idea why that - 45.0 should be there - but it doesn't work without TODO.
	lat = (2.0*math.atan(math.exp(y*math.pi/180.0*lon/x))-math.pi/4.0)*180.0/math.pi - 45.0
	return (lat, lon)

# https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

	





# preprocess the roads.
# create a set of "lines": section of a road that is joined by a straight line
nodes = dict()
ways = dict()
restrictions = dict()
lines = [] # (n0, n1, wayid)
# TODO: assumption - the area of nodes does not cross the north/south pole or lon=+-180
min_x = inf
max_x = -inf
min_y = inf
max_y = -inf


for el in road_data["elements"]:
	if el["type"] == "node":
		# also calculate the mercartor projection of the coords.
		merc_x, merc_y = merc(el["lat"], el["lon"])
		nodes[el["id"]] = el
		nodes[el["id"]]["mercx"] = merc_x
		nodes[el["id"]]["mercy"] = merc_y
		min_x = min(min_x, merc_x)
		max_x = max(max_x, merc_x)
		min_y = min(min_y, merc_y)
		max_y = max(max_y, merc_y)

	elif el["type"] == "way":
		el["stops"] = [] # add this for later
		ways[el["id"]] = el
		way_nodes = el["nodes"]
		for n0, n1 in zip(way_nodes[:-1], way_nodes[1:]):
			lines.append((n0, n1, el["id"]))

	elif el["type"] == "relation" and "tags" in el and "restriction" in el["tags"]:
		restrictions[el["id"]] = el

# make sure every node is strictly inside the bbox
max_x += 0.000000001
min_x -= 0.000000001
max_y += 0.000000001
min_y -= 0.000000001

# create a grid spacial index -- put the lines in bins based on areas they're in.
# to do this the mercartor projection is divided into a grid
square_width = 500 #metres
hor_squares = int((max_x - min_x)//square_width + 1)
vert_squares = int((max_y - min_y)//square_width + 1)
spac_in = [[[] for _ in range(hor_squares)] for _ in range(vert_squares)]

dx = max_x-min_x
dy = max_y-min_y

real_sq_width = dx/hor_squares
real_sq_height = dy/vert_squares

def merc_to_square(merc_x, merc_y):
	"""Return the sqaure in the spacial index which contains the mercator coordinates `(merc_x, merc_y)`."""
	sx = int((merc_x - min_x)/dx * hor_squares)
	sy = int((merc_y - min_y)/dy * vert_squares)
	return (sx, sy)

def square_to_merc(sx, sy):
	"""Return the mercator coordinates of the north-westerly corner of the square `(sx, sy)` in the spacial index."""
	merc_x = min_x + sx/hor_squares * dx
	merc_y = min_y + sy/vert_squares * dy
	return (merc_x, merc_y)

# find the squares that a line intersects with.
# code could be improved, e.g. Bresenham's line algorithm
for line in lines:
	# m* vars - merc coords
	# s* vars - square coords (in the spacial index grid)
	l0id, l1id, wayid = line
	m0x, m0y = (nodes[l0id]["mercx"], nodes[l0id]["mercy"])
	m1x, m1y = (nodes[l1id]["mercx"], nodes[l1id]["mercy"])
	# squares containing the endpoints
	s0x, s0y = merc_to_square(m0x, m0y)
	s1x, s1y = merc_to_square(m1x, m1y)
	# check all squares in the bbox that contains s0 and s1
	for six in range(min(s0x, s1x), max(s0x, s1x)+1):
		for siy in range(min(s0y, s1y), max(s0y, s1y)+1):
			if (six, siy) in ((s0x, s0y), (s1x, s1y)):
				spac_in[siy][six].append(line)
				continue
			# check to see if it intersects with any of the edges of the box
			mix, miy = square_to_merc(six, siy)
			if intersect((m0x, m0y), (m1x, m1y), (mix, miy), (mix+real_sq_width, miy)) or \
			intersect((m0x, m0y), (m1x, m1y), (mix+real_sq_width, miy), (mix+real_sq_width, miy+real_sq_height)) or \
			intersect((m0x, m0y), (m1x, m1y), (mix+real_sq_width, miy+real_sq_height), (mix, miy+real_sq_height)) or \
			intersect((m0x, m0y), (m1x, m1y), (mix, miy+real_sq_height), (mix, miy)):
				spac_in[siy][six].append(line)



# # check this is correct: output json for one of the squares
# test_nodes = []
# println = ""
# for l0id, l1id, _ in spac_in[vert_squares//2][hor_squares//2]:
# 	# test_nodes.append(nodes[l0id])
# 	# test_nodes.append(nodes[l1id])
# 	println += f"node(around:1,{str(nodes[l0id]['lat'])}, {str(nodes[l0id]['lon'])});\n"
# 	println += f"node(around:1,{str(nodes[l1id]['lat'])}, {str(nodes[l1id]['lon'])});\n"
# # print(json.dumps({"elements":test_nodes}))
# print(println)
# exit()
			



# calculate the stopping position for every stop by snapping to the road.
for stopid, stop in stops.items():
	# mercartor projection of stop
	stopmx, stopmy = merc(stop["lat"], stop["lon"])
	# find the square that contains the stop
	squarex, squarey = merc_to_square(stopmx, stopmy)

	min_dist_to_road = inf
	best_line = None
	best_stop_position = None

	# seach all squares in a 3x3 centered on this square
	for siy in range(max(0, squarey-1), min(vert_squares, squarey+2)):
		for six in range(max(0, squarex-1), min(hor_squares, squarex+2)):
			for line in spac_in[siy][six]:

				l0id, l1id, wayid = line
				m0x, m0y = (nodes[l0id]["mercx"], nodes[l0id]["mercy"])
				m1x, m1y = (nodes[l1id]["mercx"], nodes[l1id]["mercy"])

				cx, cy, t = closest_point_on_line(m0x, m0y, m1x, m1y, stopmx, stopmy)
				dist = sqrt((stopmx-cx)**2 + (stopmy-cy)**2)

				if dist < min_dist_to_road:
					min_dist_to_road = dist
					best_line = line
					best_stop_position = (cx, cy, t)
	
	# convert back from mercartor
	best_stop_lat, best_stop_lon = amerc(best_stop_position[0], best_stop_position[1])

	# find which side of the road the stop was on.
	# note: this works even if the closest point is at the end of the line, since if that were the case, the road must be bending away from us
	l0id, l1id, wayid = best_line
	m0x, m0y = (nodes[l0id]["mercx"], nodes[l0id]["mercy"])
	m1x, m1y = (nodes[l1id]["mercx"], nodes[l1id]["mercy"])
	on_left_of_road = is_left((m0x, m0y), (m1x, m1y), (stopmx, stopmy))

	# True if the buses travel along the direction of the way, False if the buses travel against the direction of the way
	stop_direction = on_left_of_road == drive_on_left
	
	stop.update({
		"wayid": best_line[2],
		"nodeid0": best_line[0],
		"nodeid1": best_line[1], # always in the direction of the line/way.
		"stoppos":{
			"lat": best_stop_lat,
			"lon": best_stop_lon
		},
		"dir":stop_direction,
		"pos-on-line": best_stop_position[2]
	})

	ways[wayid]["stops"].append(stopid)


# # test that the stop positions are correct:
# test_nodes = []
# println = ""
# for stopid, stop in stops.items():
# 	println += f"({str(stop['stoppos']['lat'])}, {str(stop['stoppos']['lon'])})\n"
# print(println)

		
# create a new data structure: for each node have the ways attached to it.
node_connections = dict() # nodeid -> list(wayid)
for wayid, way in ways.items():
	for nid in way["nodes"]:
		if nid in nodes:
			if nid in node_connections:
				node_connections[nid].append(wayid)
			else:
				node_connections[nid] = [wayid]

# all restriction relations a node/way is part of.
node_restrictions = dict()  # nodeid +-> list(relationid)
way_restrictions = dict()
for rid, restriction in restrictions.items():
	for member in restriction["members"]:
		if member["type"] == "node":
			nid = member["ref"]
			if nid in node_restrictions:
				node_restrictions[nid].append(rid)
			else:
				node_restrictions[nid] = [rid]
		elif member["type"] == "way":
			wid = member["ref"]
			if wid in way_restrictions:
				way_restrictions[wid].append(rid)
			else:
				way_restrictions[wid] = [rid]



# variables for the `has_access` function.
allowed_access_tags = ("yes", "permissive", "permit",
                       "destination", "designated", "variable", "unknown")
# @.* is to match (ignore) osm conditional expressions.
# we can have stuff like access:bus:lanes=no|no|yes
# this regex just checks that one of the lanes is open to buses.
# TODO - lane restrictions are not considered in conjunction with turn restrictions.
allowed_access_tags_pattern = f"^([^\|]*\|)*({'|'.join(allowed_access_tags)})(\|[^\|]*)*( @.*)?$"


def has_access(tags, dir=None) -> bool:
	"""Check access tags of element. Returns True if a bus can pass this node."""
	# TODO again, ignoring conditionals.
	# highest priority patterns first

	# check for service tag
	if "highway" in tags and tags["highway"] == "service":
		if "service" in tags and tags["service"] in ("parking_aisle", "driveway", "alley", "emergency_access", "drive-through"):
			return False


	# check for access tag
	if dir is None: # NODE
		tagname_patterns = [
			"^(access:)?psv:bus(:conditional)?$",
			"^(access:)?bus(:conditional)?$",
			"^(access:)?psv(:conditional)?$",
			"^(access:)?vehicle(:conditional)?$",
			"^access(:conditional)?$"
		]
	else: # WAY
		dir_string = "forward" if dir else "backward"
		tagname_patterns = [
			f"^(access:)?psv:bus(:lanes)?:{dir_string}(:conditional)?$",
			f"^(access:)?psv:bus(:lanes)?(:conditional)?$",
			f"^(access:)?bus(:lanes)?:{dir_string}(:conditional)?$",
			f"^(access:)?bus(:lanes)?(:conditional)?$",
			f"^(access:)?psv(:lanes)?:{dir_string}(:conditional)?$",
			f"^(access:)?psv(:lanes)?(:conditional)?$",
			f"^(access:)?vehicle(:lanes)?:{dir_string}(:conditional)?$",
			f"^(access:)?vehicle(:lanes)?(:conditional)?$",
			f"^access(:lanes)?:{dir_string}(:conditional)?$",
			f"^access(:lanes)?(:conditional)?$"
		]
	for pattern in tagname_patterns:

		for name, value in tags.items():
			if search(pattern, name) is not None:
				return search(allowed_access_tags_pattern, value) is not None
	return True


def check_node(nodeid) -> bool:
	"""Check a node is passable by a bus"""

	allowed_barriers = ("border_control", "bump_gate", "bus_trap", "cattle_grid", "coupure", "entrance", "gate",
	                    "hampshire_gate", "lift_gate", "sally_port", "sliding_beam", "sliding_gate", "spikes", "sump_buster", "toll_booth")
	node = nodes[nodeid]
	if "tags" in node and "barrier" in node["tags"]:

		if node["tags"]["barrier"] not in allowed_barriers:
			return False

		# check for the access tag on this node
		if not has_access(node["tags"]):
			return False

	return True


# check the oneway tag to see if buses can pass.
def check_oneway(wayid:int, dir:bool) -> bool:
	"""Check the oneway tags to see if a bus can pass in direction `direction` along the way with `wayid`.
	This function does not consider the `:direction` subkey - that is handled in `has_access`."""
	# TODO once again we are ignoring conditionals.

	way = ways[wayid]
	if "tags" not in way: return True

	# matching one of these verifies access.
	oneway_forwards_tags = ("yes", "true", "1", "no", "false", "0", "reversible", "alternating")
	oneway_backwards_tags = ("-1", "reverse", "no", "false", "0", "reversible", "alternating")

	oneway_tags = oneway_forwards_tags if dir else oneway_backwards_tags
	oneway_tags_pattern = f"^{'|'.join(oneway_tags)}( @.*)?$"

	# again, this list is in descending priority
	tagname_patterns = [
		"^oneway:psv:bus(:conditional)?$",
		"^oneway:bus(:conditional)?$",
		"^oneway:psv(:conditional)?$",
		"^oneway(:conditional)?$",
	]

	for pattern in tagname_patterns:
		for name, value in way["tags"].items():
			if search(pattern, name) is not None:
				return search(oneway_tags_pattern, value) is not None
	
	# some tags imply oneway by definition:
	implied_oneway = {
		"junction": "roundabout",
		"highway": "motorway"}
	if not set(implied_oneway.items()).isdisjoint(way["tags"].items()):
		# implied oneway
		return dir

	return True


def check_restriction(from_wayid: int, via_nodeid: int, to_wayid: int) -> bool:
	"""Given the restriction relations on OSM, is is possible to travel on this path?"""

	# TODO TODO TODO this function only considers prohibitory restrictions, not mandatory restritions!

	prohibitory_restrictions = ("no_right_turn" , "no_left_turn" , "no_u_turn" , "no_straight_on")

	def restriction_matches(restriction):

		# osm restrictions have the roles "from", "via", and "to".
		# https://wiki.openstreetmap.org/wiki/Relation:restriction
		# extract this data.
		fr = None
		via_type = 0  # 0->no via, 1->node, 2->ways
		vi_n = None # via node
		vi_ws = [] # via ways
		to = None

		for member in restriction["members"]:
			if member["role"] == "from":
				fr = member["ref"]
			elif member["role"] == "via":
				if member["type"] == "node":
					vi_n = member["ref"]
					via_type = 1
				elif member["type"] == "way":
					vi_ws.append(member["ref"])
					via_type = 2
			elif member["role"] == "to":
				to = member["ref"]

		# there are many cases here.
		# pseudocode:
		"""
		"from_wayid" matches FROM
			VIA is a node
				VIA matches "via_nodeid"
					TO matches "to_wayid"	-> TRUE
					else 					-> FALSE
			VIA is a list of ways
				the first VIA way matches "to_wayid"	-> TRUE
				else									-> FALSE
			VIA is missing
				TO matches "to_wayid"	-> TRUE
				else 					-> FALSE
		VIA is a list of ways
			"from_wayid" is in this list, but not the last member
				the next member VIA way is "to_wayid"	-> TRUE
				else									-> FALSE
			"from_wayid" is the last member of this list
				TO matches "to_wayid"	-> TRUE
				else					-> FALSE
			else -> FALSE
		else -> FALSE
		"""

		if from_wayid == fr:
			if via_type == 1: # node
				return vi_n == via_nodeid and to == to_wayid
			elif via_type == 2: # list of ways
				return vi_ws[0] == to_wayid
			elif via_type == 0: # no via specified
				return to == to_wayid
			raise RuntimeError # this literally cannot happen
		elif via_type == 2:
			try:
				FROM_index_in_vias = vi_ws.index(from_wayid)
			except ValueError:
				return False
			else:
				if FROM_index_in_vias == len(vi_ws) - 1:
					return to == to_wayid
				else:
					return vi_ws[FROM_index_in_vias + 1] == to_wayid
		else:
			return False

	tagname_pattern = "^restriction(:psv)?(:bus)?(:conditional)?$"
	prohibitory_restrictions_pattern = f"^{'|'.join(prohibitory_restrictions)}( @.*)?$"

	# loop through restrictions involving the 2 ways. use set union to remove duplicates
	restrictions_to_loop = set()
	if from_wayid in way_restrictions:
		restrictions_to_loop.union(way_restrictions[from_wayid])
	if to_wayid in way_restrictions:
		restrictions_to_loop.union(way_restrictions[to_wayid])
	for restriction in restrictions_to_loop:
		
		if "tags" in restriction:
			if "except" in restriction["tags"]:
				# check that neither bus nor psv is in the "except" tag
				# if "psv" in ... OR "bus" in ...
				if {"psv", "bus"}.intersection(restriction["tags"]["except"].split(";")) != set():
					continue
			for name, value in restriction["tags"].items():
				if restriction_matches(restriction) and \
					search(tagname_pattern, name) is not None and \
					search(prohibitory_restrictions_pattern, value) is not None:

					return False
	
	return True


	



def check_maneuver(from_wayid: int, via_nodeid:int, to_wayid:int, from_dir:bool, to_dir:bool) -> bool:
	"""Is it possible for a bus to travel along this path?

	Args:
		from_wayid (int): 
		via_nodeid (int): 
		to_wayid (int): 
		from_dir (bool): direction along from_wayid we are travelling
		to_dir (bool): direction along to_wayid we intend to travel

	Returns:
		bool: Whether the maneuver is valid (there are no OSM restrictions that disallow this)
	"""

	from_way = ways[from_wayid]
	via_node = nodes[via_nodeid]
	to_way = ways[to_wayid]

	# 0. check that we are not at the end of the way
	# TODO this does not accound for circular roads, e.g. roundabouts
	if via_nodeid == to_way["nodes"][-1 if to_dir else 0]:
		return False

	# 1. check that buses have access to "to_wayid"
	# (not considering oneway/restrictions in this step)
	
	if "tags" in to_way and not has_access(to_way["tags"], to_dir):
		return False

	# 2. Check that via_nodeid is not a barrier of some sort
	# some of the allowed barriers are used in conjucntion with access=*, so check for that as well
	if not check_node(via_nodeid):
		return False

	# 3. check that, if the road is oneway, we are travelling in the correct direction
	if not check_oneway(to_wayid, to_dir):
		return False

	# 4. check for turn restrictions
	if not check_restriction(from_wayid, via_nodeid, to_wayid):
		return False

	return True



# during the search we need to check if the current line contains a bus stop.
# index the stops by the lines they are on.
# line -> list of stopid, ordered by t
stops_on_line = dict()
for stopid, stop in stops.items():
	line = (stop["nodeid0"], stop["nodeid1"])
	if line in stops_on_line:
		# insert into the correct position on the line
		def _a():
			for i, _stopid in enumerate(stops_on_line[line]):
				if stops[_stopid]["pos-on-line"] < stop["pos-on-line"]:
					stops_on_line[line].insert(i, stopid)
					return
			stops_on_line[line].append(stopid)
		_a()
	else:
		stops_on_line[line] = [stopid]





# get a list of tuples containing the distance and list of nodes between stops (including start and end nodes)
# e.g.
# output[0] = (156, stopid0, [nid0_0, nid0_1, ...], stopid1)
# output[1] = etc.
# NOTE, nid0_0 etc are references to openstreetmap nodes.
# NOTE for the purpose of plotting on the map, we use "points" - need to convert to points later. Also, we must add the stopping points!
def paths_from_stop(stopid: int, maxdist: Number=max_search_distance) -> 'List[tuple[Number, int, List[int], int]]':
	"""Returns all connections from this stop within max_search distance. Within this function we only check for other stops on the same link as stopid, before passing over to paths_from_node to complete the search.

	Args:
		stopid (int): Id of starting stop
		maxdist (Number, optional): Max distance to search, in meters. Defaults to max_search_distance.

	Returns:
		List[tuple[Number, int, List[int], int]]: List of (distance, stopid, path, stopid0), where
			distance (Number): the real-world distance between the stoppos of stopid and stopid0 in meters, travelling along the path.
			stopid (int): same as in the input
			path (List[int]): path between stopid and stopid 0
			stopid0 (int): the found bus stop.
	"""

	stop = stops[stopid]
	# find the way that contains the stop
	wayid = stop["wayid"]
	way = ways[wayid]
	direction = stop["dir"]

	# stop.update({
	# 	"wayid": best_line[2],
	# 	"nodeid0": best_line[0],
	# 	"nodeid1": best_line[1], # always in the direction of the line/way.
	# 	"stoppos":{
	# 		"lat": best_stop_lat,
	# 		"lon": best_stop_lon
	# 	},
	# 	"dir":stop_direction
	# })


	# start searching at the node on the link of the bus stop we are facing
	#
	#	o---------(STOP)->>----o
	#	^ prev_node   

	path = []
	path_distance = 0

	prev_node_id, next_node_id = (stop["nodeid0"], stop["nodeid1"])[::1 if direction else -1]

	current_pos = [stop["stoppos"]["lat"], stop["stoppos"]["lon"]]


	# edge case - check if there is another proceeding stop in the same line as this.
	line = (stop["nodeid0"], stop["nodeid1"])
	sol = stops_on_line[line]
	if line in sol:
		it = iter(sol[::1 if direction else -1])
		while next(it) != stopid: pass
		for next_stop_id in it:
			next_stop = stops[next_stop_id]
			if next_stop["dir"] == direction:
				return [(surface_distance(*current_pos, next_stop["stoppos"]["lat"], next_stop["stoppos"]["lon"]), stopid, [], next_stop["stopid"])]


	path_distance += surface_distance(*current_pos, nodes[next_node_id]["lat"], nodes[next_node_id]["lon"])
	return paths_from_node(next_node_id, wayid, path_distance, stopid, [next_node_id], direction, maxdist)



# when travelling along the way 'wayid' in direction 'direction' 
def connections_from_node(nodeid:int, wayid:int, direction:bool) -> 'List[tuple[int, bool]]':
	"""Find outgoing connections from nodeid

	Args:
		nodeid (int)
		wayid (int): id of the way along which we are traveling
		direction (bool): direction we are travelling along the way (True=forwads, False=backwards)

	Returns:
		List[tuple[int, bool]]: list of (wayid, direction) pairs
	"""

	connections = []

	for onto_wayid in node_connections[nodeid]:
		for onto_direction in (True, False):
			if onto_wayid == wayid and onto_direction != direction:
				# NOTE - not considering possibility of making U-turns
				continue
			
			if check_maneuver(wayid, nodeid, onto_wayid, direction, onto_direction):
				connections.append((onto_wayid, onto_direction))
	
	return connections





def paths_from_node(nodeid: int, wayid: int, path_distance: Number, stopid: int, path: List[int], direction: bool, maxdist: Number) -> 'List[tuple[Number, int, List[int], int]]':
	"""
	Return all the connection starting from "nodeid": way["wayid"], heading in "direction" along that way.
	The behaviour of this function is to travel along the current way until a junction is reached, and then recur.

	Args:
		nodeid (int): current position (which must be non-barrier)
		wayid (int): the way we are travelling along
		path_distance (Number): real-world distance of the path
		stopid (int): the bus stop from which we started the search
		path (List[int]): path of node ids from the bus stop up to and including nodeid.
		direction (bool): direction along wayid which we are travelling
		maxdist (Number): maximum distance allowed from the original stop.

	Returns:
		List[tuple[Number, int, List[int], int]]: List of (distance, stopid, path, stopid0), where
			distance (Number): the real-world distance between the stoppos of stopid and stopid0 in meters, travelling along the path.
			stopid (int): same as in the input
			path (List[int]): path between stopid and stopid 0
			stopid0 (int): the found bus stop.
	"""

	# TODO at some point in this function we also need to look for barriers

	# start traversing along this way in the correct direction to find the prev_node
	# way_nodes_iter = iter(way["nodes"]) if direction else iter(way["nodes"][::-1])
	# while next(way_nodes_iter) != nodeid: pass

	way = ways[wayid]

	path = path[:]
	current_pos = [nodes[nodeid]["lat"], nodes[nodeid]["lon"]]

	iter_nodes = way["nodes"] if direction else way["nodes"][::-1]
	start_index = iter_nodes.index(nodeid)
	for this_node_id, next_node_id in zip(iter_nodes[start_index:], iter_nodes[start_index+1:]):
		
		# structure of this loop:
		# 1. Check for stops on this link.
		# 2. "add" the link, updating vars accordingly (current_pos, path_distance, path)
		# 3. check the next node, and branch if necessary.

		# at the start of every iteration:
		# +	this_node_id as the last element in the path
		# + path distance represents the distance up to this_node_id


		# if encountered another stop, return result
		line = (this_node_id, next_node_id)[::1 if direction else -1]
		if line in stops_on_line:
			for next_stop_id in stops_on_line[line][::1 if direction else -1]:
				next_stop = stops[next_stop_id]
				# check if this stop is on the correct side of the road
				if next_stop["dir"] != direction:
					continue

				# terminate the search
				if next_stop_id == stopid:
					# ignore self-loops
					return []
				# check the stop is on the right side of the road
				else:
					path_distance += surface_distance(*current_pos,
													next_stop["stoppos"]["lat"], next_stop["stoppos"]["lon"])
					if path_distance < max_search_distance:
						return [(path_distance, stopid, path, next_stop_id)]
					else:
						return []

		# if re-using the same link (in same direction), cancel search
		# TODO there might be some edge cases where this causes breakage (perhaps managed lanes requiring multiple traversal of the same way), but they seem very rare
		if (this_node_id, next_node_id) in zip(path[:-1], path[1:]):
			return []

		# add the new link, and update other variables accordingly
		new_node_pos = [nodes[next_node_id]["lat"], nodes[next_node_id]["lon"]]
		path_distance += surface_distance(*current_pos, *new_node_pos)
		current_pos = new_node_pos
		path.append(next_node_id)

		# if exceeding predetermined maximum distance, cancel search
		if path_distance > max_search_distance:
			return []

		# encoutered a barrier. cancel search
		if not check_node(next_node_id):
			return []

		# if there are multiple ways connected to the current node, recurr on those ways
		if len(node_connections[next_node_id]) > 1:
			output = []
			for onto_wayid, onto_direction in connections_from_node(next_node_id, wayid, direction):
				branch_paths = paths_from_node(next_node_id, onto_wayid, path_distance, stopid, path, onto_direction, maxdist)
				output.extend(branch_paths)
			return output


	# if we get to here then we have reached the end of the way without encountering any branches
	# therefore this street was a dead-end. cancel search
	return []




# test_stopid = 370817929  # this is the stop I analyzed in the presentation, near Cannon Park
# print(test_stopid)
# print(paths_from_stop(test_stopid))

# while True:
# 	test_stopid = int(input("enter stop: "))
# 	print(test_stopid)
# 	print(paths_from_stop(test_stopid))

# exit(0)



# find the connections from every stop, and store the shortest one.
# TODO: we might want to store other routes found in the future, or maybe do something such as test resilience of the routes found

def paths_from_stop_wrapper(arg) -> 'List[tuple[Number, int, List[int], int]]':
	"""Wrapper for paths_from_stop which filters the results, keeping only the shortest path to each stop.

	Args:
		from_stopid (int): stop id at which to begin the search
		i (int): for progress monitoring

	Returns:
		see `paths_from_stop`
	"""


	if type(arg) is tuple:
		i, from_stopid = arg
		if args.verbose and i % 100 == 0: print(f"{i}: processing stopid {from_stopid}")
	else:
		from_stopid = arg
	
	shortest_paths_to_stops = dict()

	for pfs in paths_from_stop(from_stopid):

		distance, _, _, to_stopid = pfs

		if to_stopid not in shortest_paths_to_stops \
		or distance < shortest_paths_to_stops[to_stopid][0]:
			shortest_paths_to_stops[to_stopid] = pfs

	# print(f"\t done processing stopid {from_stopid}")

	return list(shortest_paths_to_stops.values())


shortest_pfs = []
# run, or used cached copy.
# if isfile("shortest_paths.txt"):
# 	print("using previously generated file shortest_paths.txt")
# 	with open("shortest_paths.txt", "r") as f:
# 		shortest_pfs = eval(f.read()) # TODO unsafe
# else:
# 	for result in Parallel(n_jobs=-1)(delayed(paths_from_stop_wrapper)(stopid, i) for i, stopid in enumerate(stops)):
# 		shortest_pfs.extend(result)
# 	with open("shortest_paths.txt", "w") as f:
# 		f.write(str(shortest_pfs))

# for i, stopid in enumerate(stops):
# 	shortest_pfs.extend(paths_from_stop_wrapper((i, stopid)))

# multiprocessing ver.
# create a process pool that uses all cpus
with multiprocessing.Pool() as pool:
	# call the function for each item in parallel
	for result in pool.map(paths_from_stop_wrapper, enumerate(stops), chunksize=1):
		shortest_pfs.extend(result)





# extend the edges - i.e. add extra edges that jump over existing edges (provided the combined lengths is less than the allowed total distance)

# stopid -> [(distance, from_stopid, path, to_stopid), ...]
stop_pfs = {stopid: [] for stopid in stops}
for pfs in shortest_pfs:
	stop_pfs[pfs[1]].append(pfs)


# search all paths originating from this stop
def extended_edges_from_stop(from_stopid, remaining_distance):
	for distance, _, path, to_stopid in stop_pfs[from_stopid]:
		if remaining_distance - distance > 0:
			yield (distance, from_stopid, path, to_stopid)
			for dist_ext, _, path_ext, to_stopid_ext in extended_edges_from_stop(to_stopid, remaining_distance - distance):
				yield (distance + dist_ext, from_stopid, path + path_ext, to_stopid_ext)
	yield from []


# we will recreate stop_pfs here with extended edges
extended_stop_pfs = {stopid: [] for stopid in stops}

# do dfs starting from each stop
for from_stopid in stops:
	for pfs_ext in extended_edges_from_stop(from_stopid, max_search_distance):
		distance_ext, _, _, to_stopid_ext = pfs_ext # unpack each result.

		# search for an existing edge to see if this is shorter.
		existing_edge = False
		for i, pfs in enumerate(extended_stop_pfs[from_stopid]):
			distance, _, _, to_stopid = pfs  # unpack
			if to_stopid == to_stopid_ext:
				if distance_ext < distance:
					extended_stop_pfs[from_stopid][i] = pfs_ext
				existing_edge = True
				break
		if not existing_edge:
			extended_stop_pfs[from_stopid].append(pfs_ext)

# recombine
shortest_pfs = sum(extended_stop_pfs.values(), [])

with open("shortest_paths_extended.txt", "w") as f:
	f.write(str(shortest_pfs))
		



_id = 0
def next_id():
	global _id
	_id += 1
	return _id


points = []

# create extra points for the stopping positions.
# these points are the negative of the stopid.
for stopid, stop in stops.items():

	points.append({
		"id":-stopid,
		"lat":stop["stoppos"]["lat"],
		"lon":stop["stoppos"]["lon"]
	})


links = []
used_nodes = set()
for distance, from_stopid, path, to_stopid in shortest_pfs:

	used_nodes = used_nodes.union(path)

	# now in the real of pointids rather than nodeids.
	# +ve ids: osm nodes
	# -ve ids: calculated STOPPING POSITION of bus stop. (id is the negative of the stop's osm node id)
	path_with_endpoints = [-from_stopid] + path + [-to_stopid]

	links.append({
		"id": next_id(),
		"name": f'{stops[from_stopid]["name"]} => {stops[to_stopid]["name"]}',
		"length": distance/1000, # converting to km.
		"speed": {"0:00": 30}, # TODO
		"startid": from_stopid,
		"endid": to_stopid,
		"points": path_with_endpoints
	})



# add the other nodes to points (nodes on ways, direct from osm)
for nodeid in used_nodes:
	points.append({
		"id":nodeid,
		"lat":nodes[nodeid]["lat"],
		"lon":nodes[nodeid]["lon"]
	})

# export data
exported_json = json.dumps({
	"links":links,
	"points":points
})


args.output.write(exported_json)
# with open("stop-connections.json", "w") as f:
# 	f.write(exported_json)
	

