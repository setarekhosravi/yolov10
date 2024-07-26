from ultralytics import YOLOv10

model = YOLOv10('yolov10s.pt')

model.info()

model.train(data="/home/setare/Vision/ultralytics/Quad.yaml", epochs=5, imgsz=640, batch = 16)