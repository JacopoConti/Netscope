import matplotlib.pyplot as plt
import networkx as nx

def plot_randomization(G, G_rand):
    """Plot the original and randomized graphs side by side."""
    pos = nx.spring_layout(G)

    fig, ax = plt.subplots(1, 2, figsize=(8, 4), dpi=200)
    nx.draw(G, pos, node_size=80, node_color="w", edgecolors=".2", with_labels=False, edge_color=".6", ax=ax[0])
    ax[0].set_title("Original Graph")

    nx.draw(G_rand, pos, node_size=80, node_color="w", edgecolors=".2", with_labels=False, edge_color=".6", ax=ax[1])
    ax[1].set_title("Fully Randomized Graph")

    plt.tight_layout()
    plt.show()