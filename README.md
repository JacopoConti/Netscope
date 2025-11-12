# Netscope
Python Packaging for Network Analysis

This package performs some basic analyses in network science using the networkx library.
It computes descriptive statistics of graphs, generating randomized network models, and visualizing structural differences between original and randomized networks. I created this package to make standard exploratory network analysis automatic, easy ,and reproducible.


# Installation

Remember to install: pip install
The package is based on: pip install networkx pandas matplotlib

# Example to use for the package

import networkx as nx
import netscope as ns

## Example graph
G = nx.karate_club_graph()

## Compute basic statistics
stats = ns.graph_basic_stats(G)
print(stats)

## Create a fully randomized version of the graph
G_rand = ns.randomize_graph(G)

## Generate a configuration model that preserves the degree distribution
G_conf = ns.configuration_model(G)




# Description of Functions

The package should work with both directed and undirected graphs.

graph_basic_stats(G): computes and returns a set of network statistics in the form of a pandas DataFrame.
These include the number of nodes and edges, graph density, average degree (or average in/out degree for directed graphs), number of components, the size of the largest connected component, the average shortest path length, as well as the radius and diameter of the graph.

randomize_graph(G) function produces a randomized version of a given graph, maintaining the same number of nodes and edges but reshuffling the connections. The function plots both the original and randomized networks side by side for visual comparison of their structure.
This randomization can be used as a null model to test whether specific patterns in the original graph arise from random chance or are indeed meaningful structural features.

configuration_model(G) function creates a configuration model version of the input graph.
In this null model, the degree of each node is preserved while edges are rewired randomly.
It provides a useful baseline to test hypotheses about whether observed patterns in a network are due purely to its degree distribution or to higher-order structural organization.
