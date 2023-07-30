import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/Yash-Bari/dataset/main/Athlete.csv'
df = pd.read_csv(url)

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

def main():
    st.markdown(
        "# Olympic Athlete Information\n\n"
        "Explore details of Olympic athletes and their achievements!"
    )
    st.set_page_config(
        layout="wide",
        page_title="Olympic Athlete Information",
        page_icon=":runner:",
        initial_sidebar_state="expanded",
    )
    st.image("https://th.bing.com/th/id/OIP.W8FzzgXIKTGjKmHFYkdYnAAAAA?w=176&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", caption="MyOlympia", width=100)
    header_container = st.container()
    with header_container:
        st.markdown("<h1 style='text-align: center; font-size: 50px;'>Olympic Athlete Information</h1>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("Explore details of Olympic athletes and their achievements!")
        
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
