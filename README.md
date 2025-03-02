# DaMVA

## 0. overview

## 1. Install and Prepare Datasets for Image-goal Navigation

### 👒 1.1 Install habitat-lab 
```bash
# clone our repo
git clone https://github.com/hujch23/World-Model-Navigation.git
cd World-Model-Navigation

# clone habitat-lab code
git submodule init
git submodule update

# create conda env
conda create -n World-Model-Navigation python=3.8

# install habitat-sim
conda install habitat-sim=0.2.2 withbullet headless -c conda-forge -c aihabitat

# install pytorch1.11
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html

# install habitat-lab and habitat-baselines
cd habitat-lab
git checkout 1f7cfbdd3debc825f1f2fd4b9e1a8d6d4bc9bfc7
pip install -e habitat-lab 
pip install -e habitat-baselines

pip install -r requirements.txt
```

### 🗂️ 1.2  Download Scene Datasets
You can download the datasets from https://github.com/XinyuSun/FGPrompt. As mentioned in the repository, follow the official guidelines to download Gibson, HM3D, and MP3D scene datasets and place them in the data/scene_datasets directory.

### 📑 1.3  Prepare Train and Test episodes
We provide the script `datasets.py` to ensure the smooth loading of both curved and straight test episodes.
