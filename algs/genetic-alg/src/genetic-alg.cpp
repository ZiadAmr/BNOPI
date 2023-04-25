#include <iostream>
#include <fstream>
#include <string>
#include <argparse/argparse.hpp>
#include "genetic-alg.hpp"

#include "read-in-data.hpp"
#include "graph.hpp"
#include "smo.hpp"
#include "candidate-route-generation.hpp"

using namespace std;

bool verbose;

int main(int argc, char **argv)
{

	argparse::ArgumentParser program("genetic-alg");

	program.add_description("Implementation of a genetic algorithm for the urban transit routing problem.");

	program.add_argument("stops")
		.help("json file containing the stops")
		.required();

	program.add_argument("connection-graph")
		.help("json file containing the stop connection graph")
		.required();
	
	program.add_argument("od-matrix")
		.help("json file containing the origin-destination matrix")
		.required();

	program.add_argument("--verbose")
		.help("increase output verbosity")
		.default_value(false)
		.implicit_value(true);

	program.add_argument("-o", "--output")
		.metavar("OUTFILE")
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

	// check that the input and output files are valid.
	string stops_file_loc = program.get<string>("stops");
	string connection_graph_file_loc = program.get<string>("connection-graph");
	string outfile_file_loc = program.get<string>("output");
	string od_matrix_file_loc = program.get<string>("od-matrix");
	verbose = program.get<bool>("verbose");

#ifdef DEBUG
	std::cout << "stops_file_loc: " << stops_file_loc << std::endl;
	std::cout << "connection_graph_file_loc: " << connection_graph_file_loc << std::endl;
	std::cout << "outfile_file_loc: " << outfile_file_loc << std::endl;
	std::cout << "verbose: " << verbose << std::endl;
#endif

	// create file streams
	std::ifstream stops_fs;
	stops_fs.open(stops_file_loc, fstream::in);
	if (stops_fs.fail())
	{
		std::cerr << "Error opening file for reading: " << stops_file_loc << std::endl;
		exit(errno);
	}

	std::ifstream connection_graph_fs;
	connection_graph_fs.open(connection_graph_file_loc, fstream::in);
	if (connection_graph_fs.fail())
	{
		std::cerr << "Error opening file for reading: " << connection_graph_file_loc << std::endl;
		exit(errno);
	}

	std::ifstream od_matrix_fs;
	od_matrix_fs.open(od_matrix_file_loc, fstream::in);
	if (connection_graph_fs.fail())
	{
		std::cerr << "Error opening file for reading: " << od_matrix_file_loc << std::endl;
		exit(errno);
	}

	std::ofstream outfile_file_fs;
	outfile_file_fs.open(outfile_file_loc);
	if (outfile_file_fs.fail())
	{
		std::cerr << "Error opening file for writing: " << outfile_file_loc << std::endl;
		exit(errno);
	}

	// create graph
	Graph *graph = nullptr;
	if (verbose)
		cout << "Reading in files..." << endl;
	if (create_graph(stops_fs, connection_graph_fs, &graph))
	{
		exit(1);
	}

	// create od matrix
	OD::Matrix od_matrix = read_in_od_matrix(od_matrix_fs, *graph);

#ifdef DEBUG
	int x = 4;
	cout << x << " sample stops:" << endl;
	for (auto stop_pair : graph->stops)
	{
		if (x-- == 0)
			break;
		Stop stop = stop_pair.second;
		cout << "Stop id: " << stop.id << " lat: " << stop.lat << " lon " << stop.lon << " name: " << stop.name << endl;
	}

	// do a walk in the graph to check pointers are correct
	cout << "doing a random walk..." << endl;
	Stop& stop = graph->stops.begin()->second;
	for (int i = 0; i < 5; i++) {
		cout << "Stop id: " << stop.id << " lat: " << stop.lat << " lon " << stop.lon << " name: " << stop.name << endl;

		
		if (stop.out_edges.size() == 0) break;

		// choose the first out_edge
		Link& link = *stop.out_edges[0];
		cout << "Link id: " << link.id << " name: " << link.name << " length: " << link.length << endl;

		stop = *link.end;

	}

#endif

	// call algorithm
	AlgSettings settings;
	settings.max_route_stops = 20;
	settings.min_route_stops = 2;
	settings.num_routes = 6;
	settings.population_size = 5;

	// generate population
	Population initial_population = generatePopulation(settings,*graph);

	// init algorithm
	SMODriver smo_driver(initial_population, od_matrix, graph, settings, /*niter=*/500);

	// main loop
	smo_driver.run();

	// get output
	RouteNet best_routenet = smo_driver.get_best_routenet();
#ifdef DEBUG

	// display one of the routenets
	cout << "Best routenet" << routenet_to_string(best_routenet) << endl;

#endif

	// TODO serialize this and write to outfile_file_fs

	outfile_file_fs << routenet_to_string(best_routenet);

	stops_fs.close();
	connection_graph_fs.close();
	outfile_file_fs.close();
}
