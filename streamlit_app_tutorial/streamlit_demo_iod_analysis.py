import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt
from utils.utils_fonts_colours import *
from utils.utils_iod_values import *
from utils.utils_preprocessing import preprocess_strings
from PIL import Image
from getters.english_la_iod_data_2019 import get_english_la_iod_2019
from getters.english_lsoa_iod_data_2019 import get_english_lsoa_iod_2019
from getters.la_shapefiles_2019 import get_english_la_shapefiles_2019
from getters.lsoa_shapefiles_2011 import get_english_lsoa_shapefiles_2011
import os


# Caches the data to prevent computation on every rerun
@st.cache_data
def get_data(suppress_st_warning=True):
    return get_english_la_iod_2019()


@st.cache_data
def get_lsoa_data(suppress_st_warning=True):
    return get_english_lsoa_iod_2019()


@st.cache_data
def get_geo_data(suppress_st_warning=True):
    return get_english_la_shapefiles_2019()


current_dir = os.getcwd()

# Creating the font/colours we use for the figures:
alt.themes.register("nestafont", nestafont)
alt.themes.enable("nestafont")

colours = NESTA_COLOURS
# Load the favicon and set the page config (so what appears in the tab on your web browser)
im = Image.open(f"{current_dir}/streamlit_app_tutorial/images/favicon.ico")

st.set_page_config(page_title="IoD Deciles across England", layout="wide", page_icon=im)

# Creates the Navigation bar on the side:
with st.sidebar:
    choose = option_menu(
        # Title of the navigation bar
        "IoD Geographical Analysis",
        # Title of the sections
        [
            "About",
            "English LA Breakdown",
            "English LA Comparison",
            "English LSOA Breakdown",
        ],
        # Icons of the sections
        icons=["house", "geo-alt", "kanban", "geo-alt"],
        default_index=0,
        orientation="vertical",
        styles={
            "container": {
                "padding": "5!important",
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

with st.sidebar:
    colour_choice = st.sidebar.selectbox(
        "Choose a colour palette for the maps:",
        options=list(colour_palettes.keys()),
    )
    # Select box to pick the IoD you wish to look at.
    iod_selection = st.sidebar.selectbox(
        "Choose a IoD Decile to view in the figures:",
        options=iod_names,
    )

# For the About page (which we have not password protected):
if choose == "About":
    # Creates a separate container for us to put the header in
    header = st.container()

    with header:
        # How to add images:
        nesta_logo = Image.open(f"{current_dir}/streamlit_app_tutorial/images/nesta_logo.png")
        st.image(nesta_logo, width=250)

        # How to create a title for the page:
        st.title("Geographical Analysis of the IoD Deciles Across England")

        st.markdown(
            "  **website:** https://www.nesta.org/ **| email:** jess.gillam@nesta.org.uk"
        )

    # You can use st.markdown to add text to the app:
    st.markdown(
        """
            This app shows how open source data can be mapped geographically to look at deprivation levels across England.
            We use the English indices of deprivation (IoD) published in 2019. The IoD are statistics on the relative
            deprivation in small areas in England. Data is available at Local Authority (LA) and Lower Super Output Area (LSOA) level.

            The IoD dataset provides 10 indices, with the Index of Multiple Deprivation (IMD) being a combination of the indices shown in the graphic below.
            """
    )
    with st.expander("Click for IoD graphic:"):
        iod_graphic = Image.open(f"{current_dir}/streamlit_app_tutorial/images/iod_graphic.png")
        st.image(iod_graphic)

        # How to add url hyperlinks:
        text_iod = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833959/IoD2019_Infographic.pdf"
        st.markdown(
            f"<div style='text-align: center;'>Taken from the ONS infographic <a href={text_iod}> here</a>. </div>",
            unsafe_allow_html=True,
        )
    # This uses html syntax within the markdown.
    st.markdown(
        """
            For the geographic boundaries, we use the the corresponding LA (2019) and LSOA (2011) boundaries used for the creation of the IoD dataset.

            """
    )
    text_open_data = (
        "https://opendatacommunities.org/data/societal-wellbeing/imd2019/indices"
    )
    text_geography = "https://geoportal.statistics.gov.uk/search?collection=Dataset"
    github_repo = "https://raw.githubusercontent.com/j-gillam/geographical_iod_analysis"  ###### CHANGE
    st.markdown(
        f"<div> These open datasets can be found on the <a href= {text_open_data}> Open Data Community </a> and from <a href= {text_geography}> Open Geography Portal </a> . See <a href= {github_repo}> here </a> for the github repository with the linked datasets and streamlit code for this app.</div>",
        unsafe_allow_html=True,
    )


# In order to password protect the rest of the app, put the rest of the code inside a function.
def streamlit_iod():
    # Sets a spinner so we know that the report is updating as we change the user selections.
    with st.spinner("Updating Report..."):
        # Possible regions in England.
        region_filter = [
            "North East",
            "North West",
            "Yorkshire and The Humber",
            "East Midlands",
            "West Midlands",
            "South West",
            "East",
            "South East",
            "London",
        ]

        # # Possible IoD domains you want to look at.
        # Loading in the IoD data at LA and LSOA level for English regions.
        data = get_data().query("region_name in @region_filter")
        lsoa_data = get_lsoa_data().query("region_name in @region_filter")

        la_melt = (
            pd.melt(
                data,
                id_vars=["lad19cd", "lad19nm", "region_name"],
                value_vars=iod_indices,
            )
            .rename(columns={"variable": "iod", "value": "decile"})
            .assign(iod_name=lambda df: df.iod.replace(iod_dict_inv))
        )

        # Shapefiles for all of the LA's in the UK.
        geodata_la = get_geo_data()

        # For the LA Breakdown page:
        if choose == "English LA Breakdown":
            # Altair selections (allows you to select a local authority):
            la_select = alt.selection_single(fields=["lad19nm"])
            la_select_all = alt.selection_single(fields=["lad19nm"], empty="none")
            st.title("Local Authorities in England, broken down by IoD Decile")
            st.markdown(
                """
            Choose the IoD you wish to view on the maps in the sidebar. The first map shows results for all of England and the second map shows a 
            region of England which you can select below. Attached to the second map is a bar chart that shows all of the IoD deciles for the 
            Local Authority (LA) selected on the map. You can change the colour palette of the maps in the sidebar. 

            You can click on each LA to highlight it, double-click to remove the selection and hover over the map to see the deciles in a tooltip.
            """
            )
            # Colour pallette chosen for the maps, if you select a certain la, the others will change to 'lightgray'.
            color_ = alt.condition(
                la_select,
                alt.Color(
                    f"{iod_dict[iod_selection]}:O",
                    scale=colour_palettes[colour_choice],
                    title=iod_selection,
                    legend=alt.Legend(orient="top"),
                ),
                alt.value("lightgray"),
            )
            # Creating map for all of England.
            choro_all = (
                alt.Chart(geodata_la)
                .mark_geoshape(
                    stroke="black",
                )
                # Combines with the IoD data on Local Authority Name.
                .transform_lookup(
                    lookup="properties.lad19nm",
                    from_=alt.LookupData(
                        data,
                        "lad19nm",
                        ["lad19cd", "lad19nm", "region_name"] + iod_indices,
                    ),
                )
                # Ensures we are looking at the English La's only.
                .transform_filter(
                    alt.FieldOneOfPredicate(
                        field="properties.lad19nm", oneOf=data.lad19nm.unique()
                    )
                )
                # Specifies the colours and tooltips.
                .encode(
                    color=color_,
                    tooltip=[alt.Tooltip("lad19nm:N", title="Local Authority")]
                    + [
                        alt.Tooltip(f"{ind}:O", title=name, format="1.2f")
                        for ind, name in zip(iod_indices, iod_tooltip)
                    ],
                )
                # Allows interactivity in the altair chart.
                .add_selection(la_select)
                .properties(width=500, height=500)
            )
            choro_all_england = choro_all.configure_legend(
                labelLimit=0,
                titleLimit=0,
                titleFontSize=13,
                labelFontSize=13,
                symbolStrokeWidth=1.5,
                symbolSize=150,
            ).configure_view(strokeWidth=0)
            # Plots the altair chart in streamlit.
            st.altair_chart(
                choro_all_england,
                use_container_width=True,
            )

            # Select box to pick the region you wish to look at.
            region_selection = st.selectbox(
                "To look in closer detail, choose a region of England:",
                options=sorted(region_filter),
            )

            st.markdown(
                "Click on one of the LAs to bring up the deciles in a graph below. Double-click to remove selection. Reminder: you can choose the IoD of interest in the sidebar."
            )

            las_to_plot = list(data[data["region_name"] == region_selection].lad19nm)

            color_las = alt.condition(
                la_select,
                alt.Color(
                    f"{iod_dict[iod_selection]}:O",
                    scale=colour_palettes[colour_choice],
                    title=iod_selection,
                    legend=alt.Legend(orient="top"),
                ),
                alt.value("lightgray"),
            )
            # Altair charts for the regions:
            choro_region = (
                alt.Chart(geodata_la)
                .mark_geoshape(
                    stroke="black",
                )
                .transform_lookup(
                    lookup="properties.lad19nm",
                    from_=alt.LookupData(
                        data,
                        "lad19nm",
                        ["lad19cd", "lad19nm", "region_name"] + iod_indices,
                    ),
                )
                .transform_filter(
                    alt.FieldOneOfPredicate(
                        field="properties.lad19nm", oneOf=las_to_plot
                    )
                )
                .encode(
                    color=color_las,
                    tooltip=[alt.Tooltip("lad19nm:N", title="Local Authority")]
                    + [
                        alt.Tooltip(f"{ind}:O", title=name, format="1.2f")
                        for ind, name in zip(iod_indices, iod_tooltip)
                    ],
                )
                .add_selection(la_select, la_select_all)
                .properties(width=500, height=500)
            )

            # Interactive bar chart that will change based on what is selected in choro_region
            choro_bar = (
                alt.Chart(la_melt)
                .mark_bar(color=NESTA_COLOURS[1])
                .encode(
                    x=alt.X(
                        "decile:Q",
                        title="Decile",
                        scale=alt.Scale(domain=[0, 10]),
                        axis=alt.Axis(tickMinStep=1),
                    ),
                    y=alt.Y(
                        "iod_name:N",
                        title=" ",
                        sort=iod_names,
                        axis=alt.Axis(titlePadding=330),
                    ),
                    # If you wanted to add a color scheme to the bars:
                    # color = alt.Color(
                    #         'decile:Q',
                    #         scale=alt.Scale(domain=domain, range=range_),
                    #         legend=None)
                )
                .transform_filter(la_select_all)
                .properties(width=400, height=400)
            )

            # Adding text to the bar chart
            la_text = (
                alt.Chart(la_melt)
                .mark_text(dy=-210, size=20, color="darkgray")
                .encode(text="lad19nm:N")
                .transform_filter(la_select_all)
            )
            bar_chart = alt.layer(choro_bar, la_text)

            # Combines the two charts together and adds some configurations
            choro_region_la = (
                alt.vconcat(choro_region, bar_chart, center=True)
                .configure_legend(
                    labelLimit=0,
                    titleLimit=0,
                    titleFontSize=13,
                    labelFontSize=13,
                    symbolStrokeWidth=1.5,
                    symbolSize=150,
                )
                .configure_view(strokeWidth=0)
                .configure_axis(
                    labelLimit=0,
                    titleLimit=0,
                )
            )

            # Plots the chart in altair.
            st.altair_chart(
                choro_region_la,
                use_container_width=True,
            )

        # Comparing different Local Authorities
        elif choose == "English LA Comparison":
            st.title("Comparing the IoD for Local Authorities in England")
            st.markdown(
                """
            This bar chart allows you to select up to five Local Authorities (LAs) across England. You can select from the list or type to search for certain LAs. 
            To compare LA's against different IoDs, select the IoD of interest in the sidebar.
            """
            )
            all_las = data.lad19nm.unique()

            # Drop-down selection, allowing up to 5 LA's for filtering in the bar chart below.
            la_compare_select = st.multiselect(
                "Choose up to five LAs:",
                options=sorted(all_las),
                default=None,
                max_selections=5,
            )

            # Filtering the data
            la_compare = la_melt[
                (la_melt.lad19nm.isin(la_compare_select))
                & (la_melt.iod_name == iod_selection)
            ]

            # Bar chart to compare Local Authorities IoD's
            compare_las = (
                alt.Chart(la_compare)
                .mark_bar(size=50, color=NESTA_COLOURS[1])
                .encode(
                    x=alt.X(
                        "decile:Q",
                        title="Decile",
                        scale=alt.Scale(domain=[0, 10]),
                        axis=alt.Axis(tickMinStep=1),
                    ),
                    y=alt.Y("lad19nm:N", title=None),
                )
                .properties(width=600, height=400, title=iod_selection)
            )

            # Configurations for the bar chart
            bar_compare_las = compare_las.configure_view(strokeWidth=0).configure_axis(
                labelLimit=0, titleLimit=0, labelFontSize=18
            )

            # Plotting the chart in altair.
            st.altair_chart(
                bar_compare_las,
                use_container_width=True,
            )

        # Comparing English LSOA's within a Local Authority
        elif choose == "English LSOA Breakdown":
            st.title("Lower Super Output Areas in England, broken down by IoD Decile")
            st.markdown(
                """
            By selecting a region of England, an IoD and a Local Authority (LA), this map shows the breakdown at Lower Super Output Area (LSOA).

            You can click on each LSOA to highlight it, double-click to remove the selection and hover over the map to see the deciles.
            """
            )

            # Select box to pick the region you wish to look at.
            region_selection = st.selectbox(
                "Choose a region of England:",
                options=sorted(region_filter),
                key="region_lsoas",
            )

            # Filtering the LA's by the selected region
            las_to_plot = list(data[data["region_name"] == region_selection].lad19nm)
            data_lsoa = lsoa_data[lsoa_data.region_name == region_selection]

            # Select box to choose the LA you wish to look at.
            la_selection = st.selectbox(
                "Choose a local authority from the region chosen above to see the LSOA breakdown:",
                sorted(las_to_plot),
            )

            # Filtering the data to look at the LA selected.
            filter_data_lsoa = data_lsoa[data_lsoa.lad19nm == la_selection]
            lsoas_to_plot = list(lsoa_data[lsoa_data.lad19nm == la_selection].lsoa11nm)

            # The map shapefiles are stored by region, due to size constraints.
            # So we pull in the LSOA files based on the region selected.
            region_dict = dict(
                zip(
                    region_filter,
                    preprocess_strings(pd.Series(region_filter)),
                )
            )
            geodata_lsoa = get_english_lsoa_shapefiles_2011(
                region_dict[region_selection]
            )

            # Creating the altair chart; colours, interactivity etc.
            lsoa_select = alt.selection_single(fields=["lsoa11nm"])
            color_lsoa = alt.condition(
                lsoa_select,
                alt.Color(
                    f"{iod_dict[iod_selection]}:O",
                    scale=colour_palettes[colour_choice],
                    title=f"{iod_selection}",
                    legend=alt.Legend(orient="top"),
                ),
                alt.value("lightgray"),
            )
            choro_lsoa = (
                alt.Chart(geodata_lsoa)
                .mark_geoshape(
                    stroke="black",
                )
                .transform_lookup(
                    lookup="properties.lsoa11nm",
                    from_=alt.LookupData(
                        filter_data_lsoa,
                        "lsoa11nm",
                        ["lsoa11cd", "lsoa11nm", "lad19cd", "lad19nm"] + iod_indices,
                    ),
                )
                .transform_filter(
                    alt.FieldOneOfPredicate(
                        field="properties.lsoa11nm", oneOf=lsoas_to_plot
                    )
                )
                .encode(
                    color=color_lsoa,
                    tooltip=[alt.Tooltip("lsoa11nm:N", title="LSOA")]
                    + [
                        alt.Tooltip(f"{ind}:O", title=name, format="1.2f")
                        for ind, name in zip(iod_indices, iod_tooltip)
                    ],
                    opacity=alt.condition(lsoa_select, alt.value(1), alt.value(0.2)),
                )
                .add_selection(lsoa_select)
                .project(type="identity", reflectY=True)
                .properties(width=500, height=500)
            )

            # Configurations for the choropleth map
            choro_lsoa_chart = choro_lsoa.configure_legend(
                labelLimit=0,
                titleLimit=0,
                titleFontSize=13,
                labelFontSize=13,
                symbolStrokeWidth=1.5,
                symbolSize=150,
            ).configure_view(strokeWidth=0)

            # Plotting the chart in altair
            st.altair_chart(
                choro_lsoa_chart,
                use_container_width=True,
            )


# This adds on the password protection
pwd = st.sidebar.text_input("Password:", type="password")
# st.secrets reads it in from the toml folder, and then runs the streamlit_iod function if the password matches.
if pwd == st.secrets["PASSWORD"]:
    streamlit_iod()
elif pwd == "":
    pass
else:
    st.error("Password incorrect. Please try again.")
