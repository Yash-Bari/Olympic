import streamlit as st
import pandas as pd

# Load the CSV file
url = 'https://raw.githubusercontent.com/Yash-Bari/dataset/main/Athlete.csv'
df = pd.read_csv(url)

# Function to display athlete details on click
def display_details(row):
    st.image(row['Athlete_image_url'], width=150, output_format='PNG')
    st.header(row['Athlete_name'])
    st.image(row['Team image_url'], width=50, output_format='PNG')
    st.subheader(row['Team'])
    st.markdown(f"**Sport:** {row['Sport']}")
    st.markdown(f"**Biography:** {row['Biography']}")
    st.image(row['Event image_url'], width=200, output_format='PNG')
    st.subheader(row['Event name'])
    st.markdown(f"**Medal:** {row['Medal']}")

# Main Streamlit app
def main():
    st.set_page_config(
        layout="wide",
        page_title="Olympic Athlete Information",
        page_icon=":runner:",
        initial_sidebar_state="expanded",
    )

    # Add a smaller header and separation
    header_container = st.container()
    with header_container:
        st.markdown("<h1 style='text-align: center; font-size: 50px;'>Olympic Athlete Information</h1>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("Explore details of Olympic athletes and their achievements!")

    # Display athlete information with minimize feature
    for _, row in df.iterrows():
        col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
        with col1:
            st.image(row['Athlete_image_url'], width=100, output_format='PNG', caption=row['Athlete_name'])
        with col2:
            st.image(row['Team image_url'], width=50, output_format='PNG', caption=row['Team'])
        with col3:
            with st.expander("More details"):
                display_details(row)
        with col4:
            st.empty()
            st.empty()
            st.empty()

if __name__ == '__main__':
    main()
