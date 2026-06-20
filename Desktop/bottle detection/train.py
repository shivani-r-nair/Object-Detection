from ultralytics import YOLO

model = YOLO("yolov8n.pt")

try:
    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=2,
        workers=0
    )
except Exception as e:
    print("ERROR:", e)