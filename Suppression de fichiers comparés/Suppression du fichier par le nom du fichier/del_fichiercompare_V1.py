import os
import shutil
from tqdm import tqdm

def compare_and_delete_files(folder1, folder2):
    num_files = count_files(folder1)
    progress_bar = tqdm(total=num_files, unit="file(s)")

    for root, dirs, files in os.walk(folder1):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)

            matching_files = find_matching_files(file_name, folder2)
            if matching_files:
                print(f"Suppression du fichier {file_path}")
                os.remove(file_path)
            progress_bar.update(1)

    progress_bar.close()


def find_matching_files(file_name, folder):
    #Renvoie la liste des fichiers
    matching_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file == file_name:
                #Ajout dans la liste
                matching_files.append(os.path.join(root, file))
    return matching_files


def count_files(folder):
    num_files = 0
    for root, dirs, files in os.walk(folder):
        num_files += len(files)
    return num_files


# Exemple d'utilisation
dossier1 = r"C:\Users\avets\Desktop\Atrier"
dossier2 = r"E:"

print(dossier1)
print(dossier2)

compare_and_delete_files(dossier1, dossier2)