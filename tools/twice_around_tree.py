import time

class Twice_Around_Tree:
    def __init__(self, _adj_matrix) -> None:
        self.N = len(_adj_matrix)
        self.adj_matrix = _adj_matrix
        self.included = [False for _ in range(self.N)]
        self.parents = [None for _ in range(self.N)]
        self.keys = [9999999999999999999 for _ in range (self.N)]
        self.tree = [list() for _ in range(0, self.N)]

    def get_next_vertex(self):
        min = 9999999999999999999

        for i in range(self.N):
            if self.keys[i] < min and not self.included[i]:
                min = self.keys[i]
                next_vertex = i
        return next_vertex

    def get_MST_Prim(self):
        # first vertex is 0
        self.parents[0] = -1
        self.keys[0] = 0

        for _ in range(self.N):
            next_vertex = self.get_next_vertex()
            self.included[next_vertex] = True
            for vertex in range(self.N):
                if self.adj_matrix[next_vertex][vertex] > 0 and not self.included[vertex] and self.keys[vertex] > self.adj_matrix[next_vertex][vertex]:
                    self.keys[vertex] = self.adj_matrix[next_vertex][vertex]
                    self.parents[vertex] = next_vertex

        for i in range(1, self.N):
            self.tree[self.parents[i]].append(i)

        # sorting children nodes by shortest distance
        for i in range(0, self.N):
            if len(self.tree[i]) == 0: continue

            sorted_list = list()
            while len(self.tree[i]) > 0:
                min__weight = self.adj_matrix[i][0]
                min_index = 0
                for j in range(len(self.tree[i])):
                    if self.adj_matrix[i][j] < min__weight:
                        min__weight = self.adj_matrix[i][j]
                        min_index = j
                sorted_list.append(self.tree[i].pop(min_index))
            self.tree[i] = sorted_list
        

    def get_preorder(self, _vertex):
        if len(self.tree[_vertex]) == 0:
            return f"{_vertex},"
        
        temp_path = f"{_vertex},"
        for node in self.tree[_vertex]: 
            temp_path = temp_path + self.get_preorder(node)
        return temp_path
        

    def run_tat(self):
        start_time = time.time()
        # get Prim MST
        self.get_MST_Prim()

        # connect the path end to vertex 0
        path = self.get_preorder(0).split(",")
        path.pop()
        path.append(0)

        total_weight = 0

        for i in range(len(path)-2):
            total_weight += self.adj_matrix[int(path[i])][int(path[i+1])]

        print(f"Twice-Around-Tree total weight: {total_weight}")
        print(f"Twice-Around-Tree total time: {time.time() - start_time}")

