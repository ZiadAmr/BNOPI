

#include <iostream>
#include <argparse/argparse.hpp>
#include "genetic-alg.hpp"

#include "read-in-data.hpp"


int main(int argc, char** argv) {

	argparse::ArgumentParser program("genetic-alg");

	program.add_argument("stops")
		.help("json file containing the stops")
		.required();

	program.add_argument("connection-graph")
		.help("json file containing the stop connection graph")
		.required();

	program.add_argument("--verbose")
		.help("increase output verbosity")
		.default_value(false)
		.implicit_value(true);

	program.add_argument("-o", "--output")
		.default_value(std::string("routes.json"))
		.help("specify the output file.");

	try
	{
		program.parse_args(argc, argv);
	}
	catch (const std::runtime_error &err)
	{
		std::cerr << err.what() << std::endl;
		std::cerr << program;
		std::exit(1);
	}
}