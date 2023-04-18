# Bus Network Optimization and Planning Interface (BNOPI)

## Overview

**Bus Network Optimization and Planning Interface** (BNOPI) is a software designed to aid visualization and interaction with algorithms for the Urban Transit Routing Problem (UTRP) and related problems. BNOPI makes the assumption that the algorithmic network design process can be represented with a **dependency graph**, an example of which is shown below.


<!-- image of dependency graph, labelled -->
<!-- perhaps with numbers that can be referred to in the following paragraphs -->

The role of BNOPI is to 
+ control execution of the dependency graph
+ visualize the results of intermediate stages on a geographical map embedding
+ allow users to make changes

In the dependency graph, each node represents an **algorithm**. Algorithms are accessed by BNOPI using a metadata file, which contains information about the command-line parameters, input and output file formats, and a shell script to launch the algorithm.

To transfer data between nodes, BNOPI uses [**stage formats**](/bnopi-stage-fmts/README.md). A stage format refers to the structure of some input, output, or intermediary file. The files themselves are referred to as **stage instances**, or instances of the stage format. An example of a stage format is `STOPS`, instances of which contain data about bus stops in a standardized JSON format. Each edge in a project's dependency graph represents the flow of a stage instance from one node to the next.

On a node, a **breakpoint** may be placed. This indicates that the resulting stage instances of that node should be visualized, and the user should be able to edit them before proceeding.

To accomplish this, **display frameworks** and **editing frameworks** can be defined on a stage format. The display framework is a Javascript function that takes an instance of the stage format and returns a list of items for BNOPI to display, such as bus stops or routes. BNOPI allows the user to edit these items in the GUI, and the editing framework makes the reverse conversion of these items back to a stage instance.

## How to install

See [/README.md](/README.md)

## Example Project Walkthrough

BNOPI provides some standard stage formats and algorithm implementations. Open the example project <!-- project name --> in BNOPI and observe the dependency graph.

The dependency graph's execution begins by downloading information about bus stops and roads from OpenStreetMap, then creating a "stop connection graph". This representation of the road network represents a connection between 2 bus stops as a single directed edge, weighted on the road distance between them. We then use a genetic algorithm to generate a fitting route network.

### Preliminary steps

In order to run the dependency graph you will need to compile the genetic algorithm, written in C++. Find the metadata file for the genetic algorithm (located in [/bnopi-algs/](/bnopi-algs/)), referenced within which is the path to the executable which needs to be compiled. Navigate to that folder and follow the compilation instructions in the README.

The other algorithms used in this project are implemented in Python 3, and also referenced from [/bnopi-algs/](/bnopi-algs/). You may need to install some modules for these to work.

### Project directory structure

The main entry point for the project is `info.json`, located in the top level of the project. This contains information information about the project and links to other files and folders. Projects are structured so that all the project data is referenced from the *info.json* file, and there are no other fixed file names. Below shows the contents of the info.json file.

```json
{
	"title": "Test Project",
	"description": "Project used for testing.",
	"dependencyGraph": "test_dependency_graph.dg.json",
	"stageInstances": ["stage_instances/"]
}
```

`dependencyGraph` references a *.dg.json* file containing information about the structure of the nodes in the project. `stageInstances` contains a list of directories within which BNOPI will look for [stage instance metadata (*.stg.json*) files](/bnopi-stage-fmts/README.md), which are used to keep track of generated stage instances. Generally the stage instances are stored in the same folder alongside the *.stg.json* files.

### Dependency Graph

**TODO the coding for this is not finished - this section might be incorrect.** The example project dependency graph references several algorithms by their string **id**s, such as `"GEN_STOP_CONNECTION_GRAPH"`. 

### Algorithms

**TODO Maybe move this section to another file?**

The aforementioned GEN_STOP_CONNECTION_GRAPH algorithm has an algorithm metadata (*.alg.json*) file, which can be found [here](/bnopi-algs/gen-stop-connection-graph.alg.json). Inside the BNOPI interface, clicking on the cog icon in the GEN_STOP_CONNECTION_GRAPH node on the dependency graph allows us to view some of this information in the Properties tab to the right.

Looking at the *alg.json* file directly, it contains a `name` and `description`, as well as information concerning the algorithm's inputs and outputs. An algorithm can have 2 types of input:
+ The **parameters** - These are settings for the algorithm that can be set by the user before the algorithm is run. For GEN_STOP_CONNECTION_GRAPH the parameters are:

```json
"params": [
	{
		"name": "Left-side drive",
		"type": "dropdown",
		"choices":["left", "right"],
		"default": "left",
		"help": "Specifies that road users should on the left. If omitted, it is assumed road users drive on the right.",
		"var": "DRIVE_ON_LEFT"
	},
	{
		"name": "Max search distance",
		"type": "posint",
		"default": 1000,
		"help": "Specifies the maximum distance to search for neighboring stops, in meters. Defaults to 1000.",
		"var": "MAX_SEARCH_DISTANCE"
	}
]
```

In the Properties tab each parameter generates an input for the user of the type `type`. Later, the values that the user inputs are referenced by the name in the `var` property.

+ The **input stage instances**. This is how BNOPI passes data between nodes. Since algorithms require stage instances in specific format, we specify these formats. This affects which algorithms can be chained together. For GEN_STOP_CONNECTION_GRAPH the input stage formats are:

```json
"inputStageFormats":[
	{
		"name": "Stops",
		"help": "The stops between which to make the stop connection graph edges",
		"var": "STOPS_FILELOC",
		"stage-format": "STOPS"
	},
	{
		"name": "Roads",
		"help": "Roads between the stops",
		"var": "ROADS_FILELOC",
		"stage-format": "ROADS"
	}
]
```

When the GEN_STOP_CONNECTION_GRAPH node is about to run, with the absence of a breakpoint on any parent node, BNOPI will automatically select instances of these formats generated by the parents. If, as is the case in the example project, there *is* a breakpoint, then the user will be allowed to edit the instances generated by previous nodes, and manually select which ones to use for the GEN_STOP_CONNECTION_GRAPH node. The file paths of the selected instances are later referenced by the name in the `var` property.

Algorithms only have 1 type of output:
+ The **output stage instances**. In the *alg.json* file, the `outputStageFormats` refer to the formats of these outputs, in the same way as with the input stage intances:

```json
"outputStageFormats":[
	{
		"name": "Stop connection graph",
		"help": "A json file containing the generated stops",
		"var": "OUTPUT_FILELOC",
		"stage-format": "STOP_CONNECTION_GRAPH"
	}
]
```

When the STOP_CONNECTION_GRAPH node runs, BNOPI automatically assgins a new file location for each output stage instance and generates a corresponding stage instance metadata (*.stg.json*) file.

+ The final part of the *.alg.json* file is the **launch script**. This links to a bash and/or powershell script that launches the algorithm. The bash script for GEN_STOP_CONNECTION_GRAPH is as follows:

```bash
#!/bin/bash

if [[ $DRIVE_ON_LEFT == "left" ]]; then
	DOL_FLAG="--drive-on-left"
else
	DOL_FLAG=""
fi

../../algs/stop-connection-graph.py $DOL_FLAG -d $MAX_SEARCH_DISTANCE -o $OUTPUT_FILELOC $STOPS_FILELOC $ROADS_FILELOC
```

The launch script is called with the environment variables `DRIVE_ON_LEFT`, `MAX_SEARCH_DISTANCE`, `STOPS_FILELOC`, `ROADS_FILELOC`, and `OUTPUT_FILELOC` set as required. These variable names are those set from the `var` properties in the *alg.json* file. The launch script then runs the command to launch the algorithm.

### Running the project


After these steps, you should be able to run the project. Click the play button to execute until the first breakpoint. The `import-stops-from-osm` and `import-roads-from-osm` algorithms should run. You will be able to edit the bus stops that were downloaded from OpenSteetMap in the interface. 

The "create bus stop" and "delete bus stop" tools in the left-hand-side toolbar can be used to edit the STOPS stage instance. You can also see a list of the current bus stops in the "Map info" tab on the right-hand-side sidebar under the "List of stops" heading. From there you can click the trash can icon to delete the stop or the crayon icon to edit info such as the stop's name.

**TODO coding not finished**

Clicking the play button again will continue the execution and create the stop connection graph.

<!-- explanation of the stop connection graph display framework (not implemented) -->

Continuing the execution, we generate a route network using a genetic algorithm. 

<!-- interface tutorial on adding and deleting routes -->


## Documentation
Documentation on how to create metadata files can be found below.

+ [Stage format documentation](/bnopi-stage-fmts/README.md)
+ [Algorithm documentation](/bnopi-algs/README.md)




