import os
import configparser
from fastapi.templating import Jinja2Templates
from utils import to_pretty_json


import os
import configparser
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def load_secrets():
    """
    Loads configuration from Azure Key Vault or environment variables.
    Falls back to .config file if neither is set.
    """
    secrets = {}
    key_vault_name = "audifyapp-gzrvzu54wzzse"
    
    if key_vault_name:
        # Azure Key Vault is configured
        KVUri = f"https://{key_vault_name}.vault.azure.net"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)
        
        # Attempt to load secrets from Azure Key Vault
        try:
            print("Loading secrets from Azure Key Vault...")
            secrets['AUTH0_SESSION_SECRET'] = client.get_secret('auth0-session-secret').value
            secrets['AUTH0_DOMAIN'] = client.get_secret('auth0-domain').value
            secrets['AUTH0_CLIENT_ID'] = client.get_secret('auth0-client-id').value
            secrets['AUTH0_CLIENT_SECRET'] = client.get_secret('auth0-client-secret').value
            secrets['AUTH0_AUDIENCE'] = client.get_secret('auth0-audience').value
            secrets['WEBAPP_SECRET_KEY'] = client.get_secret('webapp-secret-key').value
        except Exception as e:
            print(f"Error loading secrets from Azure Key Vault: {e}")
    else:

        secrets['AUTH0_SESSION_SECRET'] = os.getenv('AUTH0_SESSION_SECRET')
        secrets['AUTH0_DOMAIN'] = os.getenv('AUTH0_DOMAIN')
        secrets['AUTH0_CLIENT_ID'] = os.getenv('AUTH0_CLIENT_ID')
        secrets['AUTH0_CLIENT_SECRET'] = os.getenv('AUTH0_CLIENT_SECRET')
        secrets['AUTH0_AUDIENCE'] = os.getenv('AUTH0_AUDIENCE')
        secrets['WEBAPP_SECRET_KEY'] = os.getenv('WEBAPP_SECRET_KEY')
    
    return secrets

# Use the secrets in your application
secrets = load_secrets()


def configure_templates():
    """
    Creates templates from the templates folder within the webapp
    """
    templates = Jinja2Templates(directory="webapp/templates")
    templates.env.filters['to_pretty_json'] = to_pretty_json
    return templates


templates = configure_templates()