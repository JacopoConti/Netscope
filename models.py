import networkx as nx

def randomize_graph(G):
    """Create a fully randomized graph preserving number of nodes and edges (N, M)."""
    N = G.number_of_nodes()
    M = G.number_of_edges()
    G_rand = nx.gnm_random_graph(N, M)
    return G_rand


def configuration_model(G):
    """Generate a configuration model preserving degree distribution."""
    degree_sequence = [d for _, d in G.degree()]
    G_conf = nx.configuration_model(degree_sequence)
    G_conf = nx.Graph(G_conf)  # remove multi-edges
    G_conf.remove_edges_from(nx.selfloop_edges(G_conf))
    return G_conf