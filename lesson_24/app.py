
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
from pathlib import Path

csv_path = Path(__file__).parent / "Advertising_F.csv"
df = pd.read_csv(csv_path)

# App title
st.title("Advertising Effectiveness Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

x_var = st.selectbox(
    "X axis",
    ["TV", "radio", "newspaper"]
)

# Scatter plot
fig = px.scatter(
    df,
    x=x_var,
    y="sales",
    labels={
        "TV": "TV Ad Spend",
        "radio": "Radio Ad Spend",
        "newspaper": "Newspaper Ad Spend"
    }
)

st.plotly_chart(fig)

# Bar chart
sales_per_city = df.groupby("City")["sales"].sum().reset_index()

fig = px.bar(
    sales_per_city,
    x="City",
    y="sales",
    labels={"sales": "Total Sales"}
)

st.plotly_chart(fig)

# Display dataset
st.dataframe(df)
