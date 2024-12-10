import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL of the CSV file
csv_url = "https://raw.githubusercontent.com/ahlekses/ES-Herbarium/refs/heads/main/Species_clustering_classification.csv"

# Load the data
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data = load_data(csv_url)

# Title
st.title("Herbarium Species Clustering and Classification")

# Display dataset
st.header("Dataset")
st.dataframe(data)

# Layout: Settings above the graph
st.header("Visualization Settings and Graph")

# Settings for visualization
columns = data.columns.tolist()

col1, col2, col3 = st.columns(3)
with col1:
    x_axis = st.selectbox("X-Axis", columns)
with col2:
    y_axis = st.selectbox("Y-Axis", columns)
with col3:
    chart_type = st.selectbox("Chart Type", ["Scatter Plot", "Bar Chart"])

# Filter for the number of data points to display
num_points = st.number_input(
    "Number of data points to display (limit X-axis)", 
    min_value=1, 
    max_value=len(data), 
    value=min(len(data), 100), 
    step=1
)

filtered_data = data.head(int(num_points))

# Visualization
if chart_type == "Scatter Plot":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x=x_axis, y=y_axis)
    st.pyplot(plt)
elif chart_type == "Bar Chart":
    plt.figure(figsize=(10, 6))
    sns.barplot(data=filtered_data, x=x_axis, y=y_axis, ci=None)
    st.pyplot(plt)
