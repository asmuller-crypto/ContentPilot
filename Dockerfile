FROM nvidia/cuda:12.2.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y python3-pip libgl1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]