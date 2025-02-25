import face_recognition

def detectar_rostros(ruta_imagen):
    try:
        image = face_recognition.load_image_file(ruta_imagen)
        face_locations = face_recognition.face_locations(image)
        return len(face_locations) > 0
    except FileNotFoundError as e:
        print(f"❌ Archivo no encontrado: {e}")
        return False
    except Exception as e:
        print(f"❌ Error al procesar la imagen: {e}")
        return False
