'''
    wrapper of Girvan-Newman community detection algorithm
    >>> import networkx as nx
    >>> G=nx.Graph()
    >>> G.add_edge(1,3)
    >>> G.add_edge(1,2)
    >>> G.add_edge(3,2)
    >>> G.add_edge(4,5)
    >>> G.add_edge(4,6)
    >>> G.add_edge(5,6)
    >>> G.add_edge(1,6)
    >>> from GN import GN
    >>> GN(G)
    [{1, 2, 3}, {4, 5, 6}]    
'''
from cmty import cmty
import networkx as nx
def GN(G_outer):
    '''
        G: nx.Graph like object
        returns the partition
    '''
    G = G_outer.copy()# copy the graph
    n = G.number_of_nodes()    #|V|
    A = nx.adj_matrix(G)    #adjacenct matrix

    m_ = 0.0    #the weighted version for number of edges
    for i in range(0,n):
        for j in range(0,n):
            m_ += A[i,j]
    m_ = m_/2.0

    #calculate the weighted degree for each node
    Orig_deg = {}
    Orig_deg = cmty.UpdateDeg(A, G.nodes())

    #run Newman alg
    return cmty.runGirvanNewman(G, Orig_deg, m_)