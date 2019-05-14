'''This file is used to verify the ideal condition of I(Z_V), see trival_solution.tex
\ref{ex:2nc} for detail. This experiment will produce 
[199.0, 200.0]
[200.0]
[200.02564102564102]
to the console, which is equal to the theoretical result.
'''
from info_cluster import InfoCluster
import random
import numpy as np
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--under_only',default=False, type=bool, nargs='?', const=True) 
    parser.add_argument('--print_tree',default=False, type=bool, nargs='?', const=True)     
    args = parser.parse_args()
    
    ic = InfoCluster(affinity = 'precomputed')
    n = 20
    mat = np.zeros([2*n,2*n])
    for i in range(n):
        for j in range(i+1,n):
            mat[i,j] = n
    for i in range(n,2*n):
        for j in range(i+1,2*n):
            mat[i,j] = n
    choice_array = [(i, n + j) for i in range(n) for j in range(n)]
    cnt = int(n*n/2)
    choice_array_index = [i for i in range(n*n)]
    choice_list = np.random.choice(choice_array_index, cnt, replace=False)
    for item in choice_list:
        a, b = choice_array[item]
        mat[a,b] = 1
    # under critical condition
    mat[a,b] = 0    
    ic.fit(mat)
    print(ic.critical_values)
    if(args.print_tree):        
        ic.print_hierachical_tree()
    
    if not(args.under_only):
        # in critical condition
        mat[a,b] = 1    
        ic.fit(mat)
        print(ic.critical_values)
        if(args.print_tree):
            ic.print_hierachical_tree()
        
        # up critical condition
        while(True):
            index_new = np.random.choice(choice_array_index, 1)
            a1, b1 = choice_array[index_new[0]]
            if(mat[a1,b1] > 0):
                continue
            a = a1
            b = b1
            break

        mat[a,b] = 1
        ic.fit(mat)
        print(ic.critical_values)
        if(args.print_tree):        
            ic.print_hierachical_tree()        
        