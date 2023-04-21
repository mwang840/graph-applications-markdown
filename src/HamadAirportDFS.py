import networkx as nx
import matplotlib.pyplot as plt


# DFS traversal
def airportDFS():
    VisitedAirportArea = {node: False for node in G.nodes}
    ListOfGates = [StartLocation]
    GatesTraversed = []
    while ListOfGates:
        current_gates = ListOfGates.pop()
        if not VisitedAirportArea[current_gates]:
            GatesTraversed.append(current_gates)
            VisitedAirportArea[current_gates] = True
        for node in G.neighbors(current_gates):
            if not VisitedAirportArea[node]:
                ListOfGates.append(node)
    print("The gates that you traversed is: ", "->".join(GatesTraversed))


##code refactoring
if __name__ in "__main__":
    Airport_Areas = {
        "S": ["T"],
        "T": ["ASL", "AM", "A1", "A2", "B1", "B2", "C1", "C2"],
        "ASL": ["A1", "C2", "AM", "T"],
        "AM": ["ASL", "B1", "C1", "T"],
        "A1": ["A2", "A3", "A4", "ASL", "T"],
        "A2": ["A1", "A3", "A4", "T"],
        "A3": ["A1", "A2", "A4", "A5", "A6"],
        "A4": ["A2", "A3", "A5", "A6"],
        "A5": ["A3", "A4", "A6", "A7", "A8"],
        "A6": ["A3", "A4", "A5", "A7", "A8", "A9"],
        "A7": ["A5", "A6", "A8", "A9", "A10"],
        "A8": ["A5", "A6", "A7", "A9", "A10"],
        "A9": ["A7", "A8", "A10", "A11"],
        "A10": ["A7", "A8", "A9", "A11"],
        "A11": ["A9", "A10"],
        "B1": ["T", "AM", "B2", "B3", "B4"],
        "B2": ["T", "B1", "B3", "B4"],
        "B3": ["B1", "B2", "B4", "B5", "B6"],
        "B4": ["B1", "B2", "B3", "B5", "B6"],
        "B5": ["B3", "B4", "B6", "B7", "B8"],
        "B6": ["B3", "B4", "B5", "B7", "B8"],
        "B7": ["B5", "B6", "B8", "B9", "B10"],
        "B8": ["B5", "B6", "B7", "B9", "B10"],
        "B9": ["B8", "B7", "B10"],
        "B10": ["B9", "B8", "B7"],
        "C1": ["T", "AM", "C2", "C3", "C4"],
        "C2": ["T", "ALS", "C1", "C3", "C4"],
        "C3": ["C1", "C2", "C4", "C5", "C6"],
        "C4": ["C1", "C2", "C3", "C5", "C6"],
        "C5": ["C3", "C4", "C6", "C7", "C9"],
        "C6": ["C3", "C4", "C5", "C7", "C8"],
        "C7": ["C5", "C6", "C8", "C9", "C10"],
        "C8": ["C5", "C6", "C7", "C9", "C10"],
        "C9": ["C7", "C8", "C10", "C11", "C12"],
        "C10": ["C7", "C8", "C9", "C11", "C12"],
        "C11": ["C9", "C10", "C12", "E1", "E2"],
        "C12": ["C9", "C10", "C11", "D1", "D2"],
        "D1": ["C12", "D2", "D3", "D4"],
        "D2": ["C12", "D1", "D3", "D4", "E2"],
        "D3": ["D1", "D2", "D4"],
        "D4": ["D1", "D2", "D3"],
        "E1": ["C11", "E2", "E3", "E4"],
        "E2": ["D2", "E1", "E3", "E4"],
        "E3": ["E1", "E2", "E4"],
        "E4": ["E1", "E2", "E3"]
    }
    G = nx.Graph(Airport_Areas)
    nx.draw_spring(G, with_labels=True)
    plt.show()
    StartLocation = "S"
    airportDFS()
