# 🚀 Flask CI/CD Pipeline with Jenkins, Docker & Kubernetes

<p align="center">
  <strong>From Source Code to a Kubernetes Deployment — Automated with Jenkins</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white" alt="Jenkins">
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes&logoColor=white" alt="Kubernetes">
</p>

---

## 📌 Project Overview

This project demonstrates an end-to-end CI/CD workflow for a Python Flask web application, using Jenkins to automate the build, image publishing, and deployment process.

The application is containerized with Docker, published to Docker Hub, and deployed to a local Kubernetes cluster running on Minikube.

The Flask application serves a custom-designed status page that demonstrates the application is responding successfully.

**The goal:** understand how source code moves through a practical DevOps delivery pipeline, from GitHub to a running application in Kubernetes.

## 🏗️ Architecture

```text
           Developer
               |
               v
        +--------------+
        |    GitHub    |
        | Source Code  |
        +--------------+
               |
               v
        +--------------+
        |    Jenkins   |
        |  CI/CD       |
        +--------------+
               |
               v
        +--------------+
        | Docker Build |
        | Image + Tag  |
        +--------------+
               |
               v
        +--------------+
        |  Docker Hub  |
        | Image Registry|
        +--------------+
               |
               v
        +--------------+
        |  Kubernetes  |
        |   Minikube   |
        +--------------+
               |
         +-----+-----+
         |           |
         v           v
   +-----------+ +-----------+
   |  Pod 1    | |  Pod 2    |
   | Flask App | | Flask App |
   +-----------+ +-----------+
         \           /
          \         /
           +-------+
           |Service|
           +-------+
               |
               v
       Browser / Port Forward
         localhost:8081
```

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Lightweight web framework |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Jenkins | CI/CD pipeline automation |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes environment |
| kubectl | Kubernetes command-line management |
| Git & GitHub | Source control and repository hosting |
| YAML | Kubernetes resource configuration |

## 📂 Repository Structure

```text
nti-jenkins-k8s/
├── hello.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

### File Responsibilities

- **`hello.py`** — Flask application and responsive HTML status page.
- **`requirements.txt`** — Python dependencies.
- **`Dockerfile`** — Instructions for building the application image.
- **`Jenkinsfile`** — Declarative pipeline defining the CI/CD stages.
- **`k8s/deployment.yaml`** — Kubernetes Deployment configuration, including two desired replicas.
- **`k8s/service.yaml`** — ClusterIP Service that provides internal access to the application Pods.

## 🔄 CI/CD Pipeline

The Jenkins pipeline is organized into the following stages:

### 1. Source Checkout

Retrieves the project source code from the GitHub `main` branch.

### 2. Build Docker Image

Builds a Docker image using the repository's Dockerfile and tags it with the Jenkins build number.

Example:

```bash
docker build -t new-app-nti:1 .
```

### 3. Push Image to Docker Hub

Authenticates using Jenkins-managed credentials, tags the image with the Docker Hub repository name, and pushes it to the registry.

Example:

```bash
docker tag new-app-nti:1 USERNAME/new-app-nti:1
docker push USERNAME/new-app-nti:1
```

### 4. Deploy to Kubernetes

Updates the image reference in the Kubernetes Deployment manifest, applies the Deployment and Service configurations, and waits for the rollout to complete.

The pipeline also checks the resulting Pods and Service.

A successful image push does not automatically guarantee a successful deployment, so the rollout status check is an important validation step.

## ☸️ Kubernetes Configuration

The Deployment declares two desired replicas:

```yaml
spec:
  replicas: 2
```

Kubernetes manages the Pods according to the declared configuration.

The Service uses `ClusterIP`, exposing the application internally within the cluster on port `5000`.

To access the application locally, Kubernetes port forwarding is used.

## 🚀 Accessing the Application

After the pipeline completes successfully, verify the Deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Check the rollout:

```bash
kubectl rollout status deployment/new-app-nti
```

Forward a local port to the Service:

```bash
kubectl port-forward service/new-app-nti 8081:5000
```

Open the application in your browser:

**http://localhost:8081**

Keep the terminal running while using the port-forward connection.

## 🔐 Credentials & Configuration

The pipeline uses Jenkins credentials rather than hardcoding Docker Hub authentication details in the Jenkinsfile.

The Jenkins runtime is configured with access to Docker and a Kubernetes `kubeconfig` file for communicating with the Minikube cluster.

For a production environment, credentials and Kubernetes access should follow least-privilege principles. Access to the Docker socket can provide extensive control over the Docker host and should be handled carefully.

## 🧪 Troubleshooting & Lessons Learned

This project also provided hands-on practice diagnosing common deployment problems.

| Problem | Root cause / lesson |
|---|---|
| Jenkins pipeline syntax error | Declarative stages must be nested correctly inside `stages`. |
| Unexpected backtick character | Markdown code fences must not be copied into executable source files. |
| Git branch checkout failure | The configured branch must match the actual repository branch. |
| Kubernetes rollout timeout | A deployment can fail even after an image has been built and pushed successfully. |
| `CrashLoopBackOff` | Inspect application logs to identify why the container exits. |
| Python `SyntaxError` | The container image included Markdown formatting in `hello.py` instead of valid Python code. |

Useful diagnostic commands:

```bash
kubectl get pods
kubectl describe pod POD_NAME
kubectl logs POD_NAME
kubectl rollout status deployment/new-app-nti
```

## 🎯 Key Learning Outcomes

- Built and containerized a Python Flask application.
- Created a Jenkins Declarative Pipeline.
- Automated Docker image builds and publishing.
- Used Jenkins-managed credentials for registry authentication.
- Deployed an application to Kubernetes using YAML manifests.
- Configured a Deployment with two desired replicas.
- Exposed the application through a Kubernetes Service.
- Configured Jenkins to communicate with a local Minikube cluster.
- Practiced troubleshooting CI/CD failures using Jenkins logs and Kubernetes diagnostics.

## 🔮 Potential Improvements

Future improvements could include:

- Automated builds triggered by GitHub webhooks.
- Automated application tests before publishing images.
- Image vulnerability scanning.
- Kubernetes readiness and liveness probes.
- Resource requests and limits.
- Separate development and production environments.
- Helm-based deployments.
- A dedicated Kubernetes ServiceAccount with restricted permissions.
- Deployment notifications and rollback strategies.

## 👨‍💻 Author

**Ahmed Farouk**

DevOps & Cloud Engineering Learner

This project was built as part of my hands-on journey into DevOps automation, containerization, and Kubernetes.

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.
