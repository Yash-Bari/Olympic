import pandas as pd
import streamlit as st

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(r"C:\Users\Yash\OneDrive\Desktop\Hackthon\csv\medals.csv")

# Set the page title and favicon
st.set_page_config(page_title='Medal Analysis', page_icon=':trophy:')

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
    </style>
""", unsafe_allow_html=True)

# Sidebar for filtering options
st.sidebar.header("Choose Options")
selected_country = st.sidebar.selectbox("Select Country", data["country_name"].unique())

# Filter the data based on the selected country
filtered_data = data[data["country_name"] == selected_country]

# Medal Tally
medal_tally = filtered_data["medal_type"].value_counts()
st.header("Medal Tally")
st.bar_chart(medal_tally)

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
st.markdown("<p style='text-align: center; color: gray;'>Made with :heart: by Your Name</p>", unsafe_allow_html=True)
