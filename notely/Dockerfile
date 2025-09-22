FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencies zuerst (bessere Caches)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Defaults (kannst du beim Run überschreiben)
ENV PROJECT_ID=notely
ENV PORT=8080
EXPOSE 8080

# Robuster Prod-Server für Flask
# shell-form, damit $PORT expandiert
CMD sh -c 'gunicorn -b 0.0.0.0:${PORT:-8080} app:app'



