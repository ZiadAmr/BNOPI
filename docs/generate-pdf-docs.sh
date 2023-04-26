#!/bin/bash
pandoc --pdf-engine=xelatex -V geometry:margin=1in pandoc-header.md index.md Projects.md Stage-Instances.md Stage-Formats.md Algorithms.md Dependency-Graphs.md -o docs.pdf