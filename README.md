# Scraper de Cadeaux TikTok

Ce script permet de télécharger automatiquement les images de cadeaux TikTok depuis le site streamtoearn.io.

## Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ou téléchargez ce dépôt
2. Ouvrez un terminal dans le dossier du projet
3. Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Exécutez le script :
```bash
python scrap.py
```

2. Entrez le code de la langue souhaitée quand demandé (exemple : FR, EU, ES)

Le script va :
- Créer un dossier avec le code de la langue (ex: FR/tiktok_gifts)
- Télécharger les images WEBP
- Convertir les images en PNG
- Afficher une barre de progression pendant le téléchargement

## Structure des dossiers

Pour chaque langue, deux dossiers sont créés :
- `[LANGUE]/tiktok_gifts/` : contient les images au format WEBP
- `[LANGUE]/tiktok_gifts_png/` : contient les images au format PNG

## Notes

- Les noms des fichiers sont traduits en français automatiquement
- Les images sont numérotées dans l'ordre de téléchargement
- En cas d'erreur de traduction, le nom original est conservé 