#!/usr/bin/env python3

from os import getenv, system, name

system(
    f'./algs/genetic-alg/build/genetic_alg -o "{getenv("OUTPUT_FILELOC")}" "{getenv("STOPS_FILELOC")}" "{getenv("STOP_CONNECTION_GRAPH_FILELOC")}" "{getenv("OD_MATRIX_FILELOC")}"')


