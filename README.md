# LogiAI — Application intelligente de prédiction des retards de livraison

## 1. Présentation

LogiAI est une application intelligente permettant d'estimer la probabilité de retard d'une livraison à partir de plusieurs caractéristiques : distance, poids, heure de départ, conditions météorologiques, trafic, nombre d'arrêts et type de véhicule.

L'application expose le modèle de Machine Learning à travers une API REST développée avec FastAPI.

## 2. Fonctionnalités

- Prédiction de la probabilité de retard d'une livraison.
- Déclenchement automatique d'une alerte selon un seuil configurable.
- API REST avec FastAPI.
- Validation des données avec Pydantic.
- Authentification par clé API.
- Informations sur la version du modèle.
- Packaging Python avec Wheel et distribution source.

## 3. Architecture du projet

```text
LogiAI/
│
├── src/
│   └── logiai/
│       ├── __init__.py
│       ├── config.py
│       ├── dataset.py
│       ├── predict.py
│       ├── train.py
│       └── api/
│           ├── __init__.py
│           ├── main.py
│           ├── schemas.py
│           └── security.py
│
├── data/
│   └── livraisons.csv
│
├── models/
│   ├── model.joblib
│   └── model_info.json
│
├── tests/
├── docs/
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 4. Technologies utilisées

- Python
- FastAPI
- Scikit-learn
- Pandas et NumPy
- Joblib
- Pydantic
- Uvicorn
- Pytest
- Setuptools et Wheel

## 5. Installation en environnement de développement

Créer un environnement virtuel :

```bash
python -m venv .venv
```

L'activer sous Windows :

```powershell
.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Installer le package en mode éditable :

```bash
pip install -e .
```

## 6. Configuration

Créer un fichier `.env` à partir de `.env.example`, puis renseigner les clés nécessaires :

```env
LOGIAI_API_KEY=votre_cle_api
LOGIAI_ADMIN_KEY=votre_cle_admin
```

Définir le chemin racine de l'application sous PowerShell :

```powershell
$env:LOGIAI_HOME = (Get-Location).Path
```

Le dossier indiqué doit contenir les répertoires `data/` et `models/`, ainsi que le fichier `.env` si nécessaire.

Ne jamais publier le fichier `.env` sur GitHub.

## 7. Lancement de l'API

```bash
python -m uvicorn logiai.api.main:app --reload
```

Documentation interactive :

http://127.0.0.1:8000/docs

## 8. Endpoints principaux

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/health` | Vérifier l'état de l'API |
| POST | `/v1/predict` | Prédire le risque de retard |
| GET | `/v1/model-info` | Consulter les informations du modèle |

L'endpoint `/v1/predict` nécessite une clé API dans l'en-tête `x-api-key`.

## 9. Packaging

Construire les distributions :

```bash
python -m pip install build
python -m build
```

Deux fichiers sont générés dans `dist/` :

- `logiai-0.1.0-py3-none-any.whl`
- `logiai-0.1.0.tar.gz`

Installer le Wheel :

```bash
pip install dist/logiai-0.1.0-py3-none-any.whl
```

Vérifier l'installation :

```bash
python -c "from logiai.predict import Predictor; print('LogiAI installé avec succès')"
```

**Important :** le Wheel contient le code Python, mais pas les données ni le modèle entraîné. Ces ressources doivent être fournies séparément et accessibles via `LOGIAI_HOME`.

## 10. Tests

Exécuter les tests automatisés :

```bash
pytest -v
```

Vérifier les dépendances :

```bash
pip check
```

## 11. Démonstration

Une fois le package installé et les ressources configurées, il est possible d'utiliser directement le prédicteur :

```python
from logiai.predict import Predictor

predictor = Predictor()

livraison = {
    "distance_km": 120,
    "poids_kg": 450,
    "heure_depart": 17,
    "pluie_mm": 8,
    "trafic_index": 7.5,
    "nb_arrets": 4,
    "type_vehicule": "camion"
}

resultat = predictor.predict(livraison)
print(resultat)
```

## 12. Version

Version actuelle : **0.1.0**

Projet pédagogique — Atelier MLOps : Packaging et distribution d'une application intelligente.
