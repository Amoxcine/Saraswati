# Programme de suppression des doublons d'images entre deux dossiers
import os
from Plugins.ListExtension import obtenir_extensions_fichiers as OEF
from Class.fichier import Fichier
from Class.ProgressBar_main import ProgressBar
from Logger.log import CustomLogger as Logger
from Plugins.HashCompare import comparer_images

# Compter le nombre de fichiers dans un dossier
from Class.ProgressBar.countNumFile import count_files

IMG_EXTENSIONS = [".jpg", "jpeg", "png", "gif", "bmp", "tiff", "raw", "webp", "ico"]


def check_match(matching_files, file_name, path):
  if len(matching_files) > 1:

    File = []
    File.append(path)

    Logger.log_message(f"Le fichier {file_name} dans {path} existe dans les dossiers suivants :")
    for i in range(len(matching_files)):
      # Si les images sont identiques et si c'est une image et non un fichier

      # Si il est dans la liste des extensions d'images
      if any(matching_files[i].lower().endswith(ext) for ext in IMG_EXTENSIONS):
        comparaison = comparer_images(path, matching_files[i])

        # 0 = différents, 1 = identiques, 2 = A vérifier
        if comparaison:
          Logger.log_message(f"1| {matching_files[i]}")
        else:
          Logger.log_message(f"0| {matching_files[i]} mais n'est pas identique")
          matching_files.pop(i)
      else:
        Logger.log_message(f"2| {matching_files[i]} ")

    Logger.log_message("")


def deleter(dossier1, ListFolders, ClassListLEF):
  LEF = OEF(dossier1)

  for type in LEF:
    ClassListLEF.append(Fichier(type))

  for root, dirs, files in os.walk(dossier1):
    for file in files:
      for Class in ClassListLEF:
        if file.lower().endswith(Class.type):
          Class.add_dossier1(os.path.join(root, file))

  # Analyse par comparaison du nom de fichier
  for Class in ClassListLEF:
    for path in Class.FileList:

      # Path = Chemin du fichier
      # file_name = Nom du fichier
      file_name = os.path.basename(path)
      matching_files = []  # find_matching_files(file_name, dossier2)

      # print quel fichier il analyse

      # Renvoie la liste des fichiers qui correspondent au nom du fichier
      for folder in ListFolders:
        for root, dirs, files in os.walk(folder):
          for file in files:
            if file == file_name:
              # Ajout dans la liste
              matching_files.append(os.path.join(root, file))
      # Appel Logger pour prévenir qu'il existe des doublons dans les autres dossiers

      # Comparaison plus poussée par hachage des images
      matching_files = [file for file in matching_files if
                        any(file.lower().endswith(ext) for ext in IMG_EXTENSIONS) and comparer_images(path, file)]
      check_match(matching_files, file_name, path)

    ProgressBar.update()

  ProgressBar.end()


if __name__ == "__main__":
  ClassListLEF = []
  Logger = Logger("history.log")
  ListFolders = [r"F:\IMGVD\Lieux - moments", r"F:\IMGVD\Personnes"]

  dossier1 = r"E:\Me\IMGVD"

  ProgressBar = ProgressBar(count_files(dossier1))

  if not (dossier1 in ListFolders):
    deleter(dossier1, ListFolders, ClassListLEF)
