FROM python:3.11-slim-bullseye

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# python dependencies
COPY requirements requirements/
RUN pip install -r requirements/production.txt

# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/gunicorn.sh /

# Fix windows docker bug, convert CRLF to LF
RUN sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh && sed -i 's/\r$//g' /gunicorn.sh && chmod +x /gunicorn.sh

WORKDIR /app
