import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_bat_file():
    # Отключаем кнопки
    button1.config(state=tk.DISABLED)
    
    bat_file_path = r"C:\Program Files\PrivateSpace\Starter.bat"
    # Запускаем .bat файл скрытно и ждем его завершения
    process = subprocess.Popen(bat_file_path, creationflags=subprocess.CREATE_NO_WINDOW)
    process.wait()  # Ждем завершения процесса
    
    # После завершения процесса показываем сообщение
    messagebox.showinfo("Private Space", "Готово! Private Space загрузится при следующей загрузке.")

# Создаем основное окно
root = tk.Tk()
root.title("Private Space")

# Устанавливаем иконку окна
icon_path = r"C:\Program Files\PrivateSpace\Icons\Main.ico"
root.iconbitmap(icon_path)

# Устанавливаем размер окна
root.geometry("700x500")

# Устанавливаем цвет фона
root.configure(bg='#0050b8')

# Отключаем возможность изменения размера окна
root.resizable(False, False)

# Создаем метку с текстом
label = tk.Label(root, text="Private Space", font=("Arial", 36, "bold"), bg='#0050b8', fg='white')
label.place(relx=0.5, rely=0.3, anchor='center')

# Вычисляем размеры и позиции для кнопок
button_width = 350  # 50% от ширины окна (700 / 2)
button_height = 40  # Высота кнопки
spacing = 20  # Расстояние между кнопками

# Создаем первую кнопку
button1 = tk.Button(root, text="Запустить", font=("Arial", 14), width=button_width // 10, height=button_height // 20, command=run_bat_file)
button1.place(x=(700 - button_width) // 2, y=350, width=button_width, height=button_height)

# Запускаем главный цикл обработки событий
root.mainloop()
