Boilerplate RNET avec proxy rotating
====================================

Ce dépôt fournit un exemple minimal d'appel HTTP avec [rnet](https://pypi.org/project/rnet/) en mode navigateur émulé, derrière un proxy authentifié choisi aléatoirement dans un fichier `proxies.txt`.

Prérequis
---------
- Python >= 3.14
- `uv` recommandé pour gérer l'environnement (ou `pip` classique)
- Un fichier `proxies.txt` à la racine, contenant une liste de proxies (un par ligne), aux formats:
	- `http://user:pwd@ip:port`
	- `ip:port:user:pwd` (sera converti automatiquement)

Installation rapide
-------------------
1. Crée un environnement isolé (exemple avec `uv`):

	 ```bash
	 uv venv
	 uv pip install -r pyproject.toml
	 ```

	 Avec `pip` classique:

	 ```bash
	 python -m venv .venv
	 .venv\\Scripts\\activate
	 pip install -r pyproject.toml
	 ```

2. Ajoute tes proxies dans `proxies.txt`.

Exécution
---------
```bash
uv run main.py
```

Le script:
- Charge un proxy aléatoire depuis `proxies.txt`.
- Configure un client RNET avec émulation Chrome 142 sur Windows et redirections limitées.
- Fait un GET vers https://probe.velys.software/ puis affiche le statut HTTP et la réponse JSON.

Structure des fichiers
----------------------
- `main.py` : logique principale (lecture proxy, client RNET, appel de test)
- `pyproject.toml` : métadonnées et dépendances (`aiofiles`, `rnet`)
- `proxies.txt` : liste des proxies utilisés à l'exécution (à créer)

Notes pratiques
---------------
- Le fichier `proxies.txt` ne doit pas être versionné si tu y mets des identifiants sensibles.
- En cas d'erreur d'authentification ou de connexion, vérifie le format des lignes du proxy et que le proxy accepte le protocole HTTP.
- Pour changer le site de test, modifie simplement l'URL dans `main.py`.
