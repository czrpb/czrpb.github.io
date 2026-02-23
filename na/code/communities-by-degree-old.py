import sys
import matplotlib.pyplot as plt
import networkx as nx

main = nx.read_gexf(sys.argv[1])

nodes_by_degree_dec = list(reversed(sorted(list((d,n) for n,d in main.degree()))))
print(nodes_by_degree_dec)

#g_copy = nx.Graph(g)

communities = {}

for d, n in nodes_by_degree_dec:
    n_neighbors = [n for d,n in
                    sorted([(nx.degree(main, neighbor), neighbor) for neighbor in nx.neighbors(main, n)])]
    communities[n] = [d, n_neighbors]

print(communities)

1/0
#countdown = 30
# algo: starting w/ nodes with smallest degree, add them to the largest degreed node they connect to
while nodes_by_degree_dec:
    #countdown -= 1
    d, n = nodes_by_degree_dec.pop()
    n_neighbors = communities[n][1]
    print(n, n_neighbors)

    # find neighbor w/ the most neighbors
    while n_neighbors:
        n_neighbor_with_largest_neighbors = n_neighbors.pop()
        print(f"\t{n_neighbor_with_largest_neighbors}")
        if n_neighbor_with_largest_neighbors not in communities:
            continue

        while n_neighbors:
            n_neighbor_possibly_largest = n_neighbors.pop()
            if n_neighbor_possibly_largest not in communities:
                continue

            if (len(communities[n_neighbor_with_largest_neighbors][1]) <
                len(communities[n_neighbor_possibly_largest][1])):
                n_neighbor_with_largest_neighbors = n_neighbor_possibly_largest

    print(n, n_neighbor_with_largest_neighbors)

    # add n as a neighbor to largest
    if (len(communities[n_neighbor_with_largest_neighbors][1]) > len(communities[n][1])):
        communities[n_neighbor_with_largest_neighbors][1].add(n)
        del communities[n]

    #1/countdown
    if len(communities) == int(sys.argv[2]):
        break

print(communities)

# leaders = list(reversed(communities.keys()))
# for l2 in leaders[:-1]:
#     for l1 in leaders[1:]:
#         communities[l2][1] = communities[l2][1] - communities[l1][1]

# print(communities)

k1, k2, *_ = communities.keys()
print(k1)
print(k2)

communities[k2][1] = communities[k2][1] - communities[k1][1]

el = [[k1, _] for _ in communities[k1][1]]
print(el)
el += [[k2, _] for _ in communities[k2][1]]
print(el)

g = nx.Graph(el)

nx.draw_networkx(g)
plt.show()

pos = nx.spring_layout(main)
nx.draw_networkx_nodes(main, pos, nodelist=[k1]+list(communities[k1][1]), node_shape="s", node_color="red")
nx.draw_networkx_nodes(main, pos, label=k2, nodelist=[k2]+list(communities[k2][1]), node_shape="o")
nx.draw_networkx_edges(main, pos)
nx.draw_networkx_labels(main, pos)

plt.show()