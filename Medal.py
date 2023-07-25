import pandas as pd
import streamlit as st

# Set Streamlit wide mode to display all data
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv("medals.csv")

# Add custom CSS styles
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .header {
            text-align: center;
            padding: 20px;
            background-color: #F5F5F5;
            margin-bottom: 20px;
        }
        .chart-container {
            display: flex;
            flex-direction: row;
            justify-content: space-around;
        }
        .chart-title {
            text-align: center;
            margin-bottom: 10px;
        }
        .sidebar-instructions {
            margin-bottom: 20px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Page header
st.title("Olympic Medal Analysis")
st.subheader("Explore medal data for different countries and athletes")

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.markdown("""
    1. Use the dropdown to select a country.
    2. The app will display the medal tally for the selected country.
    3. Explore country-wise and athlete-wise medal analysis.
    4. Check the overall medal distribution.
""")

# Sidebar for filtering options
st.sidebar.header("Filter Options")
selected_country = st.sidebar.selectbox("Select Country", data["country_name"].unique(), index=0)

# Filter the data based on the selected country
filtered_data = data[data["country_name"] == selected_country]

# Medal Tally
st.header("Medal Tally")
st.bar_chart(filtered_data["medal_type"].value_counts())

# Country-wise analysis
st.header("Country-wise Analysis")
country_medal_tally = filtered_data["medal_type"].value_counts().rename_axis('Medal Type').reset_index(name='Count')
st.dataframe(country_medal_tally, height=200)

# Athlete-wise analysis
st.header("Athlete-wise Analysis")
athlete_medal_tally = filtered_data.groupby("athlete_full_name")["medal_type"].value_counts().unstack().fillna(0)
st.bar_chart(athlete_medal_tally)

# Overall analysis
st.header("Overall Analysis")
overall_medal_tally = data["country_name"].value_counts()
st.bar_chart(overall_medal_tally)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Data Analysis</p>", unsafe_allow_html=True)
