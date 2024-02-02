import os
import configparser
from fastapi.templating import Jinja2Templates
from utils import to_pretty_json


import os
import configparser
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def load_config():
    """
    Loads configuration from Azure Key Vault or environment variables.
    Falls back to .config file if neither is set.
    """
    config = configparser.ConfigParser()
    key_vault_name = os.environ.get("KEY_VAULT_NAME")
    
    if key_vault_name:
        # Azure Key Vault is configured
        KVUri = f"https://audifyapp-gzrvzu54wzzse.vault.azure.net"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)
        
        # Attempt to load secrets from Azure Key Vault
        try:
            config['AUTH0'] = {
                'SESSION_SECRET': client.get_secret('auth0-session-secret').value,
                'DOMAIN': client.get_secret('auth0-domain').value,
                'CLIENT_ID': client.get_secret('auth0-client-id').value,
                'CLIENT_SECRET': client.get_secret('auth0-client-secret').value,
                'AUDIENCE': client.get_secret('AUTH0_AUDIENCE').value
            }
            config['WEBAPP'] = {
                'SECRET_KEY': client.get_secret('webapp-secret-key').value
            }

            ###################################################
            print(f"AUTH0 Session Secret '{client.get_secret('auth0-session-secret').value}'.")
            print(f"AUTH0 Domain '{client.get_secret('auth0-domain').value}'.")
            print(f"AUTH0 Client ID '{client.get_secret('auth0-client-id').value}'.")
            print(f"AUTH0 Client Secret '{client.get_secret('auth0-client-secret').value}'.")
            print(f"WEBAPP SECRET_KEY '{client.get_secret('webapp-secret-key').value}'.")
            ###################################################



        except Exception as e:
            print(f"Error loading secrets from Azure Key Vault: {e}")
            # Fall back to .config file or other sources as needed
    else:
        # Environment variables or .config file fallback
        if os.environ.get("AUTH0_SESSION_SECRET"):
            # Load from environment variables
            config['AUTH0'] = {
                'SESSION_SECRET': os.environ.get('AUTH0_SESSION_SECRET'),
                'DOMAIN': os.environ.get('AUTH0_DOMAIN'),
                'CLIENT_ID': os.environ.get('AUTH0_CLIENT_ID'),
                'CLIENT_SECRET': os.environ.get('AUTH0_CLIENT_SECRET'),
                'AUDIENCE': os.environ.get('AUTH0_AUDIENCE')
            }
            config['WEBAPP'] = {
                'SECRET_KEY': os.environ.get('WEBAPP_SECRET_KEY')
            }
        else:
            # Load from .config file
            config.read('.config')

    return config

# Configuration usage example
config = load_config()


def configure_templates():
    """
    Creates templates from the templates folder within the webapp
    """
    templates = Jinja2Templates(directory="webapp/templates")
    templates.env.filters['to_pretty_json'] = to_pretty_json
    return templates


templates = configure_templates()