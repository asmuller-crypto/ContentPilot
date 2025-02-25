from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

def mostrar_menu():
    print("""
🚀 ContentPilot - Menú Principal 🚀
1. Ingresar API Key
2. Importar fotos y seleccionar (detección de rostros con IA)
3. Salir
""")

def main():
    api_key = os.getenv("API_KEY")
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            api_key = input("Introduce tu API Key de OpenAI/DeepSeek: ").strip()
            os.environ["API_KEY"] = api_key
            print("✅ API Key guardada correctamente.")
        elif opcion == "2":
            if not api_key:
                print("⚠️ Por favor, ingresa tu API Key primero.")
                continue
            from modules.importacion_seleccion import importar_y_seleccionar
            importar_y_seleccionar(api_key)
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
