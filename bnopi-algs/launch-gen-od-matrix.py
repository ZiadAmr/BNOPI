#!/usr/bin/env python3

from os import getenv, system, name

if name == "nt": # windows
    system(
        f'py -3 ./algs/generate-random-od-matrix.py -n {getenv("NUM_USERS")} -o "{getenv("OUTPUT_FILELOC")}" "{getenv("STOPS_FILELOC")}"')
else:
    # otherwise assume we can read the shebang
    system(
        f'./algs/generate-random-od-matrix.py -n {getenv("NUM_USERS")} -o "{getenv("OUTPUT_FILELOC")}" "{getenv("STOPS_FILELOC")}"')

