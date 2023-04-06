# Creating a Streamlit app using Python

This folder contains the code behind the [medium article]() with the example streamlit app.

To see the live app, click this [link](), the password is `Nesta@IoD`.

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

6. **Open the `streamlit_demo_iod_analysis` file and have a read through!** 

7. **Run the app on your local machine:**
`streamlit run streamlit_demo_iod_analysis.py`

Alternatively if you want the app without the style choices, see `streamlit_demo_iod_analysis_without.py`.

## About the data
data:
IoD values for each English Local Authority (LA).
IoD values for each English Lower Suport Output Area(LSOA).

shapefiles: 
LA shapefiles for the choropleth maps.
LSOA shapefiles for the choropleth maps, broken down by region due to reduce file sizes.