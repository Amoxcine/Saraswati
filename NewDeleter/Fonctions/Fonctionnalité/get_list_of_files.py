import os

def get_file_path(root, file):
  return os.path.join(root, file)


def get_list_of_files(path):
  """
  Je récupère path_init et je mets dans une variable liste tous les path des fichiers
  Je récuppère path_init et je mets dans une variable liste tous les noms des fichiers
  Je regarde si dans cette liste il y a des doublons et j'utilise le logger pour les lister
  """

  path_list = []
  files_name_list = []
  for root, dirs, files in os.walk(path):
    for file in files:
      path_list.append(get_file_path(root, file))
      files_name_list.append(file)

  return path_list, files_name_list