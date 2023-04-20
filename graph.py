import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree

#Create empty graph
G = nx.Graph()

#Add all nodes plus edges
G.add_edge("A1", "A2", weight=4)
G.add_edge("A1", "A4", weight=10)
G.add_edge("A2", "A6", weight=6)
G.add_edge("A2", "A9", weight=1)
G.add_edge("A3", "A5", weight=7)
G.add_edge("A3", "A8", weight=5)
G.add_edge("A4", "A10", weight=4)
G.add_edge("A4", "A14", weight=6)
G.add_edge("A5", "A7", weight=9)
G.add_edge("A5", "A3", weight=8)
G.add_edge("A5", "A12", weight=2)
G.add_edge("A6", "A15", weight=9)
G.add_edge("A6", "A1", weight= 4)
G.add_edge("A7", "A2", weight=3)
G.add_edge("A7", "A14", weight=7)
G.add_edge("A8", "A13", weight=3)
G.add_edge("A8", "A11", weight=2)
G.add_edge("A9", "A2", weight=7)
G.add_edge("A9", "A6", weight=2)
G.add_edge("A10", "A8", weight=9)
G.add_edge("A10", "A12", weight=2)
G.add_edge("A11", "A5", weight=6)
G.add_edge("A11", "A15", weight=5)
G.add_edge("A12", "A4", weight=8)
G.add_edge("A12", "A6", weight=7)
G.add_edge("A13", "A2", weight=7)
G.add_edge("A13", "A4", weight=5)
G.add_edge("A14", "A1", weight=1)
G.add_edge("A14", "A15", weight=6)
G.add_edge("A15", "A9", weight=9)

#Visualizing the graph
plt.figure(1)
position =nx.spring_layout(G, iterations=6000)
nx.draw_networkx(G, position, arrows=False, with_labels=True)

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, position, edge_labels)

ta = plt.gca()
ta.margins(0.05)
plt.axis("off")
plt.tight_layout()
plt.show()

#MST Solution
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
shortestPath = list(mst)
sorted(sorted(i) for i in shortestPath)
print(shortestPath)