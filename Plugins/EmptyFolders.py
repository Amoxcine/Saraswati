import os

def supprimer_dossiers_vides(dossier):
    for root, dirs, files in os.walk(dossier, topdown=False):
        for nom in dirs:
            chemin_dossier = os.path.join(root, nom)
            if len(os.listdir(chemin_dossier)) == 0:
                print(f"Suppression du dossier vide : {chemin_dossier}")
                os.rmdir(chemin_dossier)
"""
if __name__ == "__main__":
    # Remplacez 'chemin_dossier' par le chemin absolu du dossier que vous voulez traiter
    chemin_dossier = r"C:\Users\avets\Desktop\Atrier\GooglePhotos"
    supprimer_dossiers_vides(chemin_dossier)
"""