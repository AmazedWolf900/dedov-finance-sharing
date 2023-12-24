# Dedov Finance Sharing Platform

Projekt slouží pro evidenci finančních nákladů jednotlivými osobami v rámci společné nemovitosti.

## Instalace

Pro spuštení je nutné míst nainstalovaný [Docker](https://docs.docker.com/engine/install/) s rozšířením [compose](https://docs.docker.com/compose/install/).

Postup pro spuštění:
1. `cp .env_example .env` - v případě potřeby soubor uprav dle vlastních parametrů
2. `docker-compose.yml_example docker-compose.yml` - v případě potřeby soubor uprav dle vlastních parametrů
3. `docker compose up`

Testováno na macOS Ventura 13.4 a Debian 12.

## To-Do
- Uživatelské účty a přihlašování