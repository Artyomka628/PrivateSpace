import tkinter as tk
from tkinter import ttk
from ctypes import windll
import subprocess
import os

def remove_window_buttons(window):
    GWL_STYLE = -16
    WS_SYSMENU = 0x00080000
    WS_MINIMIZEBOX = 0x00020000
    WS_MAXIMIZEBOX = 0x00010000

    hwnd = windll.user32.GetParent(window.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
    style &= ~WS_SYSMENU
    style &= ~WS_MINIMIZEBOX
    style &= ~WS_MAXIMIZEBOX
    windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)

    SWP_NOSIZE = 0x0001
    SWP_NOMOVE = 0x0002
    SWP_NOZORDER = 0x0004
    SWP_FRAMECHANGED = 0x0020

    windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0,
                               SWP_NOSIZE | SWP_NOMOVE | SWP_NOZORDER | SWP_FRAMECHANGED)

def update_progress():
    current_value = progress_var.get()
    next_value = current_value + 1
    progress_var.set(next_value)

    if next_value == 100:
        label2.config(text="It looks like Windows failed to restart. You will need to do it manually.")
    else:
        root.after(100, update_progress)

def run_restart_script():
    global restart_started
    if not restart_started:
        bat_file_path = os.path.join(os.getcwd(), 'C:\\Program Files\\PrivateSpace\\Restart.bat')
        subprocess.Popen(bat_file_path, creationflags=subprocess.CREATE_NO_WINDOW)
        restart_started = True

root = tk.Tk()
root.title("Restart")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#343deb")
root.update_idletasks()
remove_window_buttons(root)
root.attributes("-topmost", True)

# Set the icon
icon_path = "C:\\Program Files\\PrivateSpace\\Icons\\restart.ico"
root.iconbitmap(icon_path)

label = tk.Label(root, text="Private Space", font=("Helvetica", 36), bg="#343deb", fg="white")
label.pack(pady=20)

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", variable=progress_var, maximum=100)
progress_bar.pack(pady=20)

label2 = tk.Label(root, text="Restarting...", font=("Helvetica", 14), bg="#343deb", fg="white")
label2.pack(pady=20)

restart_started = False
run_restart_script()

update_progress()

root.mainloop()
