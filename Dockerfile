FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 3100

CMD ["gunicorn", "main:app"]