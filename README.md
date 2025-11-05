# JCR-Python-TP1 - Gestion de Boutique

Projet de simulation de gestion d'une boutique (ChossettZ).

## Structure du projet

```
JCR-Python-TP1/
├── venv/              # Environnement virtuel Python
├── main.py            # Point d'entrée du programme
├── config.py          # Configuration et variables initiales
├── display.py         # Fonctions d'affichage
├── transaction.py     # Logique de transaction et calculs
└── utils.py           # Fonctions utilitaires
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

- **config.py** : Contient toutes les variables de configuration (prix, stock, comptes)
- **display.py** : Gère tous les affichages (bienvenue, facture, types de variables)
- **transaction.py** : Gère les calculs (TTC, montants) et le traitement des achats
- **utils.py** : Fonctions utilitaires (alertes de stock, input utilisateur)
- **main.py** : Orchestre le flux du programme en appelant les différents modules
