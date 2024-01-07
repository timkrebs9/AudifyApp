# Verwenden des spezifischen Python-Images als Basis
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere das Skript update-hosts.sh aus dem Kontext des Docker-Builds in das Arbeitsverzeichnis im Container
COPY update-hosts.sh /app/update-hosts.sh

# Mache das Skript ausführbar
RUN chmod +x /app/update-hosts.sh

# Führe das Skript aus, wenn der Container startet (optional, abhängig von Ihrem Anwendungsfall)
CMD ["/app/update-hosts.sh"]
