import networkx as nx
import matplotlib.pyplot as plt

# Setting up graphs from Doha Airport
G = nx.Graph()
G.add_edge('Cls', 'Terminal')
G.add_edge('Terminal', 'A1')
G.add_edge('Terminal', 'Al-Saffya Lounge')
G.add_edge('Terminal', 'Al Mourjan Business Lounge')
G.add_edge('Al-Saffya Lounge', 'Al Mourjan Business Lounge')

G.add_edge('A1', 'A4')
G.add_edge('A1', 'A2')
G.add_edge('A1', 'A3')
G.add_edge('A2', 'A3')
G.add_edge('A2', 'A4')
G.add_edge('A3', 'A4')
G.add_edge('A3', 'A5')
G.add_edge('A3', 'A6')
G.add_edge('A3', 'A7')
G.add_edge('A3', 'A8')
G.add_edge('A4', 'A5')
G.add_edge('A4', 'A6')
G.add_edge('A5', 'A6')
G.add_edge('A5', 'A7')
G.add_edge('A5', 'A8')
G.add_edge('A6', 'A8')
G.add_edge('A6', 'A7')
G.add_edge('A7', 'A8')
G.add_edge('A7', 'A9')
G.add_edge('A7', 'A10')
G.add_edge('A9', 'A11')
G.add_edge('A9', 'A8')
G.add_edge('A9', 'A10')
G.add_edge('A9', 'A11')
G.add_edge('A10', 'A11')
G.add_edge('A10', 'A8')
G.add_edge('A8', 'A6')
G.add_edge('A6', 'A4')
G.add_edge('A4', 'A2')
G.add_edge('A2', 'Terminal')
G.add_edge('Terminal', 'B2')
G.add_edge('Terminal', 'A2')
G.add_edge('Terminal', 'B1')
nx.draw_spring(G, with_labels=True)
plt.show()
