import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_bat_file():
    # Disable buttons
    button1.config(state=tk.DISABLED)
    
    bat_file_path = r"C:\Program Files\PrivateSpace\Starter.bat"
    # Launch the batch file hidden and wait for it
    process = subprocess.Popen(bat_file_path, creationflags=subprocess.CREATE_NO_WINDOW)
    process.wait()  # Wait for the process to finish
    
    # After the process finishes, show a message
    messagebox.showinfo("Private Space", "Done! Private Space will launch on the next boot.")

# Create the main window
root = tk.Tk()
root.title("Private Space")

# Set the window icon
icon_path = r"C:\Program Files\PrivateSpace\Icons\Main.ico"
root.iconbitmap(icon_path)

# Set the window size
root.geometry("700x500")

# Set the background color
root.configure(bg='#0050b8')

# Prevent window resizing
root.resizable(False, False)

# Create the title label
label = tk.Label(root, text="Private Space", font=("Arial", 36, "bold"), bg='#0050b8', fg='white')
label.place(relx=0.5, rely=0.3, anchor='center')

# Calculate sizes and positions for the buttons
button_width = 350  # 50% of the window width (700 / 2)
button_height = 40  # Button height
spacing = 20  # Spacing between buttons

# Create the launch button
button1 = tk.Button(root, text="Launch", font=("Arial", 14), width=button_width // 10, height=button_height // 20, command=run_bat_file)
button1.place(x=(700 - button_width) // 2, y=350, width=button_width, height=button_height)

# Run the main event loop
root.mainloop()
