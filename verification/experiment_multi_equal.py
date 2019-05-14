'''This file is used to verify the ideal condition of I(Z_V), see trival_solution.tex
\ref{eq:me} for detail. This experiment will produce 
[5.857142857142857, 6.0]
[6.0]
[6.010526315789473]
to the console, which is equal to the theoretical result.
'''
import random
import argparse

import numpy as np
import networkx as nx

from info_cluster import InfoCluster

n = 12
k = 8
choice_array = [i for i in range(k*n)]

def check_constraint(G):
    for t1 in range(k):
        for t2 in range(t1+1, k):
            num_edge = 0
            for i in range(t1*n, t1*n+n):
                num_edge_each = 0
                for j in range(t2*n, t2*n+n):
                    if(G.has_edge(i, j)):
                        num_edge += 1
                        num_edge_each += 1
                if(num_edge_each == n):
                    return False
            if(num_edge >= n/2):
                return False       
    return True
def construct():
    G = nx.Graph()
    for t in range(k):
        for i in range(n):
            for j in range(i+1, n):
                G.add_edge(t*n+i, t*n+j)    

    cnt = 0
    while(cnt < n*(k-1)/2):
        a, b = np.random.choice(choice_array, 2)
        if(a == b):
            continue
        if(G.has_edge(a, b)):
            continue            
        cnt += 1
        G.add_edge(a,b)
    return (G, a, b)
    
def graph_plot(G):
    # G: networkx graph object
    global n,k
    g = graphviz.Graph(filename='multi_equal.gv', engine='neato') # g is used for plotting
    for i in range(n*k):
        g.node(str(i))
    for e in nx.edges(G):
        i,j = e
        if(abs(i-j) < n):
            weight_value = 1
        else:
            weight_value = 0.1
        g.edge(str(i), str(j), weight=str(weight_value))    
    g.save()  
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--under_only',default=False, type=bool, nargs='?', const=True) 
    parser.add_argument('--print_tree',default=False, type=bool, nargs='?', const=True)     
    args = parser.parse_args()    
    G, a, b = construct()
    while(not check_constraint(G)):
        G, a, b = construct()
    mat = np.asarray(nx.adjacency_matrix(G).todense(),dtype=float)

    # under critical condition
    ic = InfoCluster(affinity = 'precomputed')    
    mat[a,b] = 0    
    mat[b,a] = 0
    ic.fit(mat)
    print(ic.critical_values)
    if(args.print_tree):        
        ic.print_hierachical_tree()
    
    if not(args.under_only):
        # in critical condition
        mat[a, b] = 1 
        mat[b, a] = 1          
        ic.fit(mat)
        print(ic.critical_values)
        if(args.print_tree):
            ic.print_hierachical_tree()
        
        # up critical condition
        while(True):
            a, b = np.random.choice(choice_array,2) 
            if(a == b):
                continue
            if(G.has_edge(a, b)):
                continue                      
            break

        mat[a,b] = 1
        mat[b,a] = 1
        ic.fit(mat)
        print(ic.critical_values)
        if(args.print_tree):        
            ic.print_hierachical_tree()        
        