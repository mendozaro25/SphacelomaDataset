from ultralytics import YOLO
import cv2

class ObjectDetection:
    def __init__(self, model_path='yolov8n.pt', device='cpu'):
        self.model = YOLO(model_path).to(device)

    def detect_objects(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f'No se pudo leer la imagen: {image_path}')
        
        results = self.model.predict(image)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = f'{self.model.model.names[int(box.cls[0])]} {box.conf[0]:.2f}'
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow('Detecciones', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        ObjectDetection('runs/detect/train/weights/best.pt').detect_objects('./images/train/imagen42.jpg')
    except Exception as e:
        print(f'Error: {e}')
