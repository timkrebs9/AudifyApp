import os, requests

def login(request):
    auth = request.authorization
    if not auth:
        return {'message': 'Invalid credentials'}, 401
    
    basicAuth = (auth.username, auth.password)
    response = requests.post(f"http://{os.environ.get('AUTH_URL')}/login", auth=basicAuth)
    
    if response.status_code == 200:
        return response.txt(), 200
    else:
        return response.txt(), response.status_code