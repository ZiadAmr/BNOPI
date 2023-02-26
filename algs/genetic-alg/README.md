# Genetic algorithm

## Compiling

The compilation process is set up for Linux systems using the g++ compiler only. You may have to edit the Makefile for other systems.

1. Install Conan package manager if not already installed.\
```pip install conan==1.59.0```

2. Install dependencies.\
```cd [project directory]```\
```conan install .```

3. Build using the Makefile\
```make```

For programming in vscode the include directories can be found in `conanbuildinfo.txt`.

Alternatively the program can be compiled without the use of conan by setting environment variables `INCLUDE_DIRS_NLOHMANN_JSON` and `INCLUDE_DIRS_ARGPARSE` to appropriate locations before running the makefile.

After buidling, the executable is `genetic_alg`, generated inside the `/build` folder.

