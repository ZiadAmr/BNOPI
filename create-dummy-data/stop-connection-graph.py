#!/bin/python3

import math
import json
from math import sqrt, inf
from numbers import Number
from sys import exit

# !!!!!!!! 
drive_on_left = True

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
	if t <= 0: return (p0x, p0y)
	elif t >= 1: return (p1x, p1y)
	else: return (ax+t*bx, ay+t*by)

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

	



with open("stops.json", "r") as f:
	stops = json.loads(f.read())
stop_dict = {stop["id"] : stop for stop in stops["stops"]}
del stops

with open("coventry-routes.json", "r") as f:
	route_data = json.loads(f.read())

with open("coventry-roads.json", "r") as f:
	road_data = json.loads(f.read())

# preprocess the roads.
# create a set of "lines": section of a road that is joined by a straight line
nodes = dict()
ways = dict()
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
		ways[el["id"]] = el
		way_nodes = el["nodes"]
		for n0, n1 in zip(way_nodes[:-1], way_nodes[1:]):
			lines.append((n0, n1, el["id"]))

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
	sx = int((merc_x - min_x)/dx * hor_squares)
	sy = int((merc_y - min_y)/dy * vert_squares)
	return (sx, sy)

def square_to_merc(sx, sy):
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
for id, stop in stop_dict.items():
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

				cx, cy = closest_point_on_line(m0x, m0y, m1x, m1y, stopmx, stopmy)
				dist = sqrt((stopmx-cx)**2 + (stopmy-cy)**2)

				if dist < min_dist_to_road:
					min_dist_to_road = dist
					best_line = line
					best_stop_position = (cx, cy)
	
	# convert back from mercartor
	best_stop_lat, best_stop_lon = amerc(*best_stop_position)

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
		"nodeid1": best_line[1],
		"stoppos":{
			"lat": best_stop_lat,
			"lon": best_stop_lon
		},
		"dir":stop_direction
	})


# test that the stop positions are correct:
test_nodes = []
println = ""
for id, stop in stop_dict.items():
	println += f"({str(stop['stoppos']['lat'])}, {str(stop['stoppos']['lon'])})\n"
print(println)

		



_id = 0
def next_id():
	global _id
	_id += 1
	return _id

links = []

for el in route_data["elements"]:

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



		

