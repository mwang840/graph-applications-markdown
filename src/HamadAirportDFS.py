import networkx as nx
import matplotlib.pyplot as plt

if __name__ in "__main__":
    print("DFS traversal")
    G = nx.Graph()
    G.add_edge('Cls', 'Main', weight=0)
    G.add_edge('start', 'banana')
    G.add_edge('start', 'cherry')
    G.add_edge('banana', 'split')
    G.add_edge('banana', 'pie')
