
# get paths of dependencies from conan
ifneq ("$(wildcard conanbuildinfo.mak)","")
    include conanbuildinfo.mak
    INCLUDE_DIRS_NLOHMANN_JSON ?= $(CONAN_INCLUDE_DIRS_NLOHMANN_JSON)
    INCLUDE_DIRS_ARGPARSE ?= $(CONAN_INCLUDE_DIRS_ARGPARSE)
else
    $(info conanbuildinfo.mak not found. Looking in environment variables for dependencies.)
endif

# check dependency variables are defined
ifndef INCLUDE_DIRS_NLOHMANN_JSON
    $(error INCLUDE_DIRS_NLOHMANN_JSON not set)
endif
ifndef INCLUDE_DIRS_ARGPARSE
    $(error INCLUDE_DIRS_ARGPARSE not set)
endif


INCLUDE_DIRS=$(INCLUDE_DIRS_NLOHMANN_JSON) $(INCLUDE_DIRS_ARGPARSE)
LIB_DIRS=
LIB_FLAGS=

COMPILER=g++

INCLUDE_FLAGS=$(addprefix -I,$(INCLUDE_DIRS))
LINKING_FLAGS=$(addprefix -L,$(LIB_DIRS)) $(addprefix -l,$(LIB_FLAGS))
GENERAL_FLAGS=-g -Wall -std=c++17 -DDEBUG=1

CPPS=$(wildcard src/*.cpp)
HPPS=$(wildcard src/*.hpp)
OS=$(CPPS:src/%.cpp=build/%.o)

all: build/genetic_alg

debug:
	@echo CPPS: $(CPPS)
	@echo HPPS: $(HPPS)
	@echo OS: $(OS)

build/genetic_alg: $(OS)
	@mkdir -p $(@D)
	$(COMPILER) $(GENERAL_FLAGS) $^ -o $@ $(LINKING_FLAGS)

build/%.o: src/%.cpp $(HPPS) Makefile
	@mkdir -p $(@D)
	$(COMPILER) -c $(GENERAL_FLAGS) $(INCLUDE_FLAGS) $< -o $@

clean:
	rm -rf build

.PHONY: all clean debug



