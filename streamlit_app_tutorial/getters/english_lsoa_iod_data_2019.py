import pandas as pd


def get_english_lsoa_iod_2019() -> pd.DataFrame:
    """Pulling in the English Lower Super Output Area (LSOA) IoD data for 2019; with the England regions, LA codes/names,
    LSOA codes/names and IoD deciles. The lower the decile, the
    higher the deprivation. See: https://opendatacommunities.org/def/concept/folders/themes/societal-wellbeing for the dataset.

    Returns:
        pd.DataFrame: Pandas dataframe with the English LSOA IoD data.
    """
    url = "https://raw.githubusercontent.com/nestauk/dap_medium_articles/dev/streamlit_app_tutorial/data/lsoa_english_iod_2019.csv"
    return pd.read_csv(url)
