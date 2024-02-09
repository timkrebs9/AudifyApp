from app.core.config import secrets
from authlib.integrations.starlette_client import OAuth


oauth = OAuth()
oauth.register(
    "auth0",
    client_id=secrets["AUTH0_CLIENT_ID"],
    client_secret=secrets["AUTH0_CLIENT_SECRET"],
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{secrets["AUTH0_DOMAIN"]}/.well-known/openid-configuration',
)
