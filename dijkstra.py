import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Define a array of tuples for the graph

nodes = ["1", "2", "3", "4", "5", "6"]
edges = [
            ("1", "2", 3),
            ("1", "3", 1),
            ("2", "4", 2),
            ("2", "5", 6),
            ("3", "4", 1),
            ("3", "5", 4),
            ("5", "6", 5),
            ("4", "6", 2),
        ]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)

plt.show()

# plt.savefig("dijkstraGraph.png") - saves the graph as a png 

def dijkstraPath():
    return []