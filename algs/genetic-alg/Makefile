
include conanbuildinfo.mak

COMPILER=g++

INCLUDE_FLAGS=$(addprefix -I,$(CONAN_INCLUDE_DIRS))
LIBRARY_FLAGS=$(addprefix -L,$(CONAN_LIB_DIRS)) $(addprefix -l,$(CONAN_LIBS))
GENERAL_FLAGS=-g -Wall -std=c++17

CPPS=$(wildcard src/*.cpp)
HPPS=$(wildcard src/*.hpp)
OS=$(CPPS:src/%.cpp=build/%.o)

all: build/genetic_alg

debug:
	@echo CPPS: $(CPPS)
	@echo HPPS: $(HPPS)
	@echo OS: $(OS)

build/genetic_alg: $(OS)
	$(COMPILER) $(GENERAL_FLAGS) $^ -o $@ $(LIBRARY_FLAGS)

build/%.o: src/%.cpp $(HPPS) Makefile conanbuildinfo.mak
	$(COMPILER) -c $(GENERAL_FLAGS) $(INCLUDE_FLAGS) $< -o $@


clean:
	rm build/*

.PHONY: all clean debug



