import sys
import random
import matplotlib.pyplot as plt
import networkx as nx

main = nx.read_gexf(sys.argv[1])

nodes = list(nx.nodes(main))

##########################

def get_random_communities():
    ns = list(nodes)
    c1 = ns[:len(ns)//2]
    c2 = ns[len(ns)//2:]
    return c1, c2

communities = get_random_communities()

##########################

# def get_communities():
#     pass

# communities = get_communities()

##############################

pos = nx.spring_layout(main)
for community, shape, color in zip(communities, "so<>", ["red", "green", "blue", "yellow"]):
    nx.draw_networkx_nodes(main, pos, nodelist=community, node_shape=shape, node_color=color)
nx.draw_networkx_edges(main, pos)
nx.draw_networkx_labels(main, pos)

plt.show()