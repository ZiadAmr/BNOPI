#!/usr/bin/env python3

from os import getenv, system, name

print("Hi there", getenv("DRIVE_ON_LEFT"), getenv("MAX_SEARCH_DISTANCE"), getenv("OUTPUT_FILELOC"), getenv("STOPS_FILELOC"), getenv("ROADS_FILELOC"))

dol_flag = ""
if getenv("DRIVE_ON_LEFT") == "left":
    dol_flag = "--drive-on-left"

if name == "nt": # windows
    system(
        f'py -3 ./algs/stop-connection-graph.py {dol_flag} -d {getenv("MAX_SEARCH_DISTANCE")} -o "{getenv("OUTPUT_FILELOC")}" "{getenv("STOPS_FILELOC")}" "{getenv("ROADS_FILELOC")}"')
else:
    # otherwise assume we can read the shebang
    system(
        './algs/stop-connection-graph.py ' + dol_flag + ' -d '  + getenv("MAX_SEARCH_DISTANCE") + ' -o ' + getenv("OUTPUT_FILELOC") + ' ' + getenv("STOPS_FILELOC") + ' ' + getenv("ROADS_FILELOC"))

