# TDD_Sudoku_Generator

Générateur et solveur de Sudoku (implementation backtracking) avec tests TDD.

## Installation

### API & Logic
```shell
cd api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## CI/CD deployment (GHCR + SSH)

Le workflow `deploy` construit et publie 3 images Docker dans GHCR:
- `ghcr.io/<owner>/aws-docker-api`
- `ghcr.io/<owner>/aws-docker-front`
- `ghcr.io/<owner>/aws-docker-nginx`

Puis il se connecte en SSH au serveur cible et lance:
- `docker compose pull`
- `docker compose up -d --remove-orphans`

Secrets GitHub a configurer:
- `GHCR_TOKEN` (token GHCR, scope `read:packages`)
- `SSH_HOST`
- `SSH_PORT`
- `SSH_USER`
- `SSH_PRIVATE_KEY`
- `SSH_TARGET_DIR` (dossier de deployment sur le serveur)

Le fichier `docker-compose.yml` supporte les variables:
- `GHCR_NAMESPACE` (ex: `ghcr.io/<owner>`)
- `IMAGE_TAG` (ex: SHA du commit)
