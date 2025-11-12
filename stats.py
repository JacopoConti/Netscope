import networkx as nx
import pandas as pd

def graph_basic_stats(G):
    """Compute basic network statistics for a given graph G."""
    stats = {}
    stats["Nodes"] = G.number_of_nodes()
    stats["Edges"] = G.number_of_edges()
    stats["Density"] = nx.density(G)

    # Degree-based measures
    if nx.is_directed(G):
        in_degrees = dict(G.in_degree())
        out_degrees = dict(G.out_degree())
        stats["Average in-degree"] = sum(in_degrees.values()) / len(in_degrees)
        stats["Average out-degree"] = sum(out_degrees.values()) / len(out_degrees)
    else:
        degrees = dict(G.degree())
        stats["Average degree"] = sum(degrees.values()) / len(degrees)

    # Components
    if nx.is_directed(G):
        stats["Components (weak)"] = nx.number_weakly_connected_components(G)
        stats["Components (strong)"] = nx.number_strongly_connected_components(G)
        stats["Giant WCC size"] = len(max(nx.weakly_connected_components(G), key=len))
        stats["Giant SCC size"] = len(max(nx.strongly_connected_components(G), key=len))
    else:
        stats["Components"] = nx.number_connected_components(G)
        stats["Giant component size"] = len(max(nx.connected_components(G), key=len))

    # Shortest-path-based measures
    try:
        if nx.is_directed(G):
            G_und = G.to_undirected()
            stats["Avg shortest path length"] = nx.average_shortest_path_length(G_und)
            stats["Radius"] = nx.radius(G_und)
            stats["Diameter"] = nx.diameter(G_und)
        else:
            stats["Avg shortest path length"] = nx.average_shortest_path_length(G)
            stats["Radius"] = nx.radius(G)
            stats["Diameter"] = nx.diameter(G)
    except Exception:
        stats["Avg shortest path length"] = None
        stats["Radius"] = None
        stats["Diameter"] = None

    return pd.DataFrame(stats, index=[0])