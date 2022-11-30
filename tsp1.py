from sys import maxsize
from itertools import permutations
from typing import Callable, Any

#  two algorithms are implemented in wich we can work  both of them ,
#  The algorithm  also can work with two types of data dictinary and matrix
V = 4

V = 4
answer = []

def Tsp(algorithm: Callable, data):
    graph=[]
    # parse the data to data that the algorithims can work with
    if type(data)  is dict:
        for key in data.keys():
            ls=[]
            ls.append(key)
            for val in data[key]:
                ls.append(val)
            graph.append(ls)
    else:
        graph=data

    n= len(graph)
    print(graph)
    if algorithm is Algorithm1:
        print("Algorithm1: ")
        v = [False for i in range(n)]
        v[0] = True
        Algorithm1(graph, v, 0, n, 1, 0)
        print(min(answer))

    if algorithm is Algorithm2:
        print("Algorithm2: ")
        s = 0
        print(Algorithm2(graph, s))



def Algorithm1(graph, v, currPos, n, count, cost):


    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
            # Mark as visited
            v[i] = True
            Algorithm1(graph, v, i, n, count + 1,
                cost + graph[currPos][i])


            # Mark ith node as unvisited
            v[i] = False


def Algorithm2(graph, s):
    # store all vertex apart from source vertex

    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path




if __name__ == "__main__":

    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    graph2 ={0: [10, 15, 20] ,10: [0, 35, 25], 15 : [35, 0, 30], 20 : [ 25, 30, 0]}

    Tsp(Algorithm2, graph)