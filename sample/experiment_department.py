from info_cluster import InfoCluster
import random
import numpy as np
import argparse
from sklearn.cluster import SpectralClustering
if __name__ == '__main__':
    mat = np.zeros([16,16])
    edges = ((1,2),(1,5),(1,4),(2,3),(2,4),(2,5),(3,4),(3,12),(4,12),(4,8),(4,5),(5,6),(5,11),(6,8),(6,7),(6,9),(7,8),(7,9),(7,10),(8,9),(8,11),(8,12),(9,10),(9,11),(10,11),(10,16),(11,12),(11,16),(12,13),(12,15),(12,16),(13,14),(13,15),(14,15),(14,16),(15,16))
    for i,j in edges:
        mat[i-1,j-1] = 1
    #ic = InfoCluster(affinity = 'precomputed')
    #ic.fit(mat)
    # print(ic.critical_values)
    sc = SpectralClustering(affinity='precomputed', n_clusters=3)
    mat = (mat+mat.T)/2
    sc.fit(mat)
    print(sc.labels_)
    #ic.print_hierachical_tree()
