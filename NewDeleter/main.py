from Classes.CustomLogger import CustomLogger

# import pour get_list_of_files
import os

# import pour calculate_file_hash
import hashlib

# import ProgressBar
from Classes.ProgressBar import ProgressBar


def get_list_of_files(path):
    """
    Je récupère path_init et je mets dans une variable liste tous les path des fichiers
    Je récuppère path_init et je mets dans une variable liste tous les noms des fichiers
    Je regarde si dans cette liste il y a des doublons et j'utilise le logger pour les lister
    """

    list_of_files = []
    list_of_files_name = []
    for root, dirs, files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(root, file))
            list_of_files_name.append(file)

    return list_of_files, list_of_files_name


def calculate_file_hash(file_path):
    """
    Calcule le hash MD5 du contenu binaire du fichier spécifié.

    :param file_path: Chemin du fichier.
    :return: Hash MD5 du contenu du fichier en format hexadécimal.
    """
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        # Lecture et mise à jour du hachage avec le contenu binaire du fichier par morceaux
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()


def supprimer_fichier(file_path1, duplicate_file_path, customlogger):
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

    customlogger.log_message(f"Doublon trouvé : {file_path1} - {duplicate_file_path}")

    # Vérifier le nombre de `\` dans chaque chemin
    num_backslashes1 = count_backslashes(file_path1)
    num_backslashes2 = count_backslashes(duplicate_file_path)

    # Supprimer le fichier ayant le moins de `\` dans son chemin
    deleted_file = None
    if num_backslashes1 < num_backslashes2:
        os.remove(file_path1)
        deleted_file = file_path1
    elif num_backslashes2 < num_backslashes1:
        os.remove(duplicate_file_path)
        deleted_file = duplicate_file_path
    else:
        # Si les chemins ont le même nombre de `\`, supprimer le deuxième fichier analysé
        customlogger.log_message(f"2| {file_path1} >>>>> {duplicate_file_path}")

    customlogger.log_message("")

    return deleted_file



def filtrer_doublons(list_of_files, customlogger):
    """
    Cherche les doublons dans list_of_files en utilisant le hash MD5 du contenu binaire.
    Les doublons identiques sont enregistrés dans le CustomLogger.

    :param list_of_files: Liste des chemins de fichiers.
    :param customlogger: Instance du CustomLogger pour enregistrer les doublons.
    """
    files_by_hash = {}
    progression = ProgressBar(len(list_of_files))

    for file_path in list_of_files:
        file_hash = calculate_file_hash(file_path)
        duplicate_file_path = None

        if file_hash in files_by_hash:
            duplicate_file_path = files_by_hash[file_hash]
        else:
            files_by_hash[file_hash] = file_path

        if duplicate_file_path:
            # Appeler la fonction pour supprimer le fichier en fonction du nombre de `\`
            deleted_file = supprimer_fichier(file_path, duplicate_file_path, customlogger)
            if deleted_file:
                description_deleted = f"Fichier récemment supprimé : {deleted_file}"
                progression.update(description_deleted)
            else:
                progression.update()

    progression.end()



def main(customlogger, path_init, path_to_compare):
    """
    Le programme consiste à utiliser une base de fichiers pour comparer les fichiers d'un dossier à traiter.
    Il faut alors trouver les doublons et les lister dans un logger.

    Il doit respecter le principe Ouvert fermé.
    """

    list_of_files, list_of_files_name = get_list_of_files(path_init)

    filtrer_doublons(list_of_files, customlogger)


if __name__ == "__main__":
    logger = CustomLogger("History.log")
    path_init = r"E:\Me\IMGVD\Lieux - moments"
    path_to_compare = ["C:\\Users\\julie\\Desktop\\NewDeleter\\to_compare\\1"]

    main(logger, path_init, path_to_compare)
