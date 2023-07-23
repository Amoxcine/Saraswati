import dhash
from PIL import Image

def comparer_images(chemin_image1, chemin_image2):
    # Charger les images et les convertir en niveaux de gris
    image1 = Image.open(chemin_image1).convert('L')
    image2 = Image.open(chemin_image2).convert('L')

    # Calculer les hachages dhash des images
    hachage1 = dhash.dhash_int(image1)
    hachage2 = dhash.dhash_int(image2)

    # Comparer les hachages dhash
    similarite = dhash.get_num_bits_different(hachage1, hachage2)

    # Définir un seuil pour déterminer si les images sont similaires
    seuil = 10  # Vous pouvez ajuster ce seuil en fonction de vos besoins

    # Si la similarité est inférieure au seuil, les images sont considérées comme identiques
    return similarite <= seuil