import tkinter as tk
from tkinter import ttk


class ProgressBar:
  def __init__(self, root, label="", position="top"):
    self.root = root
    self.label = label
    self.position = position
    self.progress = ttk.Progressbar(root, mode='indeterminate')
    self.label_widget = tk.Label(root, text=label)

  def set_text(self, text):
    self.label_widget.config(text=text)

  def update(self, value):
    self.progress.stop()
    self.progress["value"] = value
    self.progress.update()
    self.progress.start()

  def pack(self):
    if self.position == "top":
      self.label_widget.pack()
      self.progress.pack()
    else:
      self.progress.pack()
      self.label_widget.pack()


class CustomProgressBar(ProgressBar):
  def __init__(self, root, label="", position="top", style="Horizontal.TProgressbar", length=200):
    super().__init__(root, label, position)
    self.progress = ttk.Progressbar(root, mode='determinate', style=style, length=length)


# Exemple d'utilisation :
if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("300x150")

  pb1 = ProgressBar(root, label="Tâche 1", position="top")
  pb1.pack()

  pb2 = CustomProgressBar(root, label="Tâche 2", position="bottom", style="Vertical.TProgressbar", length=100)
  pb2.pack()

  root.after(1000, lambda: pb1.set_text("Tâche 1 : 25%"))
  root.after(2000, lambda: pb1.update(50))
  root.after(3000, lambda: pb1.set_text("Tâche 1 : 75%"))
  root.after(4000, lambda: pb1.update(100))
  root.after(5000, lambda: pb1.set_text("Tâche 1 terminée"))

  root.after(1500, lambda: pb2.set_text("Tâche 2 : 50%"))
  root.after(2500, lambda: pb2.update(50))
  root.after(4500, lambda: pb2.set_text("Tâche 2 terminée"))

  root.mainloop()
