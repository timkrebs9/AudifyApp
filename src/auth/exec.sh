docker build -t auth .
docker run --env-file .env -p 3000:3000 -it auth
