# 🎁 TikTok Gift Scraper v1.0.0

## ✨ Fonctionnalités principales

- Téléchargement automatique des cadeaux TikTok depuis streamtoearn.io
- Support multi-régions (FR, EU, ES, etc.)
- Conversion automatique des images WEBP en PNG
- Traduction automatique des noms de cadeaux en français
- Interface en ligne de commande avec barre de progression colorée
- Organisation automatique des fichiers par région

## 🛠️ Caractéristiques techniques

- Double sauvegarde des images (WEBP + PNG)
- Nommage intelligent des fichiers avec numérotation automatique
- Gestion des caractères spéciaux dans les noms de fichiers
- Traitement des erreurs robuste
- Affichage en temps réel de la progression

## 📦 Dépendances principales

- requests : Gestion des requêtes HTTP
- beautifulsoup4 : Parsing HTML
- Pillow : Traitement des images
- googletrans : Traduction automatique
- tqdm : Barre de progression
- colorama : Affichage coloré dans le terminal

## 💡 Utilisation

1. Lancez le script
2. Entrez le code de la région souhaitée (FR, EU, ES, etc.)
3. Le script télécharge et convertit automatiquement toutes les images

## 📂 Structure des dossiers

```
[REGION]/
├── tiktok_gifts/     # Images au format WEBP
└── tiktok_gifts_png/ # Images au format PNG
```

## 🔄 Notes de mise à jour

- Première version stable du script
- Support complet du scraping des cadeaux TikTok
- Interface utilisateur intuitive en français
- Système de traduction intégré 