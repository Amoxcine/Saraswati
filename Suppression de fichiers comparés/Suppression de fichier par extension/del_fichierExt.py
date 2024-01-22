# Supression d'un fichier en utilisant son extension

import os


def supprimer_fichiers_par_extension(chemin, extension):
    # Parcourir tous les fichiers et dossiers du chemin actuel
    for root, dirs, files in os.walk(chemin):
        for fichier in files:
            if fichier.endswith(extension):
                fichier_path = os.path.join(root, fichier)

                # Supprimer le fichier
                os.remove(fichier_path)
                print(f"Fichier supprimé : {fichier_path}")


# Exemple d'utilisation
chemin_repertoire = "/Users/avets/Desktop/Takeout/GooglePhotos"

supprimer_fichiers_par_extension(chemin_repertoire, ".json")


print("Opération terminée !")