#pragma once

// in the actual paper there are different types of edges

class Link;


enum EdgeKind = {transport, transfer};

// superclass of all edges.
class Edge {
public:
	EdgeKind kind;
	Edge(EdgeKind kind) : kind(kind) {}
}

// transit edges are edges that are part of a bus route
// there may be multiple transit edges on the sampe
class TransportEdge : public Edge
{
public:
	Link* link;
	TransitEdge(Link* link) : Edge(EdgeKind::transport), link(link) {}
}

// nodes that
class TransferEdge : public Edge
{
public:
	float weight;
	TransferEdge(float weight) : Edge(EdgeKind::transfer), weight(weight) {}
}