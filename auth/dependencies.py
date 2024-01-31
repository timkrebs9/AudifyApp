from fastapi import Request, HTTPException, status


def ProtectedEndpoint(request: Request):
    
    
    if not 'id_token' in request.session:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT, 
            detail="Not authenticated", 
            headers={"Location": "/login"}
        )