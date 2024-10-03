import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import io
from io import BytesIO

def create_folder():
    if not os.path.exists('images'):
        os.makedirs('images')

def choose_file():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((150, 150), Image.LANCZOS)
        img = img.convert('RGBA')
        nazwa = os.path.basename(file_path)
        n = nazwa.split('.')
        del n[-1]
        nazwa2 = ""
        for i in n:
            nazwa2 = nazwa2 + i
        nazwa2 = nazwa2 + ".png"
        img.save(os.path.join('images', nazwa2))
        refresh_images()

def refresh_images():
    for widget in image_frame.winfo_children():
        widget.destroy()
    
    image_files = os.listdir('images/')
    for index, image_file in enumerate(image_files):
        img_path = os.path.join('images', image_file)
        display_image(img_path, index)

def display_image(img_path, index):
    img = Image.open(img_path)
    img = img.convert('RGBA')
    img_tk = ImageTk.PhotoImage(img)
    btn = tk.Button(image_frame, image=img_tk, command=lambda: copy_to_clipboard(img_path))
    btn.image = img_tk
    row = index // 4
    column = index % 4
    btn.grid(row=row, column=column, padx=10, pady=10)

import copykitten
def copy_to_clipboard(filepath):
    image = Image.open(filepath)
    pixels = image.tobytes()
    copykitten.copy_image(pixels, image.width, image.height)

window = tk.Tk()
window.title("Sticker board")
window.geometry("800x300")
window.wm_attributes("-topmost", 1)

choose_file_btn = tk.Button(window, text="Choose File for a new sticker", command=choose_file)
choose_file_btn.pack(pady=10)

image_frame = tk.Frame(window)
image_frame.pack(padx=10, pady=10, fill='both', expand=True)

#refresh_btn = tk.Button(window, text="Refresh", command=refresh_images)
#refresh_btn.pack(pady=10)

create_folder()
refresh_images()

window.mainloop()
