'''
In this experiment, we prepare a graph with two level hierachical structures.
The graph has k2 macro-communities and in each macro-community there are k1 micro-communities. Each micro-community
contains n nodes. There are also two parameters p1 and p2 which control the inter-community linkage respectively.
Ideally, when p2=0, the graph has k2 connected components and when p2=1, the graph is random at macro-community level.
p1 controls the micro-community linkage in the same manner.
Notice that p1 cannot be zero, otherwise the two-level structure of the graph does not exist.
By using info-clustering algorithm we try to recover the original graph with 
partition_num_list = [1, k2, k2*k1, n*k2*k1] under certain conditions of p1 and p2.

We also use other clustering algorithm which does not require predetermined cluster number. 
For example, Girvan-Newman algorithm and Affinity Propogation. There algorithms can get the macro-community first
and we rerun the algorithm to get the micro-community structures.

As we can see, if the graph has deep hierachical structure, info-cluster has advantages since we only need to run ic algorithm once.
'''
import random
import numpy as np
import argparse
import networkx as nx # for manipulating graph data-structure
import graphviz # for writing .gv file

from info_cluster import InfoCluster
import GN

n = 16
k1 = 4
k2 = 4
K = 18
color_list = ['red','orange','green','purple']

def construct(z_in_1, z_in_2, z_out):
    '''
       p2: type float, percentage of edges to be added at macro level.
       p1: type float, percentage of edges to be added at micro level.
    '''
    global n,k1,k2
    p_1 = z_in_1/(n-1)
    
    assert(p_1 <= 1)
    assert(z_out > 0)
    
    p_2 = z_in_2/(n*(k1-1))
    p_o = z_out/(n*k1*(k2-1))
    G = nx.Graph()
    cnt = 0
    for t in range(k2):
        for i in range(k1):
            for j in range(n):
                G.add_node(cnt, macro=t,micro=i)
                cnt += 1
    for i in G.nodes(data=True):
        for j in G.nodes(data=True):
            if(j[0] <= i[0]):
                continue
            if(i[1]['macro'] != j[1]['macro']):
                if(random.random()<=p_o):
                    G.add_edge(i[0], j[0])
            else:
                if(i[1]['micro'] == j[1]['micro']):
                    if(random.random() <= p_1):
                        G.add_edge(i[0], j[0])
                else:
                    if(random.random() <= p_2):
                        G.add_edge(i[0], j[0])
    return G    
    
def graph_plot(G):
    '''
    generate the plot file which is the input of graphviz.
    G: networkx graph object
    '''
    global n, k1,k2
    g = graphviz.Graph(filename='two_level.gv', engine='neato') # g is used for plotting
    for i in G.nodes(data=True):
        macro_index = i[1]['macro']
        g.node(str(i[0]), shape='point', color=color_list[macro_index])
    for e in nx.edges(G):
        i,j = e
        i_attr = G.node[i]
        j_attr = G.node[j]
        if(i_attr['macro']!=j_attr['macro']):
            edge_len = 2
            weight_value = 0.1
        elif(i_attr['micro']!=j_attr['micro']):
            weight_value = 1
            edge_len = 1
        else:
            weight_value = 10
            edge_len = 0.5
        g.edge(str(i), str(j), weight=str(weight_value), penwidth="0.3", len=str(edge_len))    
    g.save()    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_graph', default=False, type=bool, nargs='?', const=True, help='whether to save the .gv file') 
    parser.add_argument('--ic', default=False, type=bool, nargs='?', const=True, help='whether to run info-cluster algorithm')
    parser.add_argument('--z_in_1', default=14, type=int, help='inter-micro-community node average degree')      
    parser.add_argument('--z_in_2', default=3, type=int, help='intra-micro-community node average degree')          
    args = parser.parse_args()
    
    G = construct(args.z_in_1, args.z_in_2, K - args.z_in_1 - args.z_in_2)    
    if(args.save_graph):
        graph_plot(G)
    if(args.ic):           
        ic = InfoCluster(affinity='precomputed')        
        sparse_mat = nx.adjacency_matrix(G)
        ic.fit(np.asarray(sparse_mat.todense(),dtype=float))
        print(ic.partition_num_list)
    if(args.gn):
        gn_result = GN(G)
        print('number of clusters', len(gn_result))