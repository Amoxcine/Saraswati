import os

def supprimer_dossiers_vides(dossier):
    for root, dirs, files in os.walk(dossier, topdown=False):
        for nom in dirs:
            chemin_dossier = os.path.join(root, nom)
            if len(os.listdir(chemin_dossier)) == 0:
                print(f"Suppression du dossier vide : {chemin_dossier}")
                os.rmdir(chemin_dossier)


# Exemple d'utilisation
dossier1 = r"\Users\avets\Desktop\Atrier"

supprimer_dossiers_vides(dossier1)