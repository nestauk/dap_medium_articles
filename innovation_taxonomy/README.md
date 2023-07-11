# Building a Taxonomy of Innovation

Code to interact and experiment with the taxonomies described in [this medium article on developing a taxonomy of research in the UK]().

## Setup 🛠️

Open your terminal and follow the instructions:

1. **Clone this repo:**

    `git clone https://github.com/nestauk/dap_medium_articles.git`

2. **Navigate to this tutorial's folder:**

    `cd innovation_taxonomy`

3. **Create a virtual or conda environment (using Python 3.9 🐍) and install required dependencies**

    `pip install -r requirements.txt`
   
5. **Download the data from [here](https://nesta-open-data.s3.eu-west-2.amazonaws.com/innovation_taxonomy/data.zip):**

    Unzip the folder within the project directory. Your project folder should now look like:

```
dap_medium_articles\innovation_taxonomy\
    > data\
        > taxonomies\
        > group_names\
    > requirements.txt
    > getters.py
    > taxonomy_demo.ipynb
```


## Usage 💻

Launch the notebook `taxonomy_demo.ipynb` for a walkthrough of how to load and explore the three taxonomies described in the Medium article. 

The functions provided in `getters.py` could be leveraged to build pipelines on top of any documents tagged with Wikipedia entities using the (DBPedia Spotlight)[https://www.dbpedia-spotlight.org/api] annotate api.
