import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv(r"Team_medal.csv")
st.image("https://th.bing.com/th/id/OIP.W8FzzgXIKTGjKmHFYkdYnAAAAA?w=176&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", caption="MyOlympia", width=100)
st.header('Olympic Medals Dashboard')
st.subheader('This app allows you to explore Olympic medals data for different sports and years.')

selected_sport = st.sidebar.selectbox('Select a sport', df['Sport'].unique(), help='Select a sport to view the medal distribution.')
selected_year = st.sidebar.selectbox('Select a year', df['Year'].unique(), help='Select a year to view the medal distribution.')

filtered_data = df[(df['Sport'] == selected_sport) & (df['Year'] == selected_year)]

if filtered_data.empty:
    st.warning("No data available for the selected filters.")
else:
    st.markdown('---')
    st.header('Medal Distribution by Team')
    st.subheader('Bar Chart')
    fig, ax = plt.subplots(figsize=(8, 4))
    filtered_data.plot.bar(x='Team', y=['Gold', 'Silver', 'Bronze'], stacked=True, ax=ax)
    ax.set_ylabel('Number of Medals')
    ax.set_xlabel('Team')
    st.pyplot(fig)

    st.markdown('---')
    st.header('Overall Medal Distribution')
    st.subheader('Pie Chart')
    fig, ax = plt.subplots(figsize=(6, 6))
    filtered_data[['Gold', 'Silver', 'Bronze']].sum().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)

    st.markdown('---')
    st.header('Medal Trend for Each Team')
    st.subheader('Line Chart')
    fig, ax = plt.subplots(figsize=(8, 4))
    filtered_data.plot.line(x='Team', y=['Gold', 'Silver', 'Bronze'], marker='o', ax=ax)
    ax.set_ylabel('Number of Medals')
    ax.set_xlabel('Team')
    ax.grid()
    st.pyplot(fig)

show_table = st.sidebar.checkbox('Show Data in Table', help='Check this box to display the raw data in a table format.')
if show_table:
    st.header('Data Table')
    st.dataframe(filtered_data)

st.sidebar.markdown('---')
st.markdown('---')

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Data Analysis</p>", unsafe_allow_html=True)
