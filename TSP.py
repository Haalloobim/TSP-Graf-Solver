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
        path.append(s + 1)
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

# [1, 2, 3, 4, 5, 6, 1] : 237
# [1, 2, 3, 4, 6, 5, 1] : 237
# [1, 2, 3, 5, 4, 6, 1] : 290
# [1, 2, 3, 5, 6, 4, 1] : 221
# [1, 2, 3, 6, 4, 5, 1] : 279
# [1, 2, 3, 6, 5, 4, 1] : 210
# [1, 2, 4, 3, 5, 6, 1] : 317
# [1, 2, 4, 3, 6, 5, 1] : 306
# [1, 2, 4, 5, 3, 6, 1] : 359
# [1, 2, 4, 5, 6, 3, 1] : 307
# [1, 2, 4, 6, 3, 5, 1] : 359
# [1, 2, 4, 6, 5, 3, 1] : 318
# [1, 2, 5, 3, 4, 6, 1] : 360
# [1, 2, 5, 3, 6, 4, 1] : 333
# [1, 2, 5, 4, 3, 6, 1] : 349
# [1, 2, 5, 4, 6, 3, 1] : 350
# [1, 2, 5, 6, 3, 4, 1] : 280
# [1, 2, 5, 6, 4, 3, 1] : 308
# [1, 2, 6, 3, 4, 5, 1] : 330
# [1, 2, 6, 3, 5, 4, 1] : 314
# [1, 2, 6, 4, 3, 5, 1] : 341
# [1, 2, 6, 4, 5, 3, 1] : 342
# [1, 2, 6, 5, 3, 4, 1] : 272
# [1, 2, 6, 5, 4, 3, 1] : 289
# [1, 3, 2, 4, 5, 6, 1] : 238
# [1, 3, 2, 4, 6, 5, 1] : 238
# [1, 3, 2, 5, 4, 6, 1] : 281
# [1, 3, 2, 5, 6, 4, 1] : 212
# [1, 3, 2, 6, 4, 5, 1] : 262
# [1, 3, 2, 6, 5, 4, 1] : 193
# [1, 3, 4, 2, 5, 6, 1] : 308
# [1, 3, 4, 2, 6, 5, 1] : 289
# [1, 3, 4, 5, 2, 6, 1] : 332
# [1, 3, 4, 5, 6, 2, 1] : 289
# [1, 3, 4, 6, 2, 5, 1] : 332
# [1, 3, 4, 6, 5, 2, 1] : 308
# [1, 3, 5, 2, 4, 6, 1] : 361
# [1, 3, 5, 2, 6, 4, 1] : 316
# [1, 3, 5, 4, 2, 6, 1] : 342
# [1, 3, 5, 4, 6, 2, 1] : 342
# [1, 3, 5, 6, 2, 4, 1] : 273
# [1, 3, 5, 6, 4, 2, 1] : 318
# [1, 3, 6, 2, 4, 5, 1] : 331
# [1, 3, 6, 2, 5, 4, 1] : 305
# [1, 3, 6, 4, 2, 5, 1] : 350
# [1, 3, 6, 4, 5, 2, 1] : 350
# [1, 3, 6, 5, 2, 4, 1] : 281
# [1, 3, 6, 5, 4, 2, 1] : 307
# [1, 4, 2, 3, 5, 6, 1] : 221
# [1, 4, 2, 3, 6, 5, 1] : 210
# [1, 4, 2, 5, 3, 6, 1] : 333
# [1, 4, 2, 5, 6, 3, 1] : 281
# [1, 4, 2, 6, 3, 5, 1] : 314
# [1, 4, 2, 6, 5, 3, 1] : 273
# [1, 4, 3, 2, 5, 6, 1] : 211
# [1, 4, 3, 2, 6, 5, 1] : 192
# [1, 4, 3, 5, 2, 6, 1] : 315
# [1, 4, 3, 5, 6, 2, 1] : 272
# [1, 4, 3, 6, 2, 5, 1] : 304
# [1, 4, 3, 6, 5, 2, 1] : 280
# [1, 4, 5, 2, 3, 6, 1] : 253
# [1, 4, 5, 2, 6, 3, 1] : 305
# [1, 4, 5, 3, 2, 6, 1] : 245
# [1, 4, 5, 3, 6, 2, 1] : 314
# [1, 4, 5, 6, 2, 3, 1] : 193
# [1, 4, 5, 6, 3, 2, 1] : 210
# [1, 4, 6, 2, 3, 5, 1] : 245
# [1, 4, 6, 2, 5, 3, 1] : 316
# [1, 4, 6, 3, 2, 5, 1] : 253
# [1, 4, 6, 3, 5, 2, 1] : 333
# [1, 4, 6, 5, 2, 3, 1] : 212
# [1, 4, 6, 5, 3, 2, 1] : 221
# [1, 5, 2, 3, 4, 6, 1] : 280
# [1, 5, 2, 3, 6, 4, 1] : 253
# [1, 5, 2, 4, 3, 6, 1] : 349
# [1, 5, 2, 4, 6, 3, 1] : 350
# [1, 5, 2, 6, 3, 4, 1] : 304
# [1, 5, 2, 6, 4, 3, 1] : 332
# [1, 5, 3, 2, 4, 6, 1] : 290
# [1, 5, 3, 2, 6, 4, 1] : 245
# [1, 5, 3, 4, 2, 6, 1] : 341
# [1, 5, 3, 4, 6, 2, 1] : 341
# [1, 5, 3, 6, 2, 4, 1] : 314
# [1, 5, 3, 6, 4, 2, 1] : 359
# [1, 5, 4, 2, 3, 6, 1] : 279
# [1, 5, 4, 2, 6, 3, 1] : 331
# [1, 5, 4, 3, 2, 6, 1] : 261
# [1, 5, 4, 3, 6, 2, 1] : 330
# [1, 5, 4, 6, 2, 3, 1] : 262
# [1, 5, 4, 6, 3, 2, 1] : 279
# [1, 5, 6, 2, 3, 4, 1] : 192
# [1, 5, 6, 2, 4, 3, 1] : 289
# [1, 5, 6, 3, 2, 4, 1] : 210
# [1, 5, 6, 3, 4, 2, 1] : 306
# [1, 5, 6, 4, 2, 3, 1] : 238
# [1, 5, 6, 4, 3, 2, 1] : 237
# [1, 6, 2, 3, 4, 5, 1] : 261
# [1, 6, 2, 3, 5, 4, 1] : 245
# [1, 6, 2, 4, 3, 5, 1] : 341
# [1, 6, 2, 4, 5, 3, 1] : 342
# [1, 6, 2, 5, 3, 4, 1] : 315
# [1, 6, 2, 5, 4, 3, 1] : 332
# [1, 6, 3, 2, 4, 5, 1] : 279
# [1, 6, 3, 2, 5, 4, 1] : 253
# [1, 6, 3, 4, 2, 5, 1] : 349
# [1, 6, 3, 4, 5, 2, 1] : 349
# [1, 6, 3, 5, 2, 4, 1] : 333
# [1, 6, 3, 5, 4, 2, 1] : 359
# [1, 6, 4, 2, 3, 5, 1] : 290
# [1, 6, 4, 2, 5, 3, 1] : 361
# [1, 6, 4, 3, 2, 5, 1] : 280
# [1, 6, 4, 3, 5, 2, 1] : 360
# [1, 6, 4, 5, 2, 3, 1] : 281
# [1, 6, 4, 5, 3, 2, 1] : 290
# [1, 6, 5, 2, 3, 4, 1] : 211
# [1, 6, 5, 2, 4, 3, 1] : 308
# [1, 6, 5, 3, 2, 4, 1] : 221
# [1, 6, 5, 3, 4, 2, 1] : 317
# [1, 6, 5, 4, 2, 3, 1] : 238
# [1, 6, 5, 4, 3, 2, 1] : 237

# Minimum TSP :
# [1, 4, 3, 2, 6, 5, 1] : 192