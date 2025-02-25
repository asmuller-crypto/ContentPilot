FROM python:3.9-slim

# Instalar dependencias del sistema necesarias para compilar dlib y otros paquetes
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar la aplicación y archivos de datos al contenedor
COPY ./app /app
COPY ./app/data /app/data

# Actualizar pip y luego instalar las dependencias de Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
