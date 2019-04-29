# two level hierachical clustering, info-clustering algorithm can recover the original graph with 
# partition_num_list = [1, k2, k2*k1, n*k2*k1]
from info_cluster import InfoCluster
import random
import numpy as np
import argparse
import networkx as nx # for manipulating graph data-structure
import graphviz # for writing .gv file
import pdb
n = 12
k1 = 7
k2 = 3

def construct(p1):
    '''
       p1: type float, percentage of edges to be removed at first level.
    '''
    global n,k1,k2
    G = nx.Graph()
    # first level
    for t in range(k1*k2):
        for i in range(n):
            for j in range(i+1,n):
                G.add_edge(t*n+i,t*n+j)    
    # second level
    for t in range(k2):
        for i in range(k1):
            for j in range(i+1,k1):
                G.add_edge(t*n*k1+i*n, t*n*k1+j*n) # link the first vertice together

    cnt = 0
    a = 0
    b = 0
    choice_array = [i for i in range(k1*k2)]
    while(cnt < k1*(k2-1)/2 - 1):
        a1,b1 = np.random.choice(choice_array,2)
        if(a1 == b1):
            continue
        if(a1 < b1):
            a = a1
            b = b1
        else:
            a = b1
            b = a1
        if(G.has_edge(a*n, b*n)):
            continue  
        a = a1
        b = b1
        cnt += 1
        G.add_edge(a*n,b*n)
        print('add edge', a*n, b*n)
    return G    
def graph_plot(G):
    # G: networkx graph object
    global n, k1,k2
    g = graphviz.Graph(filename='two_level.gv', engine='neato') # g is used for plotting
    for i in range(n*k1*k2):
        g.node(str(i), shape='point')
    for e in nx.edges(G):
        i,j = e
        if(abs(i-j) < n):
            weight_value = 1
        elif(abs(i-j) < n*k1):
            weight_value = 0.2
        else:
            weight_value = 0.04
        g.edge(str(i), str(j), weight=str(weight_value))    
    g.save()    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_graph', default=False, type=bool, nargs='?', const=True, help='whether to save the .gv file') 
    parser.add_argument('--print_tree', default=False, type=bool, nargs='?', const=True, help='whether to print the hierachical tree')
    parser.add_argument('--p1', default=0.0, type=float, help='first level random parameter')      
    args = parser.parse_args()
    
    ic = InfoCluster(affinity='precomputed')
    G = construct(args.p1)    
    if(args.save_graph):
        graph_plot(G)
    # use neato to plot the tree
    sparse_mat = nx.adjacency_matrix(G)
    ic.fit(np.asarray(sparse_mat.todense(),dtype=float))
    print(ic.partition_num_list)
    if(args.print_tree):        
       ic.print_hierachical_tree()        
        