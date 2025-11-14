#import libraries
import networkx as nx
import matplotlib.pyplot as plt

#Create relationship graph
DG = nx.DiGraph()
edges = [
    ("Daniel", "Fred",), ("Fred", "Gilbert"), ("Gilbert", "Daniel"), 
    ("Fred", "Daniel"), ("Gilbert", "Fred"), ("Daniel", "Gilbert"), 
    ("Fred", "Pearl"), ("Pearl", "Fred"), ("Emmanuel", "Daniel"), 
    ("Daniel", "Emmanuel"), ("Emmanuel", "Fred"), ("Fred", "Emmanuel"), 
    ("Emmanuel", "Gilbert"), ("Gilbert", "Emmanuel"), ("Emmanuel", "Pearl"), 
    ("Pearl", "Emmanuel"), ("Daniel", "Pearl"), ("Pearl", "Daniel"), 
    ("Gilbert", "Pearl"), ("Pearl", "Gilbert")
]
DG.add_edges_from(edges)

#Number of nodes and edges
print("number of nodes:", DG.number_of_nodes())
print("number of edges:", DG.number_of_edges())

#Degree of Distribution
degree_dict = dict(DG.degree())
for node, degree in degree_dict.items():
    print(f"Node {node} has degree {degree}") 
    
#Isolated nodes
isolated = list(nx.isolates(DG))
if isolated:
    print("\nIsolated nodes:", isolated)
else:
    print("\nNo isolated nodes found.")
    
#Draw graph
plt.figure(figsize = (11, 12))
nx.draw(
    DG,
    with_labels = True,
    node_size = 500,
    node_color = "lightblue",
    font_size = 12,
)
plt.title("Python Project Group Relationships", fontsize=12)
plt.show()
