import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()

# 25 routers with 5 routers connected to each router

routers = {
    "R1": ["R2", "R3", "R4", "R5", "R6", "R7"],
    "R2": ["R1", "R3", "R4", "R7", "R8", "R9"],
    "R3": ["R1", "R2", "R4", "R10", "R11", "R12"],
    "R4": ["R1", "R2", "R3", "R5", "R13", "R14"],
    "R5": ["R1", "R4", "R6", "R13", "R15", "R16"],
    "R6": ["R1", "R5", "R17", "R18"],
    "R7": ["R8", "R9", "R10", "R11", "R12", "R2", "R1"],
    "R8": ["R7", "R9", "R10", "R19", "R20", "R21"],
    "R9": ["R7", "R8", "R10", "R22", "R23", "R24"],
    "R10": ["R7", "R8", "R9", "R11", "R3"],
    "R11": ["R7", "R10", "R12", "R19", "R3"],
    "R12": ["R7", "R11", "R3"],
    "R13": ["R14", "R15", "R16", "R17", "R18", "R5", "R4"],
    "R14": ["R13", "R15", "R16", "R22", "R23", "R24", "R4"],
    "R15": ["R13", "R14", "R16", "R25", "R5"],
    "R16": ["R13", "R14", "R15", "R17", "R5"],
    "R17": ["R13", "R16", "R18", "R6"],
    "R18": ["R13", "R17", "R6"],
    "R19": ["R20", "R21", "R22", "R23", "R24", "R11", "R8"],
    "R20": ["R19", "R21", "R22", "R25", "R8"],
    "R21": ["R19", "R20", "R22", "R8"],
    "R22": ["R19", "R20", "R21", "R23", "R9", "R14"],
    "R23": ["R19", "R22", "R24", "R25", "R9", "R14"],
    "R24": ["R19", "R23", "R9", "R14"],
    "R25": ["R23", "R7", "R8", "R9", "R15", "R20"],
}


# each router has a connection to 5 other routers with different weights
router_edges = []

for source, destinations in routers.items():
    for destination in destinations:
        weight = random.randint(1, 10)
        edge = (source, destination, weight)
        if (destination, source, weight) not in router_edges:
            router_edges.append(edge)

G.add_nodes_from(routers)
G.add_weighted_edges_from(router_edges)

pos=nx.shell_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
print("Path: ", nx.dijkstra_path(G, "R4", "R25"), "Distance: ", nx.dijkstra_path_length(G, "R4", "R25"))

plt.show()

# plt.savefig("dijkstraGraph.png") - saves the graph as a png 