import os
import streamlit as st
import base64

# Function to get video files from the given folder
def get_video_files(folder_path):
    video_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".webm"):
            video_files.append(os.path.join(folder_path, filename))
    return video_files

# Main Streamlit app
def main():
    st.title("Olympic Videos")

    folder_path = "videos"  # Update the folder path here
    video_files = get_video_files(folder_path)

    # Define the thumbnail width and height
    thumbnail_width = 400
    thumbnail_height = 225

    # Custom CSS style for the page
    custom_style = """
    <style>
        body {
            background-color: #f2f2f2;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 30px;
        }
        h1 {
            color: #ff8000;
            text-align: center;
        }
        .video-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .video-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
        }
        .video-thumbnail {
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .video-description {
            font-size: 14px;
            color: #333;
            margin-bottom: 5px;
        }
    </style>
    """
    st.markdown(custom_style, unsafe_allow_html=True)


    for video_file in video_files:
        # Get the video name from the file path
        video_name = os.path.basename(video_file).split(".")[0]

        # Display the video thumbnail using st.image() with custom CSS class
        video_thumbnail = f"<video class='video-thumbnail' controls width='{thumbnail_width}' height='{thumbnail_height}'><source src='data:video/webm;base64,{base64.b64encode(open(video_file, 'rb').read()).decode()}' type='video/webm'></video>"
        st.markdown(f"<div class='video-card'>{video_thumbnail}<div class='video-description'>{video_name}</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
