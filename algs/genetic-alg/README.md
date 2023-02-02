# Genetic algorithm

## Compiling
The compilation process is set up for Linux systems using the g++ compiler only. You may have to edit the Makefile for other systems.

1. Install Conan package manager if not already installed.\
```pip install conan```

2. Install dependencies.\
```cd [project directory]```\
```conan install .```

3. Build using the Makefile\
```make```

The executable is generated inside the `/build` folder.

For programming in vscode the include directories can be found in `conanbuildinfo.txt`.