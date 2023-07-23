from tqdm import tqdm


class ProgressBar:
    def __init__(self, number):
        self.number = number
        self.progress_bar = tqdm(total=self.number, unit="files")

    def update(self):
        self.progress_bar.update(1)

    def decrement(self):
        self.progress_bar.update(-1)

    def close(self):
        self.progress_bar.close()
