from rich.progress import Progress
import time

def example_progress_bar_with_description_and_progress():
    num_files = 10

    with Progress() as progress:
        task = progress.add_task("[cyan]Traitement en cours...", total=num_files)

        for i in range(num_files):
            description = f"Fichier en cours de traitement : fichier {i}"
            progress.update(task, advance=1, description=description)
            time.sleep(1)  # Juste pour simuler un traitement

example_progress_bar_with_description_and_progress()
