import pandas as pd
import numpy as np
file_dz = pd.read_csv("embd_neighbours_only_100K_rmse_original_smiles.csv", sep='\t', header=None, usecols=[i for i in range(10)])

data_dz = file_dz.set_index(0).T.to_dict('list')
file_me = pd.read_csv("Physiochemical_Featurizing.csv")
same = []
similarity = 0
similarity_dict = {}

i = 0
for mol in list(file_me.iloc[:,0]):
    l = np.flatnonzero(file_me.iloc[:, 0] == mol)
    corresponding_me = set(list(file_me.iloc[l[0],1:10]))
    corresponding_dz = set(data_dz[mol][:])
    intersection = corresponding_me.intersection(corresponding_dz)
    similarity_dict[mol] = len(intersection)/len(corresponding_me)
    similarity += len(intersection)/len(corresponding_me)

similarity  = similarity/len(similarity_dict)
print(similarity)