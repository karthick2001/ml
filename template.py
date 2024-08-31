import os 
from pathlib import Path

list_of_files=[
    "data/",
    "src/__init__.py",
    "src/model.py",
    "src/preprocess.py",
    "src/train.py",
    "src/app.py",
    "src/Dockerfile",
    "src/requirement.txt",
    "scripts/build_image.sh",
    "scripts/deploy_eks.sh",
    "scripts/create_eks_cluster.sh",
    "scripts/create_s3_bucket.py",
    "kubernetes/deployment.yaml",
    "kubernetes/service.yaml",
    "aws/codepipeline.yaml",
    "aws/eks_config.yaml",
               ]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
