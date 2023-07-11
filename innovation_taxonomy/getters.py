"""Loads in the data necessary to label and name Wikipedia entities with our taxonomy
"""
import polars as pl


def get_taxonomy(alg: str = "cooccurrence") -> pl.DataFrame:
    """loads a taxonomy table from the data folder (downloaded from https://nesta-open-data.s3.eu-west-2.amazonaws.com/innovation_taxonomy/) generated using the specified algorithm

    Args:
        alg (str, optional): algorithm used to generate the taxonomy. Defaults to "cooccurrence" - the taxonomy we found most useful based on the process described in the Medium article. Other options are "centroids" and "imbalanced" to load the taxonomies generated using the other algorithms described.

    Returns:
        pl.DataFrame: polars dataframe containing the entire taxonomy. The taxonomy is nested, and the nesting structure is represented using "_". The top level ("Level_1") is represented as a single integer (ex: 0). All of the groups at the next level within group 0 would be represented as 0_1, 0_2, 0_3, etc.

        In many cases a grouping did not break down into all 5 levels (as described in the article). In this case, the previous level is cascaded throughout the taxonomy.

        The columns in the dataframe are:
            Level_1: "disciplines" - represented by a single integer (ex: 0).
            Level_2: "domains" - represented by up to two integers separated by _ (ex: 0_1)
            Level_3: "areas" - represented by up to three integers separated by _ (ex: 0_1_1)
            Level_4: "topics" - represented by up to four integers separated by _ (ex: 0_1_1_1)
            Level_5: "subtopics" - represented by up to five integers separated by _ (ex: 0_1_1_1_1)
            "Entity": the Wikipedia entity being categorised
    """
    if alg == "cooccurrence":
        return pl.read_parquet("data/taxonomies/community_detection.parquet")
    elif alg == "centroids":
        return pl.read_parquet("data/taxonomies/semantic_centroids.parquet")
    elif alg == "imbalanced":
        return pl.read_parquet("data/taxonomies/semantic_imbalanced.parquet")
