# 🎁 TikTok Gift Scraper

Un script Python pour télécharger et organiser les cadeaux TikTok depuis streamtoearn.io, avec conversion d'images et génération d'une page de présentation.

## ✨ Fonctionnalités

- Téléchargement automatique des cadeaux TikTok par région
- Conversion automatique des images WEBP en PNG
- Traduction des noms de cadeaux en français
- Génération d'une page HTML interactive
- Support multi-régions (FR, EU, ES, etc.)
- Interface en ligne de commande avec barre de progression
- Organisation automatique des fichiers

## 📋 Prérequis

```bash
pip install -r requirements.txt
```

Dépendances principales :
- requests : Gestion des requêtes HTTP
- beautifulsoup4 : Parsing HTML
- Pillow : Traitement des images
- googletrans : Traduction automatique
- tqdm : Barre de progression
- colorama : Affichage coloré dans le terminal

## 🚀 Utilisation

1. Lancez le script :
```bash
python scrap.py
```

2. Entrez le code de la région souhaitée (FR, EU, ES, etc.)

3. Le script va automatiquement :
   - Télécharger les images des cadeaux
   - Convertir les images WEBP en PNG
   - Traduire les noms en français
   - Générer une page HTML de présentation

## 📂 Structure des dossiers

```
[REGION]/
├── tiktok_gifts/        # Images au format WEBP
├── tiktok_gifts_png/    # Images au format PNG
└── gift_prices.html     # Page de présentation
```

## 📱 Page HTML générée

La page HTML générée inclut :
- Une grille responsive de cartes pour chaque cadeau
- Des effets de survol interactifs
- Images optimisées et bien dimensionnées
- Affichage clair des informations :
  - Numéro du cadeau
  - Image du cadeau
  - Nom traduit
  - Prix en pièces avec icône

## 🎨 Personnalisation

Le script utilise des templates HTML et CSS personnalisables :
- Mise en page responsive
- Design moderne avec ombres et animations
- Thème de couleur professionnel
- Adaptation automatique à la taille de l'écran

## 🔄 Processus de traitement

1. **Scraping** :
   - Récupération de la page HTML
   - Extraction des informations des cadeaux
   - Identification des images et prix

2. **Traitement des images** :
   - Téléchargement au format WEBP
   - Conversion en PNG pour meilleure compatibilité
   - Nommage intelligent avec numérotation

3. **Traduction** :
   - Traduction automatique des noms en français
   - Conservation du nom original en cas d'échec

4. **Génération HTML** :
   - Création d'une carte par cadeau
   - Application du style CSS
   - Organisation en grille responsive

## ⚠️ Notes importantes

- Le script nécessite une connexion Internet
- Les images sont sauvegardées en double format (WEBP et PNG)
- La traduction nécessite une connexion à l'API Google Translate
- Les fichiers existants seront écrasés à chaque exécution

## 🐛 Gestion des erreurs

Le script inclut :
- Gestion des erreurs de téléchargement
- Gestion des erreurs de conversion d'images
- Gestion des erreurs de traduction
- Messages d'erreur colorés et explicites

## 🤝 Contribution

N'hésitez pas à contribuer au projet en :
- Signalant des bugs
- Proposant des améliorations
- Ajoutant de nouvelles fonctionnalités

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails. 