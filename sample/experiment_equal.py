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
            mat[i,j] = 1
    for i in range(n,2*n):
        for j in range(i+1,2*n):
            mat[i,j] = 1
    choice_array = [i for i in range(n)]

    cnt = 0
    a = 0
    b = 0
    while(cnt < n/2):
        a1,b1 = np.random.choice(choice_array,2)
        if(a1 == a and b1 == b):
            continue
        a = a1
        b = b1
        cnt += 1
        mat[a,b+n] = 1
    # under critical condition
    mat[a,b+n] = 0    
    ic.fit(mat)
    print(ic.critical_values)
    if(args.print_tree):        
        ic.print_hierachical_tree()
    
    if not(args.under_only):
        # in critical condition
        mat[a,b+n] = 1    
        ic.fit(mat)
        print(ic.critical_values)
        if(args.print_tree):
            ic.print_hierachical_tree()
        
        # up critical condition
        while(True):
            a1,b1 = np.random.choice(choice_array,2)
            if(a1 == a and b1 == b):
                continue
            a = a1
            b = b1
            break

        mat[a,b+n] = 1
        ic.fit(mat)
        print(ic.critical_values)
        if(args.print_tree):        
            ic.print_hierachical_tree()        
        