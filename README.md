# AutoDeploy — CI/CD & Cloud Deployment System

AutoDeploy will be a hands-on DevOps portfolio project designed to build practical experience with the complete deployment lifecycle. It will demonstrate how code moves from development to a running application through automated testing, Docker-based CI/CD, cloud deployment, Linux server management, monitoring, and deployment automation.

## Overview

This is how system will work:

User push the code to GitHub → GitHub Actions automatically runs the tests → if the tests pass, Docker builds an image of the application → the image is pushed to a container registry → the cloud server pulls the new image and runs it → a health check confirms that the application is working correctly.

## Architecture

_Diagram to be added._

## Tech Stack

Python · FastAPI · PostgreSQL · SQLAlchemy · Linux · Bash · Git/GitHub · Docker · Docker Compose · GitHub Actions · Cloud VM · Container Registry

## Progress

- [x] Environment & Git (WSL2, Ubuntu, Git, GitHub)
- [x] FastAPI application

## Local Setup

The project will be developed and tested locally using a Python virtual environment and Uvicorn.

### 1. Create a Virtual Environment

```bash
python3 -m venv .venv
```

This creates an isolated Python environment named `.venv`. It keeps the project's dependencies separate from other Python projects on the system.

### 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

This activates the virtual environment so that Python and packages installed in the following steps are associated with this project.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all Python packages required by the project from the `requirements.txt` file.

### 4. Start the Application

```bash
uvicorn app.main:app --reload
```

This starts the FastAPI application using Uvicorn, a Python ASGI server. The `--reload` option automatically restarts the server when code changes are detected during development.

### 5. Open the API Documentation

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

This opens FastAPI's interactive Swagger UI, where the available API endpoints can be viewed and tested directly from the browser.


## Lessons Learned

_To be added._
