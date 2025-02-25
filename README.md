# ContentPilot

ContentPilot is an automation platform designed for photographers and influencers. It leverages artificial intelligence to enhance and optimize workflows such as image import and selection, basic editing, content organization, and generating suggestions through the OpenAI API.

---

## Features

- **Interactive Menu:** Navigate through various functionalities of the platform.
- **Face Detection:** Uses `face_recognition` to identify faces in images.
- **AI-Powered Suggestions:** Integrates with OpenAI to generate suggestions (e.g., image titles).
- **Video Processing:** Provides basic support for video processing using OpenCV.
- **Secure Environment Variables:** Utilizes `python-dotenv` to load keys and configurations from an `.env` file.
- **Docker & Docker Compose:** An isolated runtime environment optimized for building dependencies like dlib.
- **Automated Testing:** Unit tests with pytest to validate key functionalities.

---

## Project Structure

```
ContentPilot/
├── .env.example                # Template for environment variables
├── .gitignore                  # Ignores sensitive files (.env, data, etc.)
├── LICENSE                     # MIT License
├── Dockerfile                  # Optimized Docker image
├── docker-compose.yml          # Container and volume configuration
├── README.md                   # Project documentation
├── app/
│   ├── main.py                 # Main menu and .env loader
│   ├── modules/                # Feature modules
│   │   ├── importacion_seleccion.py
│   │   ├── face_detection.py
│   │   ├── video_processing.py
│   │   └── ia_api.py           # Module to interact with OpenAI
│   ├── data/                   # Databases, templates, etc.
│   │   └── plantillas.json
│   └── requirements.txt        # Python dependencies
└── tests/                      # Unit tests
    ├── test_menu.py
    └── test_face_detection.py
```

---

## Requirements

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- (Optional) NVIDIA GPU with installed drivers for accelerated AI processing.
- An account with [OpenAI](https://platform.openai.com/signup) to obtain your API key.

---

## Setting Up Environment Variables

1. Copy the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit the `.env` file and add your API key:
   ```dotenv
   API_KEY=your_opensai_api_key
   ```
> **Note:** Ensure you add the `.env` file to your `.gitignore` to avoid exposing your keys.

---

## Local Installation and Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/asmuller-crypto/ContentPilot.git
   cd ContentPilot
   ```
2. **Build and run the container using Docker Compose:**
   ```bash
   docker-compose up --build
   ```
3. **Interact with the application:**
   - The application will run in your terminal. Follow the menu instructions to test each functionality.

---

## Running Tests

To execute the unit tests (using pytest), run:
```bash
docker-compose run app pytest tests/
```
Alternatively, if you work locally outside of Docker:
```bash
pytest tests/
```

---

## Deploying on Google Cloud Run

Follow these steps to deploy ContentPilot on Google Cloud Run:

1. **Set up your project on Google Cloud:**
   - Create a new project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the following APIs: Cloud Run API, Cloud Build API, and (optionally) Artifact Registry API.

2. **Install and configure the Google Cloud SDK:**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```
   Replace `YOUR_PROJECT_ID` with your project ID.

3. **Build the Docker image:**
   ```bash
   docker build -t gcr.io/YOUR_PROJECT_ID/contentpilot:latest .
   ```
4. **Authenticate Docker with Google Container Registry:**
   ```bash
   gcloud auth configure-docker
   ```
5. **Push the image:**
   ```bash
   docker push gcr.io/YOUR_PROJECT_ID/contentpilot:latest
   ```
6. **Deploy on Cloud Run:**
   ```bash
   gcloud run deploy contentpilot \
     --image gcr.io/YOUR_PROJECT_ID/contentpilot:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```
   You can change `us-central1` to your preferred region.

Once deployment is complete, you will receive a public URL to access your application.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your modifications and submit a pull request.
4. Ensure you include tests for any new functionality or fixes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Additional Notes

- **Error Handling:**  
  Specific error handling has been added for common issues such as image loading errors or connection issues with OpenAI.
  
- **Docker Optimization:**  
  A lightweight base image is used, and unnecessary caches are removed to optimize the Docker image size.
  
- **API Integrations:**  
  In the future, it is recommended to use official APIs (e.g., Instagram Graph API) for greater stability and security.

---

