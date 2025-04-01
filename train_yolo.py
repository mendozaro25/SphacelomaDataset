from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='SphacelomaDataset.yaml', epochs=100, imgsz=640)
