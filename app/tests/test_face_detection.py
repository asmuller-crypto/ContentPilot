from app.modules.face_detection import detectar_rostros

def test_deteccion_rostros():
    # Asegúrate de tener una imagen de prueba con rostros en tests/test_image.jpg
    assert detectar_rostros("tests/test_image.jpg") == True
