from sys import maxsize
from itertools import permutations
V = 6


def travellingSalesmanProblem(graph, s):

    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    out_path = []
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        path = []
        k = s
        path.append(k + 1)
        for j in i:
            path.append(j + 1)
            current_pathweight += graph[k][j]
            k = j
        path.append(j + 1)
        current_pathweight += graph[k][s]
        print(f"{path} : {current_pathweight}")
        if current_pathweight < min_path:
            out_path = path
        min_path = min(min_path, current_pathweight)
    print(f"\nMinimum TSP : \n{out_path} : {min_path}")


if __name__ == "__main__":

    graph = [
        [0, 60, 51, 2, 35, 56],
        [60, 0, 13, 61, 68, 70],
        [51, 13, 0, 51, 68, 78],
        [2, 61, 51, 0, 36, 57],
        [35, 68, 68, 36, 0, 21],
        [56, 70, 78, 57, 21, 0]
    ]
    s = 0
    travellingSalesmanProblem(graph, s)
