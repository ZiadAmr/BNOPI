#!/usr/bin/env python3

from os import getenv, system, name

if name == "nt":
    system(
        f'py -3 ./algs/import-roads-from-osm.py {getenv("WORK_AREA_RAD")} {getenv("WORK_AREA_LAT")} {getenv("WORK_AREA_LON")} -o "{getenv("OUTPUT_FILELOC")}"')
else:
    # otherwise assume we can read the shebang
    system(
        './algs/import-roads-from-osm.py ' + getenv("WORK_AREA_RAD") + " " + getenv("WORK_AREA_LAT") + " " + getenv("WORK_AREA_LON") + " -o " + getenv("OUTPUT_FILELOC"))

