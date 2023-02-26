# get paths of dependencies from conan
ifneq ("$(wildcard ../conanbuildinfo.mak)","")
    include ../conanbuildinfo.mak
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


# end of stuff copied from main makefile
# ==================






CPPS_TEST=$(wildcard ./*.cpp)
BINS_TEST=$(CPPS_TEST:%.cpp=%.test)
OS_TEST=$(CPPS_TEST:%.cpp=%.test.o)

OS_MAIN_PROG=$(filter-out ../build/genetic-alg.o, $(wildcard ../build/*.o))


# make the tests by replacing the main function with these.

all: $(BINS_TEST)

debug:
	@echo CPPS_TEST: $(CPPS_TEST)
	@echo BINS_TEST: $(BINS_TEST)
	@echo OS_TEST: $(OS_TEST)
	@echo OS_MAIN_PROG: $(OS_MAIN_PROG)

# make a static library - everything except main fn
libgenetic_alg.a: $(OS_MAIN_PROG)
	ar crf $@ $^

%.test.o: %.cpp Makefile
	$(COMPILER) -c $(GENERAL_FLAGS) $(INCLUDE_FLAGS) $< -o $@

%.test: %.test.o libgenetic_alg.a
	$(COMPILER) $< -L. -lgenetic_alg -o $@

clean:
	rm -f $(BINS_TEST) $(OS_TEST) libgenetic_alg.a

.PRECIOUS: $(OS_TEST)

.PHONY: all debug clean







