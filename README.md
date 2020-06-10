Files:
1) In order to find the closest molecules firstly generate their embeddings using 'physio_featurization.py' file.
2) Run the algorithm using the 'closer_finder.py' file as following: 

      python closer_finder.py \<start> \<end> <bool_physio>
      
where:
<start> indicates the index of a molecule in the dataset 'embd_neighbours_only_100K_rmse_original_smiles.csv' you want to start with
<end> -- the index of the last molecule in a dataset
<bool_physio> is an indicator for an embedding you want to test (in order to generate closest molecules by Physio Chemical Featurization run 'physio_featurization.py' file, otherwise for Circular Fingerprint Featurizaion there is needed a resulting file after running 'cf_featurization.py' file)

3) After several hours the algorithm will generate appropriate file depending on the inputs.
As an example, after running 'python closer_finder.py 10000 15000 True' you will get a file 'PhysiochemicalFeaturization10000_to_15000.csv' with 10 closest molecules.

4) For faster results an algorithm was runned at 20 потоки (from 0 to 5000, from 5000 to 10000, etc.) and the file 'combining.py' combines the outputs into a single file 'Physiochemical_Featurizing.csv'.

5) The file 'similarity.py' computes the similarity score based on total number of correctly predicted 10 closest molecules divided by a total number of predictions (= 100000*\10). For running it needs the former 'embd_neighbours_only_100K_rmse_original_smiles.csv' file as well as 'Physiochemical_Featurizing.csv'.
