# JCR-Python-TP1 - Gestion de Boutique

Projet de simulation de gestion d'une boutique (ChossettZ).

## Structure du projet

```
JCR-Python-TP1/
├── venv/              # Environnement virtuel Python
├── app/               # Package contenant tous les modules
│   ├── __init__.py    # Rend app/ importable
│   ├── config.py      # Configuration et variables initiales
│   ├── display.py     # Fonctions d'affichage
│   ├── transaction.py # Logique de transaction et calculs
│   └── utils.py       # Fonctions utilitaires
├── main.py            # Point d'entrée du programme
└── README.md          # Documentation
```

## Installation

1. Créer et activer l'environnement virtuel :
```bash
# Créer le venv
python -m venv venv

# Activer le venv (Windows bash)
source venv/Scripts/activate
```

2. Lancer le programme :
```bash
python main.py
```

## Modules

- **app/config.py** : Contient toutes les variables de configuration (prix, stock, comptes)
- **app/display.py** : Gère tous les affichages (bienvenue, facture, types de variables)
- **app/transaction.py** : Gère les calculs (TTC, montants) et le traitement des achats
- **app/utils.py** : Fonctions utilitaires (alertes de stock, input utilisateur)
- **app/__init__.py** : Transforme le dossier app/ en package Python importable
- **main.py** : Orchestre le flux du programme en appelant les différents modules
