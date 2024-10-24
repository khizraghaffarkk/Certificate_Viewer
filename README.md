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

### 🔍 Here’s Your Gateway to the App Interface: 🔍
![Screenshot from 2024-10-25 02-29-36](https://github.com/user-attachments/assets/ea635f2c-100b-4824-b093-5da567224f8a)

![Screenshot from 2024-10-25 02-30-38](https://github.com/user-attachments/assets/b9e32d0b-91eb-431f-a055-5fbb8c0d77b6)

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


## 📜 Proudly Presenting My Credentials: These are all my certificates!
## 📜 Proudly Presenting My Credentials: These are all my certificates!

### Here are all my certificates that reflect my skills and accomplishments:

<div align="center">
    <img src="https://github.com/user-attachments/assets/a9b7c42e-2783-437a-934d-3d913b034d73" alt="1_Python_Demonstration" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/89d62895-13bc-4e51-ac46-2b93f8caf1fc" alt="2_AWS" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/972dc590-c1a0-4b32-9462-c76beccd79c8" alt="3_Neo cert" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/737067bd-792c-4604-88bf-bf7a41a6ab63" alt="4_Course-Certificate_Lab-Terraform-for-Beginners_Khizra pdf_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/2ab1cd96-86ad-4dda-aeeb-79c26e5d5df2" alt="5_5g introduction_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/035a5c22-658f-444c-bfd6-4dc6b82f4c56" alt="6_CertificateOfCompletion_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/1c07e1a1-c78e-4b16-baf0-4e815d063f0c" alt="7_Kubernetes Crash Course" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/7b91c5e4-a02e-4467-94f1-52b4dcb64522" alt="8_Docker Hands-On Practical Experience" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/d453ae12-d373-482b-a31a-c511bbcce667" alt="9_SQL Advanced Skill Assessment Test_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/1220f06a-fce8-403b-9d5b-65c4072a079a" alt="10_SQL Intermediate Skill Assessment Test_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/894b6ce0-cf41-4fd2-81d0-e6f62ca0a8b8" alt="11_SQL Basic Skill Assessment Test_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/2e2a3b8c-f4cb-4939-8dc6-71311179b7ca" alt="12_Automation With Selenium Web Driver and TestNg_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/8ac535e5-4f95-47d9-9043-e75ca0679269" alt="13_API Testing and Basic Overview of JMETER _page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/7fd9aadb-b134-43ae-9260-7f443eeec6ec" alt="14_API Testing with Postman_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/8cc9bf5b-12ba-4594-aa39-2ae490d742b5" alt="15_Automation Using Cypress – Part II_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/1c628bdf-e267-4ebe-8499-b967fd9cdb46" alt="16_Test Automation with Cypress_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
    <img src="https://github.com/user-attachments/assets/df03faed-e3ef-47d3-af9e-cd69e50d8610" alt="17_Web and Graphic Design Course_page-0001" style="width: 300px; border-radius: 10px; margin: 10px;">
</div>
