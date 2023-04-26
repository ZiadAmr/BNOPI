
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

To transfer data between nodes, BNOPI uses [**stage formats**](/docs/Stage-Formats.md). A stage format refers to the structure of some input, output, or intermediary file. The files themselves are referred to as **stage instances**, or instances of the stage format. An example of a stage format is `STOPS`, instances of which contain data about bus stops in a standardized JSON format. Each edge in a project's dependency graph represents the flow of a stage instance from one node to the next.

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

`dependencyGraph` references a *.dg.json* file containing information about the structure of the nodes in the project. `stageInstances` contains a list of directories within which BNOPI will look for [stage instance metadata (*.stg.json*) files](/docs/Stage-Formats.md), which are used to keep track of generated stage instances. Generally the stage instances are stored in the same folder alongside the *.stg.json* files.

### Dependency Graph

**TODO the coding for this is not finished - this section might be incorrect.** The example project dependency graph references several algorithms by their string **id**s, such as `"GEN_STOP_CONNECTION_GRAPH"`. 

The GEN_STOP_CONNECTION_GRAPH algorithm has an algorithm metadata (*.alg.json*) file, which can be found [here](/bnopi-algs/gen-stop-connection-graph.alg.json). Inside the BNOPI interface, clicking on the cog icon in the GEN_STOP_CONNECTION_GRAPH node on the dependency graph allows us to view some of this information in the Properties tab to the right. You can edit the values of the paremeters as well as the title and description of the node. Note that this does not change the original *.alg.json* file; the changes occur in the dependency graph file *.dg.json*.

### Running the project


After these steps, you should be able to run the project. Click the play button to execute until the first breakpoint. The `import-stops-from-osm` and `import-roads-from-osm` algorithms should run. You will be able to edit the bus stops that were downloaded from OpenSteetMap in the interface. 

The "create bus stop" and "delete bus stop" tools in the left-hand-side toolbar can be used to edit the STOPS stage instance. You can also see a list of the current bus stops in the "Map info" tab on the right-hand-side sidebar under the "List of stops" heading. From there you can click the trash can icon to delete the stop or the crayon icon to edit info such as the stop's name.

**TODO coding not finished**

Clicking the play button again will continue the execution and create the stop connection graph.

<!-- explanation of the stop connection graph display framework (not implemented) -->

Continuing the execution, we generate a route network using a genetic algorithm. 

<!-- interface tutorial on adding and deleting routes -->


## Documentation
More in-depth documentation on the project structure can be found below.

+ [Projects](Projects.md)
+ [Stage instances](Stage-Instances)
+ [Stage formats](Stage-Formats.md)
+ [Algorithms](Algorithms.md)
+ [Dependency graphs](Dependency-Graphs.md)





