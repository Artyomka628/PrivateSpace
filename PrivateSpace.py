import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

def open_file(path):
    os.startfile(path)

def show_image(image_path):
    if image_path:
        img = Image.open(image_path)
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
        hide_widgets()

def hide_widgets():
    title_label.place_forget()
    central_frame.place_forget()
    bottom_frame.pack_forget()

def show_widgets():
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

root = tk.Tk()
root.title("Private Space")
root.attributes('-fullscreen', True)

# Set the window icon
icon_path = "C:\\Program Files\\PrivateSpace\\Icons\\Main.ico"
root.iconbitmap(icon_path)

root.protocol("WM_DELETE_WINDOW", lambda: None)

panel = tk.Label(root, bg="#2c7cf5")
panel.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = tk.Label(root, text="Private Space", font=("Helvetica", 36), bg="#2c7cf5", fg="white")
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Central buttons
central_frame = tk.Frame(root, bg="#2c7cf5")
central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

style = ttk.Style()
style.configure("Rounded.TButton", font=("Helvetica", 14), background="white", foreground="black", padding=10, relief="flat")
style.map("Rounded.TButton", background=[('active', 'white')], relief=[('active', 'flat')])

central_buttons = [
    ("Browser", "C:\\Program Files\\PrivateSpace\\browser.bat", None),
    ("Games", "C:\\Program Files\\PrivateSpace\\Games.bat", None),
    ("My Files", "C:\\Program Files\\PrivateSpace\\Files.bat", None),  # Extra button
    ("Apps", "C:\\Program Files\\PrivateSpace\\Apps.bat", None)
]

for text, path, image in central_buttons:
    button = ttk.Button(central_frame, text=text, command=lambda p=path, i=image: (show_image(i) if i else None, open_file(p)), style="Rounded.TButton")
    button.pack(pady=10, fill=tk.X, expand=True)  # Resize the buttons

# Bottom buttons
bottom_frame = tk.Frame(root, bg="#2c7cf5")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

bottom_buttons = [
    ("Shutdown", "C:\\Program Files\\PrivateSpace\\Shutdown.exe", "C:\\Program Files\\PrivateSpace\\1.png"),
    ("Restart", "C:\\Program Files\\PrivateSpace\\Restart.exe", "C:\\Program Files\\PrivateSpace\\2.png"),
    ("Windows Loading", "C:\\Program Files\\PrivateSpace\\LoadWin.exe", "C:\\Program Files\\PrivateSpace\\3.png")
]

for text, path, image in bottom_buttons:
    button = ttk.Button(bottom_frame, text=text, command=lambda p=path, i=image: (show_image(i) if i else None, open_file(p)), style="Rounded.TButton")
    button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

root.mainloop()
