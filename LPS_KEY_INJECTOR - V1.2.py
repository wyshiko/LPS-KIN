from tkinter import *
from PIL import Image, ImageTk
import os

repertoire_images = repertoire_images = os.getcwd()
images = [f for f in os.listdir(repertoire_images) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

root = Tk()
root.title("LPS-KINE-V1")

image_label = Label(root)
image_label.pack()

file_name_label = Label(root, text="Nom du fichier:")
file_name_label.pack()

label_new_keyword = Label(root, text="Mot cles a ajouter à l'image")
label_new_keyword.pack()

mot_cle_entry = Entry(root)  # Champ de saisie pour le mot-clé
mot_cle_entry.pack()

# Fonction pour afficher la prochaine image
index = 0

def afficher_image():
    global index
    if index < len(images):
        image_path = os.path.join(repertoire_images, images[index])
        img = Image.open(image_path)
        img = img.resize((800, 800), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        file_name_label.config(text=f"Nom du fichier: {images[index]}")
    else:
        image_label.config(image=None)
        file_name_label.config(text="Nom du fichier:")

def changer_titre():
    global index
    mot_cle = mot_cle_entry.get()  # Récupère le mot-clé depuis le champ de saisie
    if index < len(images):
        image_path = os.path.join(repertoire_images, images[index])
        file_name, file_extension = os.path.splitext(image_path)
        new_img_path = f"{file_name}_{mot_cle}{file_extension}"
        try:
            os.rename(image_path, new_img_path)
            print(f"Le fichier a été renommé en {new_img_path}.")
        except OSError as e:
            print(f"Erreur lors du renommage du fichier : {e}")
        index += 1
        afficher_image()

def change_title_key(event):
    global index
    if event.keysym == 'Up':
        changer_titre()

def image_precedente(event):
    global index
    if event.keysym == 'Left' and index > 0:
        index -= 1
        afficher_image()

def next_image(event):
    global index
    if event.keysym == 'Right':
        index += 1
        afficher_image()

root.bind('<Left>', image_precedente)
root.bind('<Right>', next_image)
root.bind('<Up>', change_title_key)

# bouton_valider = Button(root, text="Valider", command=changer_titre)
# bouton_valider.pack()

afficher_image()
root.mainloop()
