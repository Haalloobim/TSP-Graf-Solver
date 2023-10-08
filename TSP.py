from sys import maxsize 
from itertools import permutations
V = 6
 
def travellingSalesmanProblem(graph, s): 
 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        current_pathweight = 0
 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        min_path = min(min_path, current_pathweight) 
         
    return min_path 
 

if __name__ == "__main__": 

    graph = [[0, 60, 51, 2, 35, 56],
             [60, 0, 13, 61, 68, 70], 
             [51, 13, 0, 51, 68, 78], 
             [2, 61, 51, 0, 36, 57],
             [35, 68, 68, 36, 0, 21],
             [56, 70, 78, 57, 21, 0]] 
    s = 0
    print(travellingSalesmanProblem(graph, s))