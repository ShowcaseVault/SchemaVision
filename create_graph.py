import json
import networkx as nx
import matplotlib.pyplot as plt

from config.config import settings

# ---------------------------
# 1. JSON schema
# ---------------------------

file_path = settings.SCHEMA_FILE

with open(file_path,"r") as file:
    db_schema = json.load(file)

# ---------------------------
# 2. Create graph
# ---------------------------
G = nx.DiGraph()

for table_name, columns in db_schema["tables"].items():
    G.add_node(table_name, columns=columns)

for rel in db_schema["relationships"]:
    G.add_edge(rel["from"], rel["to"], via=rel["via"])

# ---------------------------
# 3. Draw
# ---------------------------
plt.figure(figsize=(16, 12))

# Increase spacing with k
pos = nx.spring_layout(G, seed=42, k=2.5, iterations=200)

nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightblue")
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=30)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

edge_labels = nx.get_edge_attributes(G, "via")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

plt.title("Database Tables and Relationships", fontsize=18)
plt.axis("off")
plt.show()
