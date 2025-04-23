# 🎟️ Django Ticket Booking System

A full-stack web application built with Django that allows users to register, browse shows, and book tickets seamlessly. The system is integrated with Docker and Jenkins for smooth development and deployment workflows.

---

## 🌟 Project Overview

This Ticket Booking System provides a streamlined experience for:

- User registration and authentication
- Show listings and management
- Ticket booking and order tracking
- Admin-side show management
- Session-based cart handling without Django Forms

---

## 🚀 Setup & Run Instructions

### Prerequisites
- Docker & Docker Compose
- Git

### 🐳 Running the App with Docker

To build and run the application using Docker:

bash : 
docker-compose up --build 

---

## 🛠️ Tech Stack Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (easily upgradeable to PostgreSQL/MySQL)
- **Version Control**: Git & GitHub
- **Containerization**: Docker, Docker Compose
- **CI/CD Pipeline**: Jenkins

---

## 🐳 Docker & CI/CD Notes

### Docker
- The application is fully containerized using a `Dockerfile` and `docker-compose.yml`.
- Docker ensures consistency across development, testing, and production environments.
- Run the app using:
  bash : 
  docker-compose up --build

  ---

  ### ⚙️ Jenkins CI/CD Pipeline

- Jenkins is used for Continuous Integration and Continuous Deployment (CI/CD).
- A `Jenkinsfile` defines the stages of the pipeline, which include:
  - **Build**: Docker image is built from the latest code.
  - **Test**: Run automated tests (if defined).
  - **Deploy**: Deploys the updated container to the target environment.
- Pipeline is automatically triggered via **GitHub Webhooks** on code push events.
- Ensures automated, reliable, and consistent deployment with every code change.



