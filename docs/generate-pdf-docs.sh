#!/bin/bash
pandoc index.md -V geometry:margin=1in Projects.md Stage-Instances.md Stage-Formats.md Algorithms.md Dependency-Graphs.md -o docs.pdf