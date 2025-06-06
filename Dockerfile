FROM python:3.12.11-alpine3.22

ENV DEBIAN_FRONTEND noninteractive
ENV HOST="0.0.0.0"
ENV PORT=8000
WORKDIR /app

# Installa Poetry
RUN pip install --no-cache-dir poetry

# Copia i file di configurazione Poetry prima del codice per sfruttare la cache
COPY pyproject.toml poetry.lock* /app/

# Configura Poetry per non usare un ambiente virtuale nel container
RUN poetry config virtualenvs.create false

# Installa le dipendenze
RUN poetry install --no-dev --no-interaction --no-ansi

# Copia il codice dell'applicazione
COPY app/* /app/
COPY main.py /app/

# Pulisci eventuali pacchetti non necessari
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Esponi la porta se la tua app ne usa una
# EXPOSE 8000

# Comando di avvio dell'applicazione
CMD ["python", "main.py"]