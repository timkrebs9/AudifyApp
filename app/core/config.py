import logging
import logging.config
import os

from app.services.utils import to_pretty_json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from fastapi.templating import Jinja2Templates


logging.config.fileConfig("app/etc/logging.conf")
logger = logging.getLogger("azure_secrets_loader")


def load_secrets() -> dict[str, str]:
    secrets = {}
    key_vault_name = "audifywebapp"

    if key_vault_name:
        logger.info(
            "Azure Key Vault is configured. Attempting to load secrets."
        )
        kv_uri = f"https://{key_vault_name}.vault.azure.net"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=kv_uri, credential=credential)

        try:
            secrets["AUTH0_SESSION_SECRET"] = client.get_secret(
                "auth0-session-secret"
            ).value
            secrets["AUTH0_DOMAIN"] = client.get_secret("auth0-domain").value

            secrets["AUTH0_CLIENT_ID"] = client.get_secret(
                "auth0-client-id"
            ).value
            secrets["AUTH0_CLIENT_SECRET"] = client.get_secret(
                "auth0-client-secret"
            ).value
            secrets["AUTH0_AUDIENCE"] = client.get_secret(
                "auth0-audience"
            ).value
            secrets["WEBAPP_SECRET_KEY"] = client.get_secret(
                "webapp-secret-key"
            ).value
            logger.info("Successfully loaded secrets from Azure Key Vault.")
        except Exception:
            logger.exception("Error loading secrets from Azure Key Vault")
    else:
        logger.info("Loading secrets from environment variables.")
        secrets["AUTH0_SESSION_SECRET"] = os.getenv("AUTH0_SESSION_SECRET")
        secrets["AUTH0_DOMAIN"] = os.getenv("AUTH0_DOMAIN")
        secrets["AUTH0_CLIENT_ID"] = os.getenv("AUTH0_CLIENT_ID")
        secrets["AUTH0_CLIENT_SECRET"] = os.getenv("AUTH0_CLIENT_SECRET")
        secrets["AUTH0_AUDIENCE"] = os.getenv("AUTH0_AUDIENCE")
        secrets["WEBAPP_SECRET_KEY"] = os.getenv("WEBAPP_SECRET_KEY")

    return secrets


secrets = load_secrets()


def configure_templates() -> Jinja2Templates:
    """
    Creates templates from the templates folder within the webapp
    """
    templates = Jinja2Templates(directory="webapp/templates")
    templates.env.filters["to_pretty_json"] = to_pretty_json
    return templates


secrets = load_secrets()
templates = configure_templates()
