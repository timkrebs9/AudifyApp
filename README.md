# FastAPI Web App with Auth0

[![CodeQL](https://github.com/timkrebs9/AudifyApp/actions/workflows/codeql.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/codeql.yml)
[![Build and deploy Python app to Azure Web App - audityapp](https://github.com/timkrebs9/AudifyApp/actions/workflows/main_audityapp.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/main_audityapp.yml)

This application is a small demo on how to integrate Auth0 for authentication in a FastAPI web application.

## How to run the server

1. Clone this repository
    ```
    git clone https://github.com/bajcmartinez/fastapi-webapp-auth0.git && cd fastapi-webapp-auth0
    ```
2. Create a `.env` file from `.env.example` and populate the values from your Auth0 Application. Here is 
   ```
   cp .env.example .env
   ```

3. Create a virtual environment and install dependencies
   
   ```
   # Create a venv
   python3 -m venv venv 
   
   # Activate
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. Start the server

   ```
   uvicorn main:app --reload
   ```
   
5. Visit `http://localhost:8000`