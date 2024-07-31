import datalad.api as dl 
import os 
import numpy as np
import h5py 
import nibabel as nib
from nilearn.input_data import NiftiMasker

root = "./listening_task"
data_set_root = "./"
dataset = dl.Dataset(data_set_root)

if not dataset.is_installed():
  print('No dataset')
  exit(1)
else:
  print("dataset successfully loaded")

def get_paths():
    paths = []
    subjects = [i for i in os.listdir(os.path.join(root, "derivative/preprocessed_data")) if (i.startswith('UTS'))]
    subjects = sorted(subjects)

    for i in subjects:
        tr_count = 0

        path = os.path.join(root, "derivative/preprocessed_data")
        path = os.path.join(path, i)
        for j in ((os.listdir(path))):
            print(j)
            if j.endswith(".hf5"):
                dataset.get(os.path.join(path, j))  

                with h5py.File(os.path.join(path, j), "r") as f:
                    data_key = f.keys()
                    print(data_key)
                    data = f["data"][:]
                    print(data.shape)
                if not os.path.exists(os.path.join("./dataset", i)):
                    os.makedirs(os.path.join("./dataset", i))
                    
                for k in data:
                    np.save(os.path.join(os.path.join("./dataset", i), str(tr_count)), k)
                    tr_count += 1
                
                dataset.drop(os.path.join(path, j))       

get_paths()