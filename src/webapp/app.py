import streamlit as st
from pathlib import Path
import sys

# Add the project root to the Python path
root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))

def main():
    st.title("Brand Detection System")
    st.write("Upload a video to detect and track brand logos")
    
    # File uploader
    video_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    
    if video_file is not None:
        st.video(video_file)
        
        if st.button("Analyze Video"):
            st.info("Analysis in progress...")
            # Add detection logic here
            
if __name__ == "__main__":
    main()
