import math
import matplotlib.pyplot as plt
import networkx as nx

from math import sqrt
from networkx import Graph
from queue import Queue
from random import randint

GRAPH_SIZE = 50
EDGES_PER_NODE = 2

def generate_graph () -> Graph:

    city_roads = {
        1: [2, 11, 10],
        2: [22, 23, 13, 1, 3],
        3: [2, 22, 14, 4],
        4: [3, 5, 15],
        5: [4, 6, 17],
        6: [5, 7, 17, 20],
        7: [6, 8, 20],
        8: [7, 20, 21, 9],
        9: [8, 21, 10],
        10: [9, 11, 1],
        11: [10, 1, 18, 12],
        12: [11, 18, 13, 16],
        13: [2, 14, 16, 12],
        14: [3, 13, 15, 16],
        15: [4, 14, 17, 16],
        16: [13, 14, 15, 17, 19, 18, 12],
        17: [15, 20, 16, 19],
        18: [11, 12, 16, 19],
        19: [16, 17, 18, 20],
        20: [6, 17, 19, 7, 8],
        21: [8, 9],
        22: [3, 2, 24, 23],
        23: [2, 22, 24, 25],
        24: [25, 26, 23, 22],
        25: [23, 24, 26],
        26: [24, 25],
    }

    return nx.Graph(city_roads)

def perform_BFS (G: Graph, start: int, end: int) -> Graph:

    visited = { start }     # set of visited
    discovered = { start }  # set of discovered
    queue = Queue()         # queue of discovered to be visited

    bfs_G = nx.Graph()
    bfs_G.add_node(start, distance=0, previous=None)

    for neighbor in G.neighbors(start):
        bfs_G.add_node(neighbor, distance=1, previous=start)
        bfs_G.add_edge(start, neighbor)
        discovered.add(neighbor)
        queue.put(neighbor)

    while not queue.empty():

        visited_node = queue.get()
        visited.add(visited_node)
        distances = nx.get_node_attributes(bfs_G, "distance")
        previous_distance = distances[visited_node]

        for neighbor in G.neighbors(visited_node):
            if neighbor not in discovered:
                bfs_G.add_node(neighbor, distance=previous_distance+1, previous=visited_node)
                bfs_G.add_edge(visited_node, neighbor)
                discovered.add(neighbor)
                queue.put(neighbor)

    previouses = nx.get_node_attributes(bfs_G, "previous")

    print(f"Start is {start}.", end="")
    print(f" End is {end}. Path is", end="")
    while end is not None:
        if end is airport:
            print(f" {end}")
        else:
            print(f" {end} ->", end="")
        end = previouses[end]

    return bfs_G

if __name__ == "__main__":

    airport = 22
    driver_location = 9

    # Drawing initial graph
    G = generate_graph()
    plt.figure(1)
    nx.draw(G, with_labels=True, font_weight="bold")
    plt.savefig("../before-bfs.png")

    # Drawing graph with BFS applied
    H = perform_BFS(G, airport, driver_location)
    plt.figure(2, figsize=(12.8, 9.6)) # Figure has 12.8 inch / 9.6 inch size

    pos = nx.multipartite_layout(H, subset_key="distance") # Tree-like layout

    # nx.draw_networkx(H, pos=pos, with_labels=False) # Draw edges/nodes
    nx.draw_networkx_nodes(H, pos=pos, node_size=1500)
    nx.draw_networkx_edges(H, pos=pos)
    
    distances = nx.get_node_attributes(H, "distance") 
    previouses = nx.get_node_attributes(H, "previous")
    labels = {n: f"{n}\n{previouses[n]} | {distances[n]}" for n in G.nodes()}
    # labels = {n: f"{n}" for n in G.nodes()}
    nx.draw_networkx_labels(H, pos=pos, labels=labels, font_size=12) # Draw labels

    plt.savefig("../after-bfs.png") # save to png