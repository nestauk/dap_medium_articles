import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt
from getters.english_la_iod_data_2019 import get_english_la_iod_2019
from getters.english_lsoa_iod_data_2019 import get_english_lsoa_iod_2019
from getters.lsoa_shapefiles_2011 import get_english_lsoa_shapefiles_2011
from utils.utils_fonts_colours import *
from PIL import Image
import os


# Caches the data to prevent computation on every rerun
@st.cache_data
def get_data(suppress_st_warning=True):
    return get_english_la_iod_2019()


@st.cache_data
def get_lsoa_data(suppress_st_warning=True):
    return get_english_lsoa_iod_2019()


current_dir = os.getcwd()

# Add your own font/colours here:
alt.themes.register("nestafont", nestafont)
alt.themes.enable("nestafont")
colours = NESTA_COLOURS

# Load the favicon and set the page config (so what appears in the tab on your web browser)
# Change the favicon here:
im = Image.open(f"{current_dir}/images/favicon.ico")
st.set_page_config(page_title="NAME OF YOUR APP", layout="wide", page_icon=im)

# Creates the Navigation bar on the side:
with st.sidebar:
    choose = option_menu(
        # Title of the navigation bar
        "NAV BAR",
        # Title of the sections
        ["PAGE 1", "PAGE 2"],
        # Icons of the sections
        icons=[
            "house",
            "geo-alt",
        ],
        default_index=0,
        orientation="vertical",
        styles={
            "container": {
                "background-color": NESTA_COLOURS[12],
            },
            "icon": {"color": NESTA_COLOURS[10], "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": NESTA_COLOURS[0]},
        },
    )

# For PAGE 1 (which we have not password protected):
if choose == "PAGE 1":
    # How to add images:
    nesta_logo = Image.open(f"{current_dir}/images/nesta_logo.png")
    st.image(nesta_logo, width=250)

    # How to create a title for the page:
    st.title("Title of App")

    # You can use st.markdown to add text to the app:
    st.markdown(
        """
            This is an example of using markdown. 

            Below is an expander you can click on.
            """
    )
    with st.expander("Click on me!"):
        # Can put figures, charts, text here:
        iod_graphic = Image.open(f"{current_dir}/images/iod_graphic.png")
        st.image(iod_graphic)

        # How to add url hyperlinks:
        text_iod = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833959/IoD2019_Infographic.pdf"
        st.markdown(
            f"<div style='text-align: center;'>Taken from the ONS infographic <a href={text_iod}> here</a>. </div>",
            unsafe_allow_html=True,
        )


# In order to password protect the rest of the app, put the rest of the code inside a function.
def name_of_app():
    # Sets a spinner so we know that the report is updating as we change the user selections.
    with st.spinner("Updating Report..."):
        # Loading in the data
        imd_lsoa_data = get_lsoa_data().query("lad19nm == 'York'")
        geodata_lsoa = get_english_lsoa_shapefiles_2011("yorkshire_and_the_humber")

        if choose == "PAGE 2":
            # Filtering for York
            iod_lsoa_data_york = imd_lsoa_data.query("lad19nm == 'York'")
            lsoas_to_plot = list(iod_lsoa_data_york.lsoa11nm)
            color_lsoa = alt.Color(
                "income_deprivation_affecting_children:O",
                scale=alt.Scale(scheme="yellowgreenblue"),
                title="IDACI",
                legend=alt.Legend(orient="top"),
            )

            # To plot a geojson in Vega-Altair we use .mark_geoshape()
            choro_lsoa = (
                alt.Chart(geodata_lsoa)
                .mark_geoshape(stroke="black")
                # We then need to link the geojson to the iod_lsoa_data_york dataframe, using the .transform_lookup we can do this in the plotting code.
                .transform_lookup(
                    # We want to match on the lsoa11nm which is stored under properties.lsoa11nm in the geojson
                    lookup="properties.lsoa11nm",
                    from_=alt.LookupData(
                        # This is the dataframe we want to read the data from.
                        iod_lsoa_data_york,
                        # This is the column we want to match on
                        "lsoa11nm",
                        # These are the column names we want to bring in from the iod_lsoa_data_york dataframe.
                        [
                            "lsoa11cd",
                            "lsoa11nm",
                            "lad19cd",
                            "lad19nm",
                            "income_deprivation_affecting_children",
                        ],
                    ),
                )
                # We then want to make sure that we just plot the LSOAs which are in the York dataset, rather than the whole of the UK, therefore we use this .transform_filter function.
                .transform_filter(
                    alt.FieldOneOfPredicate(
                        field="properties.lsoa11nm", oneOf=lsoas_to_plot
                    )
                )
                # Here is where we encode the colour, which we specified earlier.
                .encode(
                    color=color_lsoa,
                    # We’ve also added an interactive tooltip so you can hover over each LSOA and see its name and its IDACI.
                    tooltip=[
                        alt.Tooltip("lsoa11nm:N", title="LSOA"),
                        alt.Tooltip(
                            "income_deprivation_affecting_children:O", title="IDACI"
                        ),
                    ],
                )
                .project(type="identity", reflectY=True)
                .properties(width=500, height=500)
            )

            choro_lsoa = (
                choro_lsoa.configure_legend(
                    labelLimit=0,
                    titleLimit=0,
                    titleFontSize=13,
                    labelFontSize=13,
                    symbolStrokeWidth=1.5,
                    symbolSize=150,
                )
                .configure_view(strokeWidth=0)
                .configure_axis(labelLimit=0, titleLimit=0)
            )

            # Plotting the chart in altair
            st.altair_chart(choro_lsoa, use_container_width=True)

            # Task: Can you create some interactive bar charts and figures using this code?
            # Hint: you can use the code in the blog 'Vega-Altair - a surprisingly powerful Python library for plotting interactive maps' to recreate the example. See altair_interactive_charts_tutorial.ipynb.


# This adds on the password protection
pwd = st.sidebar.text_input("Password:", type="password")
# st.secrets reads it in from the toml folder, and then runs the streamlit_iod function if the password matches.
if pwd == st.secrets["PASSWORD"]:
    name_of_app()
elif pwd == "":
    pass
else:
    st.error("Password incorrect. Please try again.")
