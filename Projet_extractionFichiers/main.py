import os
import shutil

def deplacer_fichiers(dossier_source):
    # Vérifier si le dossier source existe
    if not os.path.exists(dossier_source):
        print(f"Le dossier '{dossier_source}' n'existe pas.")
        return

    # Parcourir tous les dossiers et fichiers du dossier source
    for dossier_actuel, sous_dossiers, fichiers in os.walk(dossier_source):
        # Ignorer le dossier source lui-même pour éviter de le déplacer
        if dossier_actuel == dossier_source:
            continue

        # Déplacer tous les fichiers dans le dossier racine
        for fichier in fichiers:
            chemin_source = os.path.join(dossier_actuel, fichier)
            chemin_destination = os.path.join(dossier_source, fichier)
            shutil.move(chemin_source, chemin_destination)
            print(f"Fichier déplacé : {chemin_source} -> {chemin_destination}")

    print("Tous les fichiers ont été déplacés dans le dossier racine.")

if __name__ == "__main__":
    # Remplacez 'chemin_dossier_source' par le chemin absolu du dossier que vous voulez traiter
    chemin_dossier_source = r"C:\Users\avets\Desktop\Takeout\Google Photos"
    deplacer_fichiers(chemin_dossier_source)
