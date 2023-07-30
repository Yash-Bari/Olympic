import pandas as pd
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

data = pd.read_csv("medals.csv")

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
st.image("https://th.bing.com/th/id/OIP.W8FzzgXIKTGjKmHFYkdYnAAAAA?w=176&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", caption="MyOlympia", width=100)
st.title("Olympic Medal Analysis")
st.subheader("Explore medal data for different countries and athletes")

st.sidebar.title("Instructions")
st.sidebar.markdown("""
    1. Use the dropdown to select a country.
    2. The app will display the medal tally for the selected country.
    3. Explore country-wise and athlete-wise medal analysis.
    4. Check the overall medal distribution.
""")

st.sidebar.header("Filter Options")
selected_country = st.sidebar.selectbox("Select Country", data["country_name"].unique(), index=0)

filtered_data = data[data["country_name"] == selected_country]

st.header("Medal Tally")
st.bar_chart(filtered_data["medal_type"].value_counts())

st.header("Country-wise Analysis")
country_medal_tally = filtered_data["medal_type"].value_counts().rename_axis('Medal Type').reset_index(name='Count')
st.dataframe(country_medal_tally, height=200)

st.header("Athlete-wise Analysis")
athlete_medal_tally = filtered_data.groupby("athlete_full_name")["medal_type"].value_counts().unstack().fillna(0)
st.bar_chart(athlete_medal_tally)

st.header("Overall Analysis")
overall_medal_tally = data["country_name"].value_counts()
st.bar_chart(overall_medal_tally)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Data Analysis</p>", unsafe_allow_html=True)
