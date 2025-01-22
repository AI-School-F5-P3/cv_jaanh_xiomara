import streamlit as st
from pathlib import Path
import sys
import cv2 as cv
import tempfile
from ultralytics import YOLO
from camera_input_live import camera_input_live

# Add the project root to the Python path
root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))

def capture_video(video="0"):
    model = YOLO("../../data/models/model_epoch20.pt")
    if video == "0":
        video = int(video)
    cap = cv.VideoCapture(video)
    stframe = st.empty()
    if not cap.isOpened():
        print("No se puede abrir el archivo.")
        exit()
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Fin del video o error al leer el frame.")
        try:
            results = model(frame, save=False, verbose=False)[0]
            box = results.boxes
            cls = int(box[0].cls[0])
            conf = float(box[0].conf[0])
            class_name = model.names[cls]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
            label = f'{class_name} {conf:.2f}'
            cv.putText(frame, label, (x1, y1 - 10), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            stframe.image(frame_rgb, channels="RGB")

        except Exception as e:
            print(f"Error: {e}")
            continue

    cap.release()

def page_video():
    video_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if video_file is not None:
        st.video(video_file)
        if st.button("Analyze Video"):
            st.info("Analysis in progress...")
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_file.read())
            capture_video(tfile.name)

def page_camera():
    start = st.button("Iniciar")
    stop = st.button("Stop")
    if start:
        st.warning("Camara encendida.")
        capture_video()
    elif stop:
        st.warning("Camara apagada.")


def main():
    st.title("Brand Detection System")
    st.write("Upload a video to detect and track brand logos")

    opt = st.sidebar.selectbox(
        "Escoge una opción",
        ("imagen", "video", "camara")
    )
    
    if opt == "imagen":
        pass
    elif opt == "video":
        page_video()
    elif opt == "camara":
        page_camera()
            
if __name__ == "__main__":
    main()
