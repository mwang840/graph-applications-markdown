import math
import matplotlib.pyplot as plt
import networkx as nx

from math import sqrt
from networkx import Graph
from queue import Queue
from random import randint

GRAPH_SIZE = 30

def generate_graph () -> Graph:

    G = nx.Graph()
    G.add_nodes_from(range(1, GRAPH_SIZE))

    for i in range(1, GRAPH_SIZE):
        edges = { i }
        j = 0
        while j < 5:
            edge = randint(1, GRAPH_SIZE)
            if edge not in edges:
                G.add_edge(i, edge)
                edges.add(edge)
                j += 1

    return G

def perform_BFS (G: Graph) -> Graph:

    start = randint(1, GRAPH_SIZE)

    print(f"Starting node is {start}.")

    visited = { start }     # set of visited
    discovered = { start }  # set of discovered
    queue = Queue()         # queue of discovered to be visited

    print(f"Visited: {visited}")
    print(f"Discovered: {discovered}")

    bfs_G = nx.Graph()
    bfs_G.add_node(start, distance=0, previous=None)

    print(f"Visiting node {start}...")

    for neighbor in G.neighbors(start):
        bfs_G.add_node(neighbor, distance=1, previous=start)
        bfs_G.add_edge(start, neighbor)
        discovered.add(neighbor)
        queue.put(neighbor)
        print(f"{start} had neighbor {neighbor}")

    print(f"Visited: {visited}")
    print(f"Discovered: {discovered}")

    while not queue.empty():

        visited_node = queue.get()
        visited.add(visited_node)
        distances = nx.get_node_attributes(bfs_G, "distance")
        previous_distance = distances[visited_node]

        print(f"Visiting node {visited_node}...")

        for neighbor in G.neighbors(visited_node):
            if neighbor not in discovered:
                bfs_G.add_node(neighbor, distance=previous_distance+1, previous=visited_node)
                bfs_G.add_edge(visited_node, neighbor)
                discovered.add(neighbor)
                queue.put(neighbor)
                print(f"{visited_node} had neighbor {neighbor}")

        print(f"Visited: {visited}")
        print(f"Discovered: {discovered}")

    return bfs_G

if __name__ == "__main__":

    # Drawing initial graph
    G = generate_graph()
    plt.figure(1)
    nx.draw(G, with_labels=True, font_weight="bold")
    plt.savefig("before-bfs.png")

    # Drawing graph with BFS applied
    H = perform_BFS(G)
    plt.figure(2, figsize=(12.8, 9.6)) # Figure has 12.8 inch / 9.6 inch size

    pos = nx.multipartite_layout(H, subset_key="distance") # Tree-like layout

    nx.draw_networkx(H, pos=pos, with_labels=False) # Draw edges/nodes
    
    # distances = nx.get_node_attributes(H, "distance") 
    # previouses = nx.get_node_attributes(H, "previous")
    # labels = {n: f"{n}\n{previouses[n]} | {distances[n]}" for n in G.nodes()}
    labels = {n: f"{n}" for n in G.nodes()}
    nx.draw_networkx_labels(H, pos=pos, labels=labels, font_size=10) # Draw labels

    plt.savefig("after-bfs.png") # save to png