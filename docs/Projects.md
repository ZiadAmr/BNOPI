# Projects

A BNOPI project consists of some metadata in a file named `info.json`, the project [dependency graph](Dependency-Graphs.md), and the [stage instances](Stage-Instances.md) generated by it.

The project directory structure, as is generated when creating a new project in the UI, is the following:

```
	.
	└── my_project/
		├── info.json
		├── dependency_graph.dg.json
		└── stage_instances/
			└── ...
```

The only part of the above that is fixed is `info.json` in the top level of the directory. The paths to the other components of a project are specified within it.

## *info.json* structure
A project's *info.json* file contains information about the project and links to the other project components. It is a JSON Object containing the following properties:

+ `title: String` - Project title. Typically the same or similar to the directory name.
+ `description: String` - Description of the project.
+ `dependencyGraph: String` - Relative or absolute (relative preferred) path to the project's [dependency graph](Dependency-Graphs.md) (*.dg.json*) file.
+ `stageInstances: Array[String]` - Relative or absolute (relative preferred) paths to directories containing [stage instance metadata](Stage-Instances.md) (*.stg.json*) files to be displayed in the project's stage tracker.
