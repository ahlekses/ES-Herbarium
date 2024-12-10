import streamlit as st
import pandas as pd  # pip install pandas


# CONFIGS

DATA_URL = "https://raw.githubusercontent.com/ahlekses/ES-Herbarium/refs/heads/main/Species_clustering_classification.csv"


st.title(f"Sales Dashboard", anchor=False)


@st.cache_data
def get_and_prepare_data(data):
    df = pd.read_csv(data).assign(
        date_of_sale=lambda df:(df["Area"]),
        month=lambda df: df["species"],
        year=lambda df: df["species_number"],
    )
    return df


df = get_and_prepare_data(data=DATA_URL)

# Calculate total revenue for each city and year, and then calculate the percentage change
city_revenues = (
    df.groupby(["species", "dbh"])["crown_width"]
    .sum()
    .unstack()
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] * 100)
)



# Display the data
st.bar_chart(filtered_data.set_index(filtered_data.columns[0])["sales_amount"])
