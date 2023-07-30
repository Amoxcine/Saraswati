from tqdm import tqdm
import os


def count_files(folder):
    num_files = 0
    for root, dirs, files in os.walk(folder):
        num_files += len(files)
    return num_files


class ProgressBar:
    def __init__(self, number):
        self.number = number
        self.progress_bar = tqdm(total=self.number, unit="files")
        self.description = ""
        self.progress = ""

    def update(self, newDescriptionDeleted="", newDescritpionProgress=""):
        self.progress_bar.update(1)

        if newDescriptionDeleted:
            self.description = "Fichier récemment supprimé : " + newDescriptionDeleted
        if newDescritpionProgress:
            self.progress = "Fichier en cours de traitement : " + newDescritpionProgress

        # Mise à jour dynamique de la description sans ajouter de nouvelles lignes
        description = f"{self.description} {self.progress}"
        self.progress_bar.set_postfix_str(description, refresh=True)

    def decrement(self):
        self.progress_bar.update(-1)

    def end(self):
        self.progress_bar.close()
