import pandas as pd
import streamlit as st
import altair as alt
from collections import Counter

# Set the page title and favicon
st.set_page_config(page_title='Olympic Analysis', page_icon=':trophy:')

# Add custom CSS styles
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
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

# Read the medal CSV file into a Pandas DataFrame
medal_data = pd.read_csv("medals.csv")

# Read the game CSV file into a Pandas DataFrame
game_data = pd.read_csv("athlete_events.csv")

# Title
st.title("Olympic Games Analysis")

# Sidebar for choosing the analysis option
analysis_option = st.sidebar.radio("Select Analysis Option", ("Medal Analysis", "Game Analysis"))

if analysis_option == "Medal Analysis":
    # Sidebar for filtering options
    st.sidebar.header("Choose Options")
    selected_country = st.sidebar.selectbox("Select Country", medal_data["country_name"].unique())

    # Filter the medal data based on the selected country
    filtered_medal_data = medal_data[medal_data["country_name"] == selected_country]

    # Medal Tally
    medal_tally = Counter(filtered_medal_data["country_name"])

    # Render the HTML heading with custom CSS class
    st.markdown("<h1 class='header'>Medal Tally</h1>", unsafe_allow_html=True)

    # Render the bar chart with a custom CSS class
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.bar_chart(medal_tally)
    st.markdown("</div>", unsafe_allow_html=True)

    # Country-wise analysis
    st.header("Country-wise Analysis")
    country_group = filtered_medal_data.groupby("country_name")
    country_medal_tally = country_group["medal_type"].value_counts().unstack().fillna(0)
    st.bar_chart(country_medal_tally)

    st.subheader("Country-wise Medal Tally (Table)")
    st.dataframe(country_medal_tally)

    # Athlete-wise analysis
    st.header("Athlete-wise Analysis")
    athlete_group = filtered_medal_data.groupby("athlete_full_name")
    athlete_medal_tally = athlete_group["medal_type"].value_counts().unstack().fillna(0)
    st.bar_chart(athlete_medal_tally)

    st.subheader("Athlete-wise Medal Tally (Table)")
    st.dataframe(athlete_medal_tally)

    # Overall analysis
    st.header("Overall Analysis")
    overall_medal_tally = medal_data["country_name"].value_counts()
    st.bar_chart(overall_medal_tally)

    st.subheader("Overall Medal Tally (Table)")
    st.dataframe(overall_medal_tally)

else:
    # Sidebar for filtering options
    st.sidebar.header("Choose Options")
    sport = st.sidebar.selectbox("Select a sport", game_data["Sport"].unique())
    gender = st.sidebar.selectbox("Select a gender", game_data["Sex"].unique())

    # Filter the game data
    filtered_game_data = game_data[(game_data["Sport"] == sport) & (game_data["Sex"] == gender)]

    # Render the HTML heading with custom CSS class
    st.markdown("<h1 class='header'>Game Analysis</h1>", unsafe_allow_html=True)

    # Render the bar chart with a custom CSS class
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)

    # Display the data
    st.write(f"Number of athletes in {sport} ({gender}): {len(filtered_game_data)}")
    st.dataframe(filtered_game_data)

    # Display the chart
    chart = alt.Chart(filtered_game_data).mark_bar().encode(
        x=alt.X("NOC", title="Country"),
        y=alt.Y("count()", title="Number of athletes"),
        color=alt.Color("NOC", legend=None),
        tooltip=["NOC", "count()"]
    ).properties(
        width=600,
        height=400
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with :heart: by Yash Bari</p>", unsafe_allow_html=True)
