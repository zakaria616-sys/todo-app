# To-Do List API – DevSecOps Project 

Ce projet consiste à développer une API REST minimaliste de gestion de tâches avec Flask, intégrée dans un pipeline CI/CD sécurisé DevSecOps.

## Stack Technique

- Python 3.x + Flask
- Docker (multi-stage, non-root)
- GitHub Actions (CI/CD)
- Ansible (déploiement automatisé)
- Outils Shift-Left : CodeQL, Trivy, Dependabot, ansible-vault

## Lancer localement

```bash
pip install -r requirements.txt
python app.py
```

## Tester

```bash
pytest tests/
```

## Build Docker

```bash
docker build -t todo-api .
docker run -p 5000:5000 todo-api
```

## Déployer avec Ansible

```bash
ansible-playbook -i ansible/inventory.yml ansible/deploy.yml --ask-vault-pass
```

## Sécurité

- Secrets chiffrés via `ansible-vault`
- Dépendances scannées (Dependabot)
- Analyse de code avec CodeQL
- Scan conteneur avec Trivy

## Auteur

Zakaria BOULAYAD – Master 2 CIP - ENSAM
