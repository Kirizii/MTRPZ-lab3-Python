FROM python:3.12-alpine

WORKDIR /app

COPY requirements/backend.in .

RUN pip install --upgrade pip \
    && pip install -r backend.in

COPY . .

EXPOSE 8000

CMD ["uvicorn", "spaceship.main:app", "--host", "0.0.0.0", "--port", "8000"]
