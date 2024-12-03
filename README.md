Rhythmix
========

AI-powered app for song processing.

## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

Local deploy:

`docker compose up --build`

Production deploy:

`docker compose -f docker-compose-prod.yml up --build`

Create an admin:

`docker compose run backend python manage.py createsuperuser`

Run tests:

`docker compose run backend pytest`
