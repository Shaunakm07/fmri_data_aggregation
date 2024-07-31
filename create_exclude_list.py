import json 

with open("scan_exclude.json") as f:
   d = json.load(f)

exclude_list = []

for key in d.keys():
    for sub in (d[key]):
        for e in (d[key][sub]):
            exclude_list.append(e + "_space-MNI152NLin6Asym_res-native_desc-preproc_bold.nii.gz")
            exclude_list.append(e + "_space-MNI152NLin6Asym_res-native_desc-brain_mask.nii.gz")

with open("exclude_files.json", "w") as file:
    json.dump(exclude_list, file)

with open("exclude_files.json", "r") as file:
    contents = json.load(file)
    print(contents)