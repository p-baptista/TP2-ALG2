import numpy as np
import time

class Branch_And_Bound:
    def __init__(self, _adj_matrix) -> None:
        self.N = len(_adj_matrix)
        self.adj_matrix = _adj_matrix
        self.best_solution = 9999999999999999999
        self.solution_path = [None for _ in range(self.N+1)]

    def get_min_cost(self, _vertex):
        min = 999999999999999
        for i in range(self.N):
            if self.adj_matrix[_vertex][i] < min and _vertex != i:
                min = self.adj_matrix[_vertex][i]
        return min
    
    def get_second_min_cost(self, _vertex):
        first_min, second_min = 999999999999999, 999999999999999
        for i in range(self.N):
            if _vertex == i: continue
            if self.adj_matrix[_vertex][i] < first_min:
                second_min = first_min
                first_min = self.adj_matrix[_vertex][i]
            elif self.adj_matrix[_vertex][i] <= second_min and self.adj_matrix[_vertex][i] != first_min:
                second_min = self.adj_matrix[_vertex][i]
        return second_min
    
    def recursive_bnb(self, _bound, _weight, _level, _path, _visited):
        if _level == self.N:
            if self.adj_matrix[_path[_level-1]][_path[0]] != 0:
                total_weight = _weight + self.adj_matrix[_path[_level-1]][_path[0]]
                if total_weight < self.best_solution:
                    self.solution_path[:(self.N+1)] = _path[:]
                    self.solution_path[self.N] = _path[0]
                    self.best_solution = total_weight
            return

        for vertex in range(self.N):
            if self.adj_matrix[_path[_level-1]][vertex] != 0 and not _visited[vertex]:
                temp_bound = _bound
                _weight += self.adj_matrix[_path[_level-1]][vertex]

                if _level == 1: _bound -= (self.get_min_cost(_path[_level-1]) + self.get_min_cost(vertex))/2
                else: _bound -= (self.get_second_min_cost(_path[_level-1]) + self.get_min_cost(vertex))/2

                if _bound + _weight < self.best_solution:

                    _path[_level] = vertex
                    _visited[vertex] = True

                    self.recursive_bnb(_bound, _weight, _level+1, _path, _visited)
                
                _weight -= self.adj_matrix[_path[_level-1]][vertex]
                _bound = temp_bound

                _visited = [False for _ in range(len(_visited))]
                for i in range(_level):
                    if _path[i] != -1:
                        _visited[_path[i]] = True

    def run_bnb(self):
        start_time = time.time()
        bound = 0
        path = [-1 for _ in range(self.N+1)]
        visited = [False for _ in range(self.N)]

        for vertex in range(self.N):
            bound += self.get_min_cost(vertex) + self.get_second_min_cost(vertex)

        bound = np.ceil(bound/2)

        path[0] = 0
        visited[0] = True

        self.recursive_bnb(bound, 0, 1, path, visited)

        print(f"Branch-and-Bound total weight: {self.best_solution}")
        print(f"Branch-and-Bound total time: {time.time() - start_time}")
