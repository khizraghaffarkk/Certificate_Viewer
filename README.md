# 🎓 Certificate Viewer Application

Welcome to the **Certificate Viewer** app, a simple yet powerful tool built with Flask to display and filter certificates in different formats (PDF, JPG). Below, you’ll find all the steps to run this project locally, deploy it using Docker and Kubernetes, and even make it accessible through Ngrok and Vercel.

## ✨ Features

- 🚀 **Dynamic Content Serving**: Displays certificates based on format (PDF, JPG).
- 🎨 **Modern UI**: Responsive web design with Bootstrap 4.
- 🔍 **Filter Options**: Filter certificates by type (all, PDF, images).
- 🌐 **Multi-deployment Methods**: Deployed via Docker, Kubernetes, Ngrok, and Vercel.

## 🛠️ Prerequisites

To run this application, make sure you have the following installed:

- Python 3.x
- Flask
- Bootstap & JavaScript
- Docker
- Kubernetes (Minikube or any other Kubernetes environment)
- Ngrok (for port forwarding)
- Vercel (for serverless deployment)

## 🗂️ Directory Structure
```bash
.
├── app.py
├── templates
│   └── index.html
├── app
│   └── certificates  # Add your certificate files here
│   └── app.py
│   └── templates
│       └── index.html
├── Dockerfile
├── deployment.yaml
├── README.md
└── requirements.txt
└── vercel.json
```

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/khizraghaffarkk/certificate-viewer.git
   cd certificate-viewer
   ```

2. **Set up a virtual environment (optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install Flask
   ```

4. **Add your certificates to the app/certificates directory.**

## 🔧 Running the Application

**Start the Flask app:**

   ```bash
   python app.py
   ```
Access the app on your browser: Open `http://127.0.0.1:5000` to view the app.

## 🌐 Deployment
This application can be run locally and is deployed using docker, kubernetes, Ngrok and Vercel for testing and demonstration purposes.
### 🐳 Docker Deployment
#### Build and Run with Docker
You can containerize the app with Docker for easy deployment.

1. **Build the Docker image:**

   ```bash
   docker build -t certificate-viewer .
   ```
You need replace `khizraghaffarkk` with your docker hub username.
2. **Run the Docker container:**

   ```bash
   docker run -d -p 5000:5000 certificate-viewer
   ```

3. **Tag the image and push it to Docker Hub:**

   ```bash
   docker tag certificate-viewer:latest khizraghaffar/certificate-viewer:1.2
   docker push khizraghaffar/certificate-viewer:1.2
   ```

4. **Access the app:**
   ```bash
   Open `http://localhost:5000`.
   ```

### 🐳 Kubernetes Deployment
You can deploy this application in a Kubernetes cluster.

#### Create Kubernetes Deployment and Service
You can containerize the app with Docker for easy deployment.

1. **Create a Kubernetes Deployment:**

   ```bash
   kubectl apply -f deployment.yaml
   ```

2. **Expose the Deployment:**

   ```bash
   kubectl expose deployment certificate-viewer --type=LoadBalancer --port=5000
   ```

3. **Access the app:**
   ```bash
   Use the external IP provided by your Kubernetes cluster (e.g., Minikube or GKE).
   ```



## This application can be run locally and is deployed using **Ngrok** and **Vercel** for testing and demonstration purposes. 

### 🐳 Ngrok Deployment
To share your local app publicly, you can use Ngrok to forward the port.

1. **Start the Flask app locally:**

   ```bash
   python app.py
   ```

2. **Forward port 5000 using Ngrok:**

   ```bash
   ngrok http 5000
   ```

3. **Access the app with the Ngrok URL:**
   ```bash
   `(http://127.0.0.1:4040/inspect/http)`
   ```
   ![Screenshot from 2024-10-25 00-39-19](https://github.com/user-attachments/assets/b24c5ae5-f3ad-4002-abe0-4beb142e42ef)

   ![Screenshot from 2024-10-25 00-37-43](https://github.com/user-attachments/assets/9bcf644f-8ecc-4fc6-9645-1e778b8cbaf4)
   
   ![Screenshot from 2024-10-25 00-39-54](https://github.com/user-attachments/assets/9eb2b074-bc88-4804-87dd-85b6ef940486)

5. **Ngrok URL to inspect and check the status of application:**
   ```bash
   Ngrok will provide a public URL, e.g., `(https://94f7-87-100-227-126.ngrok-free.app/)`, which you can use to access your application.
   ```
#### When you close the terminal running Ngrok, the public URL will no longer be accessible!

### ▲ Vercel Deployment
You can deploy this Flask app on Vercel for a serverless, production-ready setup.

1. **Vercel Setup - Login to Vercel:**

   ```bash
   vercel login
   ```

2. **Deploy the app:**

   ```bash
   vercel #if deploy first time
   vercel --prod #if you modify you app, and need to rebuild it
   ```

3. **Access the app:**
   ```bash
   Vercel will provide a live URL for your app, such as, (https://certificate-viewer-74harxi4f-khizra-ghaffars-projects.vercel.app/).
   ```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a pull request.
