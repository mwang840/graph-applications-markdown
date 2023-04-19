# Transportation Building Exploration

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Maxwell Wang (maxwang@udel.edu)
* Thomas Ashfield (tomash@udel.edu )
* Ethan Orevillo (eorev@udel.edu )
* Nicholas DiGirolamo (nickdigi@udel.edu )


## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```

# Hamad Airport Terminal Traversal

**Doha Airport Terminal Traversal**: 
An airport geek wants to explore the entire airport of Doha. Currently, the airport
has 41 gates with airline lounges. Given the airport map which is listed as an undirected graph, lets make a Depth-First
Search Traversal of the airport to visit every gate or lounge. For example you are allowed
to visit the terminal **after** you clear security (Node **S**).
> **Formal Description**:
>  * Input: An undirected graph of the airport terminal consisting of gates and lounges
>  * Output: A list of all the gates and the lounges visited within the terminal!

**Graph Problem/Algorithm**: [DFS]


**Setup code**:

```python
import networkx as nx
import matplotlib.pyplot as plt
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
StartLocation = "S"
G = nx.Graph(Airport_Areas)
nx.draw_spring(G, with_labels=True)
plt.show()
airportDFS()
```

**Visualization**:

![Image goes here](dfs-visualization.png)

**Solution code:**

```python
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
```

**Output**

```
 S->T->C2->C4->C6->C8->C10->C12->D2->E2->E4->E3->E1->C11->C9->C7->C5->C3->C1->AM->B1->B4->B6->B8->B10->B9->B7->B5->B3->B2->ASL->A1->A4->A6->A9->A11->A10->A8->A7->A5->A3->A2->D4->D3->D1->ALS
```

**Interpretation of Results**:
Based on our results, the airport geek starts
from security and visits the terminal. We then visit Concourse C and visit the even gates
C2, C4, C6, C8, C10. Once we get to concourse D, We visit D2 and then move on to node E2 and visit 
the remaining gates in Concourse E. Then we visit the odd gates in Concourse C,
visit the Al-Mourjain Lounge (node AM) and visit all Concourse B,
The First Class Al-Saffaya Lounge (node ASL), all concourse A, visits the remaining
gates D1, D3 and D4 and ends in style in the Al-Saffya First class lounge

