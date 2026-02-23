import sys
import networkx as nx
import matplotlib.pyplot as plt

def sum_of_weighted_paths_by_node(g, decay=1):
  sums = {}
  nodes = list(g)
  for i in nodes:
    i_sum = 0
    nodes_without_i = nodes.copy()
    nodes_without_i.remove(i)
    for j in nodes_without_i:
      i_sum += decay ** (len(list(nx.shortest_simple_paths(g, i, j))[0])-1)
    sums[i] = i_sum / (decay * (len(nodes)-1))
  return sums

nx.decay_centrality = lambda g, decay=0.5: sum_of_weighted_paths_by_node(g, decay)

title = []
dim = [[3,3]]
centrality_funcs = []
node_annotations = []

def mk_pairs(l):
  #print(l)
  match l:
    case [(_, _), *_]:
      return
    case [centrality, *_] if (centrality.startswith("--")
                              and (centrality.endswith("_centrality")
                                   or centrality.endswith("pagerank")
                                   or centrality.endswith("eccentricity")
                                   or centrality.endswith("clustering")
                                   )):
      title.append(centrality)
      centrality_funcs.append(getattr(nx, centrality[2:]))
      l.pop(0)
      mk_pairs(l)
    case [graph, *_] if (graph.startswith("--")
                         and "_graph" in graph):
      title.append(graph)
      name, *n = graph.split("=")
      g = getattr(nx, name[2:])
      if n:
        n = n[0].split(",")
        if "circulant" in name:
          g = g(int(n[0]), [1, 2])
        else:
          g = g(*map(int, n))
      else:
        g = g()
      l.extend(list(g.edges))
      l.pop(0)
      mk_pairs(l)
    case [d, *_] if d.startswith("--dim"):
      dim.append([float(_) for _ in d.split("=")[1].split(",")])
      l.pop(0)
      mk_pairs(l)
    case [a, *_] if a.startswith("--node_annotations"):
      node_annotations.extend(a.split("=")[1].split(","))
      l.pop(0)
      mk_pairs(l)
    case _:
      l.append((l.pop(0), l.pop(0)))
      mk_pairs(l)

edges = sys.argv[1:]

mk_pairs(edges)
#print(edges)

g = nx.Graph()
g.add_edges_from(edges)
g = nx.relabel_nodes(g, dict([(n, str(n)) for n in g]))

if centrality_funcs:
    for c_f in centrality_funcs:
      centralities = c_f(g)
      g = nx.relabel_nodes(
        g,
        dict([(n, f"{n}\n{centralities[n]:.2f}"
                  if (not node_annotations or n.split()[0] in node_annotations)
                  else n)
               for n in g])
        )

try:
  dia = nx.diameter(g)
except:
  dia = "n/a"
  
try:
  ecc = sum(nx.eccentricity(g).values()) / len(nx.eccentricity(g))
  ecc = f"{ecc:.2}"
except:
  ecc = "n/a"

fig, ax = plt.subplots(figsize=dim[-1])
title.append(f"Den: {nx.density(g):.2}  Ecc: {ecc}  Dia: {dia}")
ax.set_title("\n".join(title))
nx.draw_networkx(g)
plt.show()

nx.write_gexf(g, "net.gexf")