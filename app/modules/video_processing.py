import cv2

def procesar_video(ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    if not cap.isOpened():
        print("❌ Error al abrir el vídeo.")
        return
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Aquí se podría agregar lógica de procesamiento, por ejemplo, guardar frames
    cap.release()
    print("✅ Vídeo procesado correctamente.")
