# Training spaCy's spancat component in Python 🐍

<p align="center">
  <img src="https://user-images.githubusercontent.com/46863334/194558740-95e51e09-81d9-41b6-8481-38a2aaee3f98.gif" alt="spancat"/>
</p>

The code behind [this medium article on training spaCy's spancat component in Python](https://hackmd.io/Yg2u3MZQS26_WbdO5WSdWw?edit).

The entity recognition dataset has been downloaded from [Kaggle here](https://www.kaggle.com/datasets/debasisdotcom/name-entity-recognition-ner-dataset) and is shared [under DbCL v1.0](https://www.ebi.ac.uk/ols/ontologies/swo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fswo%2Flicense%2FSWO_1000097).   


## Set up 🛠️

1. **Clone this git repo:** `git clone https://github.com/india-kerle/spancat.git`
2. **Create your conda environment:** `conda create --name spancat_training`
3. **Activate your conda environment:** `conda activate spancat_training` 
4. **install spacy:**
```
pip install -U pip setuptools wheel
pip install -U spacy
```
5. **(at the repo base) install other dependencies:** `pip install -r requirements.txt`

6. **add your environment to your notebook:** 
```
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=spancat_training
```

7. **Run the notebook to replicate the training!** Remember to make sure your kernel is the right environment, `spancat_training`. 