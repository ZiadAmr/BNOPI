#!/bin/bash

# the input parameters are inside environment variables.
# the locations of the stage instances should be determined and kept track of by the dependency graph code

if [[ $DRIVE_ON_LEFT == "left" ]]; then
	DOL_FLAG="--drive-on-left"
else
	DOL_FLAG=""
fi

../../algs/stop-connection-graph.py $DOL_FLAG -d $MAX_SEARCH_DISTANCE -o $OUTPUT_FILELOC $STOPS_FILELOC $ROADS_FILELOC