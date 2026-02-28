FROM python:3.11-slim

WORKDIR /app

# Copier les fichiers de dépendances
COPY api/requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY api/ .
COPY src/ ./src

# Exposer le port
EXPOSE 8000

# Commande de démarrage
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]