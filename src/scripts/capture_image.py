from ultralytics import YOLO
import cv2 as cv

model = YOLO("../../data/models/model_epoch20.pt")

img = cv.imread("../data/fedex.webp")
if img is None:
    print("No se puede leer la imagen.")

results = model(img, verbose=False)[0]
results.show()
results.save(filename="result.jpg")
info = results.summary()[0]
print("Label:", info['name'])
print("Class:", info['class'])
print("Confidence:", info['confidence'])