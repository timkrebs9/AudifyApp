---
page_type: Application
description: "A minimal sample app that can be used to demonstrate deploying FastAPI apps to Azure App Service with Auth0 authentication."
languages:
- python
products:
- azure
- azure-app-service
- auth0
---

# Deploy a Python (FastAPI) web app to Azure App Service
![Python](https://img.shields.io/badge/python-3.9+-blue)
[![pre-commit](https://github.com/timkrebs9/AudifyApp/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/pre-commit.yml)
[![CodeQL](https://github.com/timkrebs9/AudifyApp/actions/workflows/codeql.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/codeql.yml)
[![Build and deploy](https://github.com/timkrebs9/AudifyApp/actions/workflows/main_audifywebapp.yml/badge.svg)](https://github.com/timkrebs9/AudifyApp/actions/workflows/main_audifywebapp.yml)


[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://codespaces.new/timkrebs9/AudifyApp)
[![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/timkrebs9/AudifyApp)


This is the sample FastAPI application for the Azure Quickstart [Deploy a Python (Django, Flask or FastAPI) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

Sample applications are available for the other frameworks here:
- Django [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart)
- Flask [https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart)

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).

## Local Testing

To try the application on your local machine:

### Install the requirements

`pip install -r requirements.txt`

### Start the application

`uvicorn main:app --reload`

### Example call

http://127.0.0.1:8000/

## Next Steps

To learn more about FastAPI, see [FastAPI](https://fastapi.tiangolo.com/).
