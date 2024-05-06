import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def rgb_to_grayscale(image):
    return image.convert('L')

def open_image():
    global original_image, grayscale_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        original_image = Image.open(file_path)
        original_width, original_height = original_image.size
        if original_width > 500:
            original_image = original_image.resize((500, int(original_height * (500 / original_width))), Image.LANCZOS)
        elif original_width < 500:
            original_image = original_image.resize((500, int(original_height * (500 / original_width))), Image.LANCZOS)
        grayscale_image = rgb_to_grayscale(original_image)
        root.geometry(f"{min(original_image.width, 500)}x{min(original_image.height, 500)+100}")
        update_image(original_image)

def update_image(image):
    global shown
    shown = image
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def convert_to_grayscale():
    global grayscale_image

    if grayscale_image:
        update_image(grayscale_image)

def save_image():
    if original_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            shown.save(file_path)

root = tk.Tk()
root.title("Grayscale Converter")
root.config(bg="gray")
root.geometry("500x500")

image_label = tk.Label(root)
image_label.config(bg="gray")
image_label.pack()

grayscale_button = tk.Button(root, text="Convert to Grayscale", command=convert_to_grayscale, bg="black",fg="white")
grayscale_button.pack(side="bottom", pady=(0, 5), fill="x")

save_button = tk.Button(root, text="Save Image", command=save_image, bg="black",fg="white")
save_button.pack(side="bottom",pady=5, fill="x")

open_button = tk.Button(root, text="Open Image", command=open_image,bg="black",fg="white")
open_button.pack(side="bottom", fill="x")


original_image = None
grayscale_image = None

root.mainloop()