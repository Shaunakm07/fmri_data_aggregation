import datalad.api as dl 
import os 
import numpy as np
import json 
import nibabel as nib
from nilearn.input_data import NiftiMasker

root = "./narratives"
data_set_root = "./"
dataset = dl.Dataset(data_set_root)

if not dataset.is_installed():
  print('No dataset')
  exit(1)
else:
  print("dataset successfully loaded")

with open("exclude_files.json", "r") as file:
    exclude_list = json.load(file)

def get_paths():
    paths = []
    masks = []
    subjects = [i for i in os.listdir(root) if (i.startswith('sub-') and (i.endswith(".html") == False))]
    subjects = sorted(subjects)

    for i in subjects:
        path = os.path.join(root, i)
        func = os.path.join(path, "func")

        for j in os.listdir(func):
            if j.endswith("_space-MNI152NLin6Asym_res-native_desc-preproc_bold.nii.gz"):
                try:
                    if j not in exclude_list:
                        task = j.split('task-')[1].split('_')[0]
                        path = os.path.join(func, j)
                        paths.append([path, task])
                except Exception as e:
                    print(f"Error for file {path}: {str(e)}")
            elif j.endswith("_space-MNI152NLin6Asym_res-native_desc-brain_mask.nii.gz"):
                    if j not in exclude_list:
                        path = os.path.join(func, j)
                        masks.append(path)

    return sorted(paths), sorted(masks)
    
paths, masks = get_paths()

length = len(paths)

for i in range(length):
    mask = masks[i]
    path, task = paths[i]

    print("getting data")
    dataset.get(path)
    dataset.get(mask)

    masker = NiftiMasker(mask_img=None)
    func_data = masker.fit_transform(path)
    print(path)
    print(task)
    print(func_data.shape)

    if not os.path.exists(os.path.join("./dataset", task)):
        os.makedirs(os.path.join("./dataset", task))

    string = os.path.basename(path)
    name = string.split("_space-MNI152NLin6Asym_res-native_desc-preproc_bold.nii.gz")[0]
    np.save((os.path.join(os.path.join("./dataset", task), f"{name}.npy")), func_data)
   
    dataset.drop(path)
    print("dropped data")



'''
nifti_paths = glob.glob(
                os.path.join("./", '**/*sub-001_task-pieman_run-1_space-MNI152NLin6Asym_res-native_desc-preproc_bold.nii.gz'),
                recursive=True)

for path in nifti_paths:
    print(path)
    dataset.get(path)
    img = nib.load(path)
    data = img.get_fdata()
    print(data.shape)


with open("scan_exclude.json") as f:
   d = json.load(f)
   print(d["pieman"])
'''