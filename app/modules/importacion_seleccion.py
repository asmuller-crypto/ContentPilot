import os
import face_recognition
import openai

def importar_y_seleccionar(api_key):
    print("🔍 Importando y seleccionando fotos/vídeos...")
    
    # Configurar la API Key para OpenAI
    openai.api_key = api_key

    # Ejemplo: Uso de ChatGPT para sugerir un título
    prompt = "Sugiere un título para una foto de paisaje."
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        sugerencia = response.choices[0].text.strip()
        print(f"📝 Sugerencia de título: {sugerencia}")
    except openai.error.OpenAIError as e:
        print(f"❌ Error al obtener sugerencia de OpenAI: {e}")

    # Solicitar la ruta de la carpeta con imágenes
    folder_path = input("Introduce la ruta de la carpeta con imágenes: ").strip()
    if not os.path.isdir(folder_path):
        print("⚠️ La ruta especificada no existe.")
        return

    # Procesar cada imagen en la carpeta
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, file)
            try:
                image = face_recognition.load_image_file(file_path)
                face_locations = face_recognition.face_locations(image)
                if face_locations:
                    print(f"✅ Rostro detectado en {file}")
                else:
                    print(f"❌ No se detectaron rostros en {file}")
            except Exception as e:
                print(f"❌ Error procesando {file}: {e}")
