FROM python:3.12-slim-buster

ENV DEBIAN_FRONTEND=noninteractive
ENV HOST="0.0.0.0"
ENV PORT=8000
WORKDIR /app

# Installa le dipendenze
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione
COPY app/ /app/app/
COPY main.py /app/

# Esponi la porta
EXPOSE 8000

# Comando di avvio dell'applicazione
CMD ["python", "main.py"]