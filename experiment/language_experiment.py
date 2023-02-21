import pandas as pd
import numpy as np
# df_h = pd.read_csv('./similarities_1.0_high.tsv', sep='\t')
df = pd.read_csv('./similarities_1.0.tsv', sep='\t')
df_h=df[df['Robustness'] == 'High']
N = 83 # robustness = high
X = np.zeros([N, N])
dic_map = {}
columns = []
index = 0
for i in range(len(df_h)):
    row = df_h.iloc[i]
    lan_1 = row['LangName_1']
    lan_2 = row['LangName_2']
    if dic_map.get(lan_1) is None:
        dic_map[lan_1] = index
        columns.append(lan_1)
        index += 1
    if dic_map.get(lan_2) is None:
        dic_map[lan_2] = index
        columns.append(lan_2)
        index += 1
    index_1 = dic_map[lan_1]
    index_2 = dic_map[lan_2]
    X[index_1, index_2] = row['Similarity']
    X[index_2, index_1] = X[index_1, index_2]
for i in range(N):
     X[i, i] = 1
print(X)
filter = [1,  2,  3,  4,  5,  6,  7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18,
       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
       53, 54, 55, 56, 57, 58, 61, 66, 67, 69, 70, 71, 74, 77, 78, 80]
new_columns = []
for i in filter:
    new_columns.append(columns[i])
print(new_columns)

df_sim = pd.DataFrame(X[filter,:][:,filter], index=new_columns, columns=new_columns)
df_sim.to_csv('similarity_matrix.csv', sep=',')
np.save('X.npy', X[filter,:][:,filter])
# import code
# code.interact(local=locals())
