# 🖼️ Detección de Objetos con YOLOv8

Este proyecto utiliza [YOLOv8](https://github.com/ultralytics/ultralytics) para la detección de objetos en imágenes.

---

## 📌 Características

✅ Implementación optimizada con `Ultralytics YOLOv8`  
✅ Detección de objetos en imágenes con bounding boxes  
✅ Uso de `OpenCV` para visualizar resultados  
✅ Compatible con `CPU` y `GPU`  

---

## 📥 Instalación

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2️⃣ Crear un entorno virtual (opcional pero recomendado)
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

---

## 🚀 Uso
Ejecuta el script para detectar objetos en una imagen:
```sh
python detect.py
```

### 📌 Personalización
- Cambia la ruta del modelo en:
  ```python
  ObjectDetection(model_path='ruta_al_modelo.pt')
  ```
- Modifica la ruta de la imagen en:
  ```python
  detector.detect_objects('ruta_a_la_imagen.jpg')
  ```

---

## 📂 Estructura del Proyecto
```bash
📦 tu-repo
├── 📂 images/          # Carpeta con imágenes de prueba
├── 📂 runs/            # Resultados del modelo
├── 📜 detect.py        # Código principal
├── 📜 requirements.txt # Dependencias del proyecto
├── 📜 README.md        # Este archivo
├── 📜 LICENSE          # Licencia MIT
└── 📜 .gitignore       # Archivos a ignorar en Git
```

---

## ⚖️ Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.



