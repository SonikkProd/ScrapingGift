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

# Récupérer le contenu HTML de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Trouver toutes les images sur la page
images = soup.find_all("img")

# Filtrer les images WEBP
webp_images = [img for img in images if img.get("src") and img.get("src").startswith("http") and is_webp(img.get("src"))]

# Compteur pour l'ordre de téléchargement
download_counter = 1

# Créer une barre de progression plus conviviale
with tqdm(total=len(webp_images), 
          desc=f"{Fore.CYAN}🎁 Téléchargement des cadeaux{Style.RESET_ALL}",
          bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Style.RESET_ALL),
          ncols=100,
          unit="img",
          unit_scale=True,
          leave=True) as pbar:
    for img in webp_images:
        img_url = img.get("src")
        if img_url and img_url.startswith("http") and is_webp(img_url):
            # Utiliser l'attribut alt comme nom de fichier, ou le nom original si alt n'existe pas
            alt_text = img.get("alt", "")
            if alt_text:
                # Traduire le nom en français
                french_name = translate_to_french(alt_text)
                # Ajouter le numéro de téléchargement au début du nom
                webp_filename = f"{download_counter:03d} - {sanitize_filename(french_name)}.webp"
                png_filename = f"{download_counter:03d} - {sanitize_filename(french_name)}.png"
            else:
                base_name = os.path.splitext(os.path.basename(img_url))[0]
                webp_filename = f"{download_counter:03d} - {base_name}.webp"
                png_filename = f"{download_counter:03d} - {base_name}.png"
            
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

print(f"\n{Fore.GREEN}✨ Téléchargement et conversion terminés ! {download_counter-1} images traitées.{Style.RESET_ALL}")
