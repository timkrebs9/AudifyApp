from fastapi import HTTPException
from fastapi import Request
from fastapi import status


def protected_endpoint(request: Request) -> None:
    if "id_token" not in request.session:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            detail="Not authenticated",
            headers={"Location": "/login"},
        )
