import pandas as pd
file1 = pd.read_csv("PhysiochemicalFeaturization0_to_5000.csv")
file2 = pd.read_csv("PhysiochemicalFeaturization5000_to_10000.csv")
file3 = pd.read_csv("PhysiochemicalFeaturization10000_to_15000.csv")
file4 = pd.read_csv("PhysiochemicalFeaturization15000_to_20000.csv")
file5 = pd.read_csv("PhysiochemicalFeaturization20000_to_25000.csv")
file6 = pd.read_csv("PhysiochemicalFeaturization25000_to_30000.csv")
file7 = pd.read_csv("PhysiochemicalFeaturization30000_to_35000.csv")
file8 = pd.read_csv("PhysiochemicalFeaturization35000_to_40000.csv")
file9 = pd.read_csv("PhysiochemicalFeaturization40000_to_45000.csv")
file10 = pd.read_csv("PhysiochemicalFeaturization45000_to_50000.csv")
file11 = pd.read_csv("PhysiochemicalFeaturization50000_to_55000.csv")
file12 = pd.read_csv("PhysiochemicalFeaturization55000_to_60000.csv")
file13 = pd.read_csv("PhysiochemicalFeaturization60000_to_65000.csv")
file14 = pd.read_csv("PhysiochemicalFeaturization65000_to_70000.csv")
file15 = pd.read_csv("PhysiochemicalFeaturization70000_to_75000.csv")
file16 = pd.read_csv("PhysiochemicalFeaturization75000_to_80000.csv")
file17 = pd.read_csv("PhysiochemicalFeaturization80000_to_85000.csv")
file18 = pd.read_csv("PhysiochemicalFeaturization85000_to_90000.csv")
file19 = pd.read_csv("PhysiochemicalFeaturization90000_to_95000.csv")
file20 = pd.read_csv("PhysiochemicalFeaturization95000_to_100000.csv")
file_dz = pd.read_csv("embd_neighbours_only_100K_rmse_original_smiles.csv", sep='\t', header=None, usecols=[i for i in range(10)])
data = pd.concat([file1, file2, file3, file4, file5, file6, file7, file8, file9, file10, file11, file12, file13, file14,
                  file15, file16,file17, file18, file19, file20], ignore_index=True, sort=False)
ready = []
for i in range(len(file_dz[0]) - 1):
    ready.append([file_dz[0][i], data['1st closest'][i],data['2nd closest'][i],
                  data['3rd closest'][i],
                  data['4th closest'][i],
                  data['5th closest'][i],
                  data['6th closest'][i],
                  data['7th closest'][i],
                  data['8th closest'][i],
                  data['9th closest'][i],
                  data['10th closest'][i]])

ready = pd.DataFrame(ready)
ready.to_csv('Physiochemical_Featurizing.csv', index=False)
