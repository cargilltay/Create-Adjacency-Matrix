import networkx as nx

def adjacency_matrix(g):

  matrix = []

  #init empty matrix
  for v in g.nodes():
    matrix.append([])
    for consec_v in g.nodes():
      matrix[v - 1].append(0)

  #flip bit to 1for neighbors of each vertex
  for v in g.nodes():    
    for n in g.neighbors(v):
      matrix[v - 1][n - 1] = 1

  return matrix


edges = [(1,2), (1,3), (2,3), (2,4), (3,4)]
G = nx.Graph(edges)
print adjacency_matrix(G)
