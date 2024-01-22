from Classes.CustomLogger import CustomLogger
import time

# import pour get_list_of_files
import os

# import pour calculate_file_hash
import hashlib

# import ProgressBar
from Classes.ProgressBar import ProgressBar
from NewDeleter.Fonctions.Fonctionnalité.file_hash import calculate_file_hash
from NewDeleter.Fonctions.Fonctionnalité.get_list_of_files import get_list_of_files

activation_suppression = True





def supprimer_fichier(path_init, file_path1, duplicate_file_path, customlogger):
    """
    Supprime le fichier en fonction du nombre de `\` dans leur chemin.

    :param file_path1: Chemin du premier fichier.
    :param duplicate_file_path: Chemin du deuxième fichier.
    :param customlogger: Instance du CustomLogger pour enregistrer les suppressions.
    :return: Chemin du fichier supprimé.
    """

    def count_backslashes(path):
        # Compter le nombre de `\` dans le chemin
        return path.count(os.path.sep)

    customlogger.log_message(f"Doublons | {file_path1} -- {duplicate_file_path}")

    # Vérifier le nombre de `\` dans chaque chemin
    num_backslashes1 = count_backslashes(file_path1)
    num_backslashes2 = count_backslashes(duplicate_file_path)

    # Supprimer le fichier ayant le moins de `\` dans son chemin
    last_event = None

    if activation_suppression:
        if num_backslashes1 < num_backslashes2:
            os.remove(file_path1)
            customlogger.log_message(f"Suppression de {file_path1}")
            last_event = file_path1

        elif num_backslashes2 < num_backslashes1:
            os.remove(duplicate_file_path)
            customlogger.log_message(f"Suppression de {duplicate_file_path}")
            last_event = duplicate_file_path

    if num_backslashes1 == num_backslashes2:
        # Créer un dossier dans path_init
        dossier = os.path.join(path_init, "NewDeleter - Fusion doublons")
        last_event = "Doublon : " + file_path1

        if not os.path.exists(dossier):
            os.mkdir(dossier)
            customlogger.log_message(f"Création du dossier {dossier}")

        # Si le fichier est déjà présent dans le dossier NewDeleter - Fusion doublons càd le fichier de destination, alors on supprime le fihcier le fichier qui aurait du être déplacé sinon fait la procédure habituelle qui est le déplacement du fichier dans le dossier NewDeleter - Fusion doublons
        if os.path.exists(os.path.join(dossier, os.path.basename(file_path1))):
            os.remove(file_path1)
            customlogger.log_message(f"Suppression de {file_path1}")
            customlogger.log_message("")
            return last_event
        else:
            # Déplacer le premier fichier dans le dossier
            os.rename(file_path1, os.path.join(dossier, os.path.basename(file_path1)))
            customlogger.log_message(f"Déplacement de {file_path1} dans {dossier}")

            # Supprimer le deuxième fichier
            os.remove(duplicate_file_path)
            customlogger.log_message(f"Suppression de {duplicate_file_path}")
            customlogger.log_message("")
            return last_event


def filtrer_doublons(path_init, list_of_files, customlogger):
    """
    Cherche les doublons dans list_of_files en utilisant le hash MD5 du contenu binaire.
    Les doublons identiques sont enregistrés dans le CustomLogger.

    :param list_of_files: Liste des chemins de fichiers.
    :param customlogger: Instance du CustomLogger pour enregistrer les doublons.
    """
    files_by_hash = {}
    progression = ProgressBar(len(list_of_files))
    last_event = None

    for file_path in list_of_files:
        file_hash = calculate_file_hash(file_path)
        duplicate_file_path = None

        if file_hash in files_by_hash:
            duplicate_file_path = files_by_hash[file_hash]
        else:
            files_by_hash[file_hash] = file_path

        if duplicate_file_path:
            # Appeler la fonction pour supprimer le fichier en fonction du nombre de `\`
            last_event = supprimer_fichier(path_init, file_path, duplicate_file_path, customlogger)

        progression.update(last_event, file_path)


def supprimer_dossiers_vides(dossier):
    for root, dirs, files in os.walk(dossier, topdown=False):
        for nom in dirs:
            chemin_dossier = os.path.join(root, nom)
            if len(os.listdir(chemin_dossier)) == 0:
                print(f"Suppression du dossier vide : {chemin_dossier}")
                os.rmdir(chemin_dossier)


def main(customlogger, path_init):
    """
    Le programme consiste à utiliser une base de fichiers pour comparer les fichiers d'un dossier à traiter.
    Il faut alors trouver les doublons et les lister dans un logger.

    Il doit respecter le principe Ouvert fermé.
    """
    #Afficher Début du programme et l'heure dans logger
    customlogger.log_message("\nDébut du programme " + time.strftime("|| %D | %H:%M:%S ||", time.localtime()))

    list_of_files, list_of_files_name = get_list_of_files(path_init)

    filtrer_doublons(path_init, list_of_files, customlogger)

    supprimer_dossiers_vides(path_init)

    customlogger.log_message("|| Fin du programme" + time.strftime(" %D | %H:%M:%S ||", time.localtime()))

    print("Fin du programme")


if __name__ == "__main__":
    logger = CustomLogger("History.log")
    path_init = r"C:\Users\avets\Desktop\Takeout\Google Photos"
    main(logger, path_init)