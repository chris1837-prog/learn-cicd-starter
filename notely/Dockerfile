FROM python:3.12-slim
# Erklärung: Schlankes Python-Basisimage (klein & schnell)

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# Erklärung: Keine .pyc-Dateien; sofortige Ausgabe im Terminal (kein Buffering)

WORKDIR /app
# Erklärung: Setzt das Arbeitsverzeichnis im Container auf /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Erklärung: Zuerst nur Abhängigkeiten kopieren und installieren (bessere Docker-Layer-Caches)

COPY . .
# Erklärung: Danach deinen App-Code ins Image kopieren

ENV PROJECT_ID=notely
ENV PORT=8000
# Erklärung: Standard-ENV im Container (kannst du beim Run überschreiben)

EXPOSE 8000
# Erklärung: Dokumentiert, welchen Port der Container anbietet

CMD ["python", "app.py"]
# Erklärung: Startkommando – führt deine Flask-App aus

