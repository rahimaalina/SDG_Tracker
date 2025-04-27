import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('sdg_data.csv')
    return df

# Load the data
df = load_data()

# Streamlit App
st.title("🌍 UN Sustainable Development Goals Dashboard")
st.write("Small project showing SDG progress across countries.")

# Sidebar filters
country = st.sidebar.selectbox("Select a Country", df['Country'].unique())

# Main chart
filtered_df = df[df['Country'] == country]

fig = px.bar(filtered_df, x='Goal', y='Progress', color='Goal', 
             title=f"SDG Progress for {country} in 2020",
             labels={"Progress": "% Progress"})
st.plotly_chart(fig)

# Data table
st.subheader("Raw Data")
st.dataframe(filtered_df)
