import datalad.api as dl 

local_path = "./narratives"
url = "///labs/hasson/narratives/derivatives/fmriprep"
data = dl.clone(path=local_path, source=url)

print(data)

