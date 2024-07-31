import datalad.api as dl 

local_path = "./listening_task"
url = "https://github.com/OpenNeuroDatasets/ds003020.git"
data = dl.clone(path=local_path, source=url)

print(data)

