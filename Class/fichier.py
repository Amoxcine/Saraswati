class Fichier:
    def __init__(self, type):
        self.type = type
        self.FileList = []

    def add_dossier1(self, fichier):
        self.FileList.append(fichier)