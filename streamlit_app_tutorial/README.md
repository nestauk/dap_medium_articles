# Creating a Streamlit app using Python

This folder contains the code behind the [medium article]() with the example streamlit app.

To see the live app, click this [link](https://dap-tutorial-geographical-iod-deciles.streamlit.app/), the password is `Nesta@IoD`.

If you wish to run the app locally, follow the instructions below.

## Set up 🛠️
Open your terminal and follow the instructions:
1. **Clone this repo:** 

`git clone https://github.com/nestauk/dap_medium_articles.git`

2. **Navigate to this tutorial's folder:** 

`cd streamlit_app_tutorial`

3. **Create your conda environment:** 

`conda create --name streamlit_app_tutorial`

4. **Activate your conda environment:** 

`conda activate streamlit_app_tutorial`

5. **Install package dependencies:** 

`pip install -r requirements.txt`
If pip is not installed, install pip by `conda install pip`.

6. **Open the `streamlit_demo_iod_analysis.py` file and have a read through!** 

7. **Run the app on your local machine:**

Inside your .streamlit folder create a file called `secrets.toml` and add the following:

`PASSWORD = "Nesta@IoD"`

Then run:

`streamlit run streamlit_demo_iod_analysis.py`

Alternatively if you want an to have a go yourself using streamlit with some of the basics set up, see `streamlit_template.py`.

## About the data
data:

IoD (2019) values for each English Local Authority (LA).

IoD (2019) values for each English Lower Suport Output Area(LSOA).

You can find the open data for the IoD [here](https://opendatacommunities.org/def/concept/folders/themes/societal-wellbeing).

shapefiles (in another repository): 

LA 2019 geographical boundaries for the choropleth maps.

LSOA 2019 geographical boundaries for the choropleth maps, broken down by region due to reduce file sizes.

You can find the open data for the geographical boundaries [here](https://geoportal.statistics.gov.uk/search?collection=Dataset).
