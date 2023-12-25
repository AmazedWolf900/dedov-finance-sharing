# Dedov Finance Sharing Platform

Aim of this project is to record and further evidence of the financial costs incurred by each owner within the common property.

## Installation

[Docker](https://docs.docker.com/engine/install/), with [compose](https://docs.docker.com/compose/install/) extension, must be installed to run this project.

Installation steps:
1. `cp .env_example .env` - customize to your needs
2. `cp docker-compose.yml_example docker-compose.yml` - customize to your needs
3. `docker compose up`

Tested on macOS Ventura 13.4 and Debian 12.

## To-Do
- Deploy Gunicorn & NGINX instead of the development Flask webserver
- User accounts with login and individual permissions
- Pagination