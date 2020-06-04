from rdkit import Chem
import numpy as np
import pandas as pd
from math import sqrt
from tqdm import tqdm
import deepchem as dc
import time
import argparse
import molecules_multiprocessing
start_time = time.time()
class Finder:
    def __init__(self):
        file = pd.read_csv("embd_neighbours_only_100K_rmse_original_smiles.csv")
        self.dataset = file.iloc[:, 0]

    def _RMSE(self, x, y):
        return sqrt(sum(np.square(x - y)) / len(x))

    def find_n(self, data, element, index_of_element):
        neighbors = []
        for index, e in enumerate(data):
            if index != index_of_element:
                dist = self._RMSE(element, e)
                if len(neighbors) < 10:
                    neighbors.append((dist, index))
                    neighbors = sorted(neighbors, key=lambda x: x[0])
                else:
                    if dist < neighbors[9][0]:
                        neighbors.append((dist, index))
                        neighbors = sorted(neighbors, key=lambda x: x[0])
                        neighbors = neighbors[0:10]

        molecules = [n[1] for n in neighbors]
        molecules.insert(0, index_of_element)
        return molecules

    def prepare(self, start, end, atomic):
        print("Molecules loading")
        mols = [Chem.MolFromSmiles(s) for s in self.dataset[:]]
        print("Molecules loaded")
        if atomic == False:
            file1 = pd.read_csv("featurized_cf.csv")
            x = np.array(file1.iloc[:, :])
            subset = x[start:end]
        else:

            file1 = pd.read_csv("featurized_ph.csv")
            x = np.array(file1.iloc[:, :])
            subset = x[start:end]

        closest_df = []

        for i, mol in tqdm(enumerate(subset)):
            closest_df.append(self.find_n(x, mol, i))

        neighbors_molecules = []
        for mol in closest_df:
            row = [Chem.MolToSmiles(mols[i]) for i in mol]
            neighbors_molecules.append(row)


        neighbors = np.array(neighbors_molecules)
        print(neighbors)
        neighbors_dataframe = pd.DataFrame(
            {'Molecule name': neighbors[:, 0], '1st closest': neighbors[:, 1], '2nd closest': neighbors[:, 2],
             '3rd closest': neighbors[:, 3], '4th closest': neighbors[:, 4], '5th closest': neighbors[:, 5],
             '6th closest': neighbors[:, 6], '7th closest': neighbors[:, 7], '8th closest': neighbors[:, 8],
             '9th closest': neighbors[:, 9], '10th closest': neighbors[:, 10]})
        if not atomic:
            name = 'CircularFingerprintsFeaturization'+str(start)+'_to_'+str(end)+'.csv'
        else:
            name = 'PhysiochemicalFeaturization'+str(start)+'_to_'+str(end)+'.csv'
        neighbors_dataframe.to_csv(name, index=False)

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
parser.add_argument("start", help="fist index by slicing the dataset",
                    type=int)
parser.add_argument("end", help="last index by slicing the dataset",
                    type=int)
parser.add_argument("atomic", type=str2bool, nargs='?', const=True, default=False,
                        help="bool indicating the  method of featurization")
args = parser.parse_args()

start = args.start
end = args.end
atomic = args.atomic

if atomic:
    print("Physiochemical Featurization", start, end)
else:
    print("Circular Fingerprints Featurization", start, end)

nonatomic_f = Finder()
print("Dataset loaded")
nonatomic_f.prepare(start, end, atomic)

finish = time.time()
print("5K molecules: ", finish - start_time)