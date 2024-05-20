import networkx as nx
import matplotlib.pyplot as plt

# create directed graph
G = nx.DiGraph()

# First SCC
G.add_edges_from([('1', '2'), ('2', '3'), ('3', '1')])

# Second SCC
G.add_edges_from([('4', '5'), ('5', '6'), ('6', '4')])

# Third SCC
G.add_edges_from([('7', '8'), ('8', '9'), ('9', '7')])

# inter-component edges
G.add_edges_from([('3', '4'), ('6', '7')])

pos = nx.spring_layout(G)
# pos = nx.spectral_layout(G)
plt.figure(figsize=(10,7))
nx.draw(G, pos, with_labels=True, node_color="skyblue", \
	node_size=2000, edge_color='k', font_size=16, font_weight='bold')
plt.title("Directed Graph")
plt.savefig('graph.png')