# Usar imagen base ligera
FROM python:3.9-slim

# Instalar dependencias del sistema y librerías gráficas necesarias
RUN apt-get update && apt-get install -y \
    libgl1 \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el contenido de la carpeta app al contenedor
COPY ./app /app

# Copiar archivos de datos (plantillas, etc.)
COPY ./app/data /app/data

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
