import hashlib

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