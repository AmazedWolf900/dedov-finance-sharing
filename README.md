# Dedov Finance Sharing Platform

Projekt slouží pro evidenci finančních nákladů jednotlivými osobami v rámci společné nemovitosti.

## Instalace

Pro spuštení je nutné míst nainstalovaný [Docker](https://docs.docker.com/engine/install/) s rozšířením [compose](https://docs.docker.com/compose/install/).

Postup pro spuštění:
1. Zkopíruj a případně uprav soubor `.env`: `cp .env_example .env`
2. Zkopíruj a případně uprav soubor `docker-compose.yml_example docker-compose.yml`
3. `docker compose up`

Testováno na macOS Ventura 13.4 a Debian 12.