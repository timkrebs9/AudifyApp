---
name: Audify
description: "A minimal sample app that uses Auth0, FastApi and Azure App Services"
languages:
- python
- javascript
- html
- css
-azurecli
products:
- azure
- azure-app-service
- auth0
---

# Audify Web App

## Description
This is the sample FastAPI application for deploying FastAPI apps to Azure App Service with Auth0 authentication. The application demonstrates a minimal setup required to get a FastAPI web app up and running and integrated with Azure services.

![Python](https://img.shields.io/badge/python-3.9+-blue)
[![pre-commit](https://github.com/timkrebs9/AudifyApp/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/pre-commit.yml)
[![CodeQL](https://github.com/timkrebs9/AudifyApp/actions/workflows/codeql.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/codeql.yml)
[![Build and deploy](https://github.com/timkrebs9/AudifyApp/actions/workflows/main_audifywebapp.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/main_audifywebapp.yml)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://codespaces.new/timkrebs9/AudifyApp)
[![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/timkrebs9/AudifyApp)

## Local Testing

### Install the requirements
```bash
pip install -r requirements-dev.txt
```

### Install the pre-commit check
```bash
pre-commit install
```

### Start the application
```bash
uvicorn main:app --reload
```

### Example call
Open http://127.0.0.1:8000/ in your browser to access the app locally.

## Build and Run the Image Locally

### Build the image
```bash
docker build --tag audifywebapp .
```

### Run the image in a Docker container
```bash
docker run --detach --publish 3100:3100 audifywebapp
```
Open http://localhost:3100 in your browser to see the web app running locally.

## Deployment to Azure

### Login into Azure Account
```bash
az login
```

### Create a Resource Group and Azure Container Registry
```bash
az group create --name rg-audifywebapp --location eastus
az acr create --resource-group rg-audifywebapp --name audifywebapp --sku Basic --admin-enabled true
```

### Build the Image in Azure Container Registry
```bash
az acr build --resource-group rg-audifywebapp --registry audifywebapp --image audifywebapp:latest .
```

### Deploy Web App to Azure
```bash
az appservice plan create --name webplan --resource-group rg-audifywebapp --sku B1 --is-linux
az webapp create --resource-group rg-audifywebapp --plan webplan --name audifywebapp --deployment-container-image-name audifywebapp.azurecr.io/audifywebapp:latest
```

## Make Updates and Redeploy
After making code changes, redeploy to App Service with the following commands:
```bash
az acr build --resource-group rg-audifywebapp --registry audifywebapp --image audifywebapp:latest .
az webapp update --name audifywebapp --resource-group rg-audifywebapp --docker-registry-server-password <$ACR_PASSWORD> --deployment-container-image-name audifywebapp.azurecr.io/audifywebapp:latest
```

## Contributing
We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit contributions to this project.

## Issues
If you encounter any issues or have feature suggestions, please file them in the [issues section](https://github.com/timkrebs9/AudifyApp/issues) of this repository.

## Changelog
See the [CHANGELOG.md](CHANGELOG.md) for details on changes and updates made to the project.

## Next Steps

This is the sample FastAPI application for the Azure Quickstart [Deploy a Python (Django, Flask or FastAPI) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

Sample applications are available for the other frameworks here:
- Django [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart)
- Flask [https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart)

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).


To learn more about FastAPI, visit [FastAPI documentation](https://fastapi.tiangolo.com/).
