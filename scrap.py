import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from googletrans import Translator
import io
from tqdm import tqdm
import colorama
from colorama import Fore, Style

# Initialiser colorama pour les couleurs Windows
colorama.init()

# Demander la langue à l'utilisateur
language = input("Entrez le code de la langue (FR, EU, ES, etc.) : ").upper()

# URL de la page à scraper
url = f"https://streamtoearn.io/gifts?region={language}"

# Dossiers où enregistrer les images
webp_folder = f"{language}/tiktok_gifts"
png_folder = f"{language}/tiktok_gifts_png"
os.makedirs(webp_folder, exist_ok=True)
os.makedirs(png_folder, exist_ok=True)

# Initialiser le traducteur
translator = Translator()

# Fonctions utilitaires
def is_webp(img_url):
    return img_url.lower().endswith(".webp")

def sanitize_filename(filename):
    # Remplacer les caractères non autorisés dans les noms de fichiers
    invalid_chars = '<>:"/\\|?*\n\r'
    # Nettoyer les espaces en début/fin de chaîne et les retours à la ligne
    filename = filename.strip()
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    # Supprimer les underscores multiples
    while '__' in filename:
        filename = filename.replace('__', '_')
    return filename

def translate_to_french(text):
    try:
        # Traduire en français
        translation = translator.translate(text, dest='fr')
        return translation.text
    except:
        # En cas d'erreur de traduction, retourner le texte original
        return text

# Template HTML
html_template = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des Cadeaux TikTok - {language}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #1F4E78;
            text-align: center;
            padding: 20px;
            margin-bottom: 30px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .gifts-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }}
        .gift-card {{
            background: white;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .gift-card:hover {{
            transform: translateY(-5px);
        }}
        .gift-card img {{
            width: 100px;
            height: 100px;
            object-fit: contain;
            margin-bottom: 10px;
        }}
        .gift-name {{
            font-weight: bold;
            color: #333;
            margin: 10px 0;
        }}
        .gift-price {{
            color: #1F4E78;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }}
        .gift-price img {{
            width: 20px;
            height: 20px;
            margin: 0;
        }}
        .gift-number {{
            color: #666;
            font-size: 0.9em;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <h1>Liste des Cadeaux TikTok - {language}</h1>
    <div class="gifts-container">
        {gift_cards}
    </div>
</body>
</html>
"""

# Template pour chaque carte de cadeau
gift_card_template = """
        <div class="gift-card">
            <div class="gift-number">#{number}</div>
            <img src="{png_path}" alt="{name}">
            <div class="gift-name">{name}</div>
            <div class="gift-price">
                {price} <img src="https://app.streamtoearn.io/assets/images/coin.png" alt="pièces">
            </div>
        </div>
"""

# Récupérer le contenu HTML de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Trouver toutes les div de cadeaux
gift_divs = soup.find_all("div", class_="gift")

# Debug: Afficher le nombre de cadeaux trouvés
print(f"\n{Fore.YELLOW}🔍 Nombre de cadeaux trouvés : {len(gift_divs)}{Style.RESET_ALL}")

# Liste pour stocker les cartes de cadeaux HTML
gift_cards_html = []

# Compteur pour l'ordre de téléchargement
download_counter = 1

# Créer une barre de progression plus conviviale
with tqdm(total=len(gift_divs), 
          desc=f"{Fore.CYAN}🎁 Téléchargement des cadeaux{Style.RESET_ALL}",
          bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Style.RESET_ALL),
          ncols=100,
          unit="img",
          unit_scale=True,
          leave=True) as pbar:
    
    for gift_div in gift_divs:
        # Trouver l'image dans la div du cadeau
        img = gift_div.find("img")
        # Trouver le nom du cadeau
        name_p = gift_div.find("p", class_="gift-name")
        # Trouver le prix dans la balise p
        price_p = gift_div.find("p", class_="gift-price")
        
        if img and price_p and img.get("src") and img.get("src").startswith("http") and is_webp(img.get("src")):
            img_url = img.get("src")
            # Extraire seulement le nombre de pièces (le premier mot avant l'image de la pièce)
            price = price_p.get_text(strip=True).split()[0]
            
            # Utiliser le nom du cadeau depuis la balise p class="gift-name"
            if name_p:
                gift_name = name_p.text.strip()
                # Traduire le nom en français
                french_name = translate_to_french(gift_name)
                # Ajouter le numéro de téléchargement au début du nom
                webp_filename = f"{download_counter:03d} - {sanitize_filename(french_name)}.webp"
                png_filename = f"{download_counter:03d} - {sanitize_filename(french_name)}.png"
                
                # Créer le HTML pour cette carte de cadeau
                relative_png_path = f"tiktok_gifts_png/{png_filename}"
                gift_card_html = gift_card_template.format(
                    number=f"{download_counter:03d}",
                    png_path=relative_png_path,
                    name=french_name,
                    price=price
                )
                gift_cards_html.append(gift_card_html)
                
            else:
                base_name = os.path.splitext(os.path.basename(img_url))[0]
                webp_filename = f"{download_counter:03d} - {base_name}.webp"
                png_filename = f"{download_counter:03d} - {base_name}.png"
                
                # Créer le HTML pour cette carte de cadeau
                relative_png_path = f"tiktok_gifts_png/{png_filename}"
                gift_card_html = gift_card_template.format(
                    number=f"{download_counter:03d}",
                    png_path=relative_png_path,
                    name=base_name,
                    price=price
                )
                gift_cards_html.append(gift_card_html)
            
            webp_path = os.path.join(webp_folder, webp_filename)
            png_path = os.path.join(png_folder, png_filename)
            
            # Télécharger l'image WEBP
            img_data = requests.get(img_url).content
            
            # Sauvegarder en WEBP
            with open(webp_path, "wb") as f:
                f.write(img_data)
            
            # Convertir en PNG
            try:
                # Ouvrir l'image WEBP depuis les données en mémoire
                image = Image.open(io.BytesIO(img_data))
                # Convertir et sauvegarder en PNG
                image.save(png_path, "PNG")
            except Exception as e:
                print(f"\n{Fore.RED}❌ Erreur lors de la conversion en PNG : {e}{Style.RESET_ALL}")
            
            # Incrémenter le compteur et la barre de progression
            download_counter += 1
            pbar.update(1)

# Créer le fichier HTML final
html_output = html_template.format(
    language=language,
    gift_cards="\n".join(gift_cards_html)
)

# Sauvegarder le fichier HTML
html_file = f"{language}/gift_prices.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"\n{Fore.GREEN}✨ Téléchargement et conversion terminés ! {download_counter-1} images traitées.{Style.RESET_ALL}")
print(f"{Fore.CYAN}📝 La page des cadeaux a été générée : {html_file}{Style.RESET_ALL}")
