from tools.branch_and_bound import Branch_And_Bound
from tools.twice_around_tree import Twice_Around_Tree
from tools.christofides import Christofides

# http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/

def euclidian_distance(x1, y1, x2, y2):
    xd = x1 - x2
    yd = y1 - y2
    return pow(((xd*xd)+(yd*yd)), 1/2)

def input_reader(_path):
    with open(_path, 'r') as file:
            lines = file.readlines()
            N = int(lines[3].split()[-1])
            vertices = [0 for _ in range(0, N)]
            adj = [[0 for _ in range(0, N)] for _ in range(0, N)]

            for i in range(6, N+6):    
                line_temp = lines[i].split()
                vertices[int(line_temp[0])-1] = tuple((float(line_temp[1]), float(line_temp[2])))

            for i in range(0, N):
                for j in range(i, N):
                    if i == j: adj[i][j] = 0
                    else:
                        adj[i][j] = euclidian_distance(vertices[i][0], vertices[i][1], vertices[j][0], vertices[j][1])
                        adj[j][i] = euclidian_distance(vertices[i][0], vertices[i][1], vertices[j][0], vertices[j][1])
    return adj

adj = input_reader("./instances/d15112/d15112.tsp")


tat = Twice_Around_Tree(adj)
tat.run_tat()

chr = Christofides(len(adj), adj)
chr.run_christofides()

# bnb = Branch_And_Bound(adj)
# bnb.run_bnb()