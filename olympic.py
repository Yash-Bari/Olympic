import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r"Team_medal.csv")

# Sidebar filters
selected_sport = st.sidebar.selectbox('Select a sport', df['Sport'].unique())
selected_year = st.sidebar.selectbox('Select a year', df['Year'].unique())

# Filter the data based on the selected filters
filtered_data = df[(df['Sport'] == selected_sport) & (df['Year'] == selected_year)]

if filtered_data.empty:
    st.write("No data available for the selected filters.")
else:
    # Bar chart
    st.subheader('Bar Chart')
    fig, ax = plt.subplots()
    filtered_data.plot.bar(x='Team', y=['Gold', 'Silver', 'Bronze'], ax=ax)
    ax.set_ylabel('Number of Medals')
    ax.set_xlabel('Team')
    st.pyplot(fig)

    # Pie chart
    st.subheader('Pie Chart')
    fig, ax = plt.subplots()
    filtered_data[['Gold', 'Silver', 'Bronze']].sum().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)

    # Line chart
    st.subheader('Line Chart')
    fig, ax = plt.subplots()
    filtered_data.plot.line(x='Team', y=['Gold', 'Silver', 'Bronze'], ax=ax)
    ax.set_ylabel('Number of Medals')
    ax.set_xlabel('Team')
    st.pyplot(fig)

    # Show data in table format
    show_table = st.checkbox('Show Data in Table')
    if show_table:
        st.subheader('Data Table')
        st.dataframe(filtered_data)
