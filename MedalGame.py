import pandas as pd
import streamlit as st
import altair as alt
from collections import Counter

st.set_page_config(page_title='Olympic Analysis', page_icon=':trophy:', layout="wide")

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
        .header {
            font-size: 36px;
            text-align: center;
            margin-bottom: 24px;
        }
        .description {
            font-size: 18px;
            text-align: center;
            margin-bottom: 12px;
        }
        .section-separator {
            margin-top: 36px;
            margin-bottom: 12px;
            border-top: 2px solid #ccc;
        }
    </style>
""", unsafe_allow_html=True)

medal_data = pd.read_csv("medals.csv")

game_data = pd.read_csv("athlete_events.csv")

st.title("Olympic Games Analysis")
st.markdown("<p class='description'>Explore Olympic Games data with this interactive application.</p>", unsafe_allow_html=True)

analysis_option = st.sidebar.radio("Select Analysis Option", ("Medal Analysis", "Game Analysis"))

if analysis_option == "Medal Analysis":

    st.sidebar.header("Choose Options")
    selected_country = st.sidebar.selectbox("Select Country", medal_data["country_name"].unique())

    filtered_medal_data = medal_data[medal_data["country_name"] == selected_country]

    medal_tally = Counter(filtered_medal_data["country_name"])

    st.markdown("<h1 class='header'>Medal Tally</h1>", unsafe_allow_html=True)

    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.bar_chart(medal_tally, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-separator'></div>", unsafe_allow_html=True)

    st.header("Country-wise Analysis")
    country_group = filtered_medal_data.groupby("country_name")
    country_medal_tally = country_group["medal_type"].value_counts().unstack().fillna(0)
    st.bar_chart(country_medal_tally, use_container_width=True)

    st.subheader("Country-wise Medal Tally (Table)")
    st.dataframe(country_medal_tally)

    st.markdown("<div class='section-separator'></div>", unsafe_allow_html=True)

    st.header("Athlete-wise Analysis")
    athlete_group = filtered_medal_data.groupby("athlete_full_name")
    athlete_medal_tally = athlete_group["medal_type"].value_counts().unstack().fillna(0)
    st.bar_chart(athlete_medal_tally, use_container_width=True)

    st.subheader("Athlete-wise Medal Tally (Table)")
    st.dataframe(athlete_medal_tally)

    st.markdown("<div class='section-separator'></div>", unsafe_allow_html=True)

    st.header("Overall Analysis")
    overall_medal_tally = medal_data["country_name"].value_counts()
    st.bar_chart(overall_medal_tally, use_container_width=True)

    st.subheader("Overall Medal Tally (Table)")
    st.dataframe(overall_medal_tally)

else:
    st.sidebar.header("Choose Options")
    sport = st.sidebar.selectbox("Select a sport", game_data["Sport"].unique())
    gender = st.sidebar.selectbox("Select a gender", game_data["Sex"].unique())

    filtered_game_data = game_data[(game_data["Sport"] == sport) & (game_data["Sex"] == gender)]

    st.markdown("<h1 class='header'>Game Analysis</h1>", unsafe_allow_html=True)

    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)

    st.write(f"Number of athletes in {sport} ({gender}): {len(filtered_game_data)}")
    st.dataframe(filtered_game_data.drop(columns=['ID', 'image']))

    chart = alt.Chart(filtered_game_data).mark_bar().encode(
        x=alt.X("NOC", title="Country"),
        y=alt.Y("count()", title="Number of athletes"),
        color=alt.Color("NOC", legend=None),
        tooltip=["NOC", "count()"]
    ).properties(
        width=700, 
        height=400
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Data Analysis</p>", unsafe_allow_html=True)
