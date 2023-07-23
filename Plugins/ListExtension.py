import os

def obtenir_extensions_fichiers(dossier):
    extensions = set()

    for root, dirs, files in os.walk(dossier):
        for fichier in files:
            extension = os.path.splitext(fichier)[1].lower()
            extensions.add(extension)

    return list(extensions)
