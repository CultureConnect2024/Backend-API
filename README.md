# Backend API

This is a FastAPI backend API for supporting a Machine Learning-based mobile application. The API provides endpoints for authentication, predictions, and user management. This project is designed to be deployed to Google Cloud Run.

Key Features:

- Authentication
- Predictions
- User Management 
- Blog Management
- Scalable Deployment (docker)

Technologies Used:
- python
- docker
- fastapi ( backend framework )

## How To Use

1. **Kloning Repositori**
   ```bash
   
   https://github.com/CultureConnect2024/Backend-API.git
   
   cd Backend-API
2. **Create Virtual ENV**
   ```bash
   python -m venv venv

3. **Activate the virtual env (gitbash)**
   ```bash
   source venv/Scripts/activate
   
4. **Activate the virtual env (cmd)**
   ```bash
   venv/Scripts/activate.bat

5. **Install the requirements**
   ```bash
   pip install -r requirements.txt

5. **Run Project**
   ```bash
   fastapi dev main.py
