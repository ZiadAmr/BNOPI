#pragma once
#include <string>

class Stop;

class Link {
public:

	int id;
	std::string name;
	float length;
	// speed
	Stop* start;
	Stop* end;

	Link(int id, std::string name, float length, Stop* start, Stop*end): id(id), name(name), length(length), start(start), end(end) {};

};