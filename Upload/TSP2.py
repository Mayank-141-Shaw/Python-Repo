# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:43:52 2020

@author: MAYANK SHAW
"""
import copy
import matplotlib.pyplot as plt
from sys import maxsize

def tsp(graph, s, coords):
    #copying all vertex other than start node
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    print(vertex)
    #assuming minpath is very big
    min_path = maxsize
    path_vector = vertex

    while True:
        cur_pathweight = 0
        k = s
        for i in range(len(vertex)):
            cur_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        cur_pathweight += graph[k][s]


        if min_path > cur_pathweight:
            path_vector = copy.copy(vertex)
            print('<><> ',path_vector, cur_pathweight)

        min_path = min(min_path, cur_pathweight)
            
        #bt permuting we get all possible paths
        if not next_permutation(vertex):
            break

    final_path = [s]
    for i in path_vector:
        final_path.append(i)
    final_path.append(s)
    print('>>>> ',final_path)

#now we plot on graph
    given_x = coords[0]
    given_y = coords[1]
    x, y = [], []

    for i in final_path:
        x.append(given_x[i])
        y.append(given_y[i])


    plt.plot(x, y, 'ob-')
    plt.show()

    return min_path

def next_permutation(L):

    n = len(L)

    i = n-2
    while i>=0 and L[i]>=L[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i+1
    while j < n and L[j]>L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i+1
    right = n-1

    while left<right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -=1

    return True

if __name__=='__main__':

    graph_weights = [[0,10,45,20],
                     [10,0,35,25],
                     [45,35,0,30],
                     [20, 25,30,0]]
    s=0

    graph = [[2,1,3,2], [3,1,1,2]]
    print(tsp(graph_weights,s,graph))