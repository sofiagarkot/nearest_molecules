import deepchem as dc
from rdkit import Chem
import numpy as np
import pandas as pd
file = pd.read_csv("embd_neighbours_only_100K_rmse_original_smiles.csv")
dataset = file.iloc[:, 0]
mols = [Chem.MolFromSmiles(s) for s in dataset]
featurizer = dc.feat.fingerprints.CircularFingerprint()
x = featurizer.featurize(mols)
x = pd.DataFrame(x)
x.to_csv('featurized_cf.csv', index=False)

