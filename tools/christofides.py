import networkx as nx
import time

class Christofides:
    def __init__(self, _n, _adj_matrix) -> None:
        self.N = _n
        self.graph = nx.complete_graph(_n)
        self.adj_matrix = _adj_matrix

        for i, j in self.graph.edges:
            distance = _adj_matrix[i][j]
            self.graph.edges[i,j]['length'] = distance
        
    def run_christofides(self):
        start_time = time.time()
        min_Tree = nx.minimum_spanning_tree(self.graph, weight='length')
        
        odd_vertices = [i for i in min_Tree.nodes if min_Tree.degree(i)%2]

        for i,j in self.graph.edges:
            self.graph.edges[i,j]['neg_length'] = -self.graph.edges[i,j]['length']

        min_matching = nx.max_weight_matching(self.graph.subgraph(odd_vertices), maxcardinality=True, weight='neg_length')
        
        multigraph = nx.MultiGraph()

        multigraph.add_nodes_from(range(self.N))
        multigraph.add_edges_from(min_Tree.edges())
        multigraph.add_edges_from(min_matching)

        start_tour = list(nx.eulerian_circuit(multigraph,source=0))
        
        tour = [0]
        for (i,j) in start_tour:
            if j not in tour:
                tour.append(j)  

        total_weight = 0
        for i in range(len(tour)-2):
            total_weight += self.adj_matrix[int(tour[i])][int(tour[i+1])]

        print(f"Christofides total weight: {total_weight}")
        print(f"Christofides total time: {time.time() - start_time}")