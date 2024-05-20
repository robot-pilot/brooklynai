import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

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

# pos = nx.spring_layout(G)
# # pos = nx.spectral_layout(G)
# plt.figure(figsize=(10,7))
# nx.draw(G, pos, with_labels=True, node_color="skyblue", \
# 	node_size=2000, edge_color='k', font_size=16, font_weight='bold')
# plt.title("Directed Graph")
# plt.savefig('graph.png')

# Choose a Graphviz layout
pos = graphviz_layout(G, prog='dot')  # Try 'dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo'

# Draw the graph
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=16, font_weight='bold')
plt.title('Graph with Nine Nodes and Three Strongly Connected Components')
plt.savefig('graph.png')
