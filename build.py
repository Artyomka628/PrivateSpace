import os
import shutil
import subprocess
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

BASEDIR = r"C:\Program Files\PrivateSpace"


def success(msg: str):
    print(Fore.GREEN + "[OK] " + msg + Style.RESET_ALL)


def error(msg: str):
    print(Fore.RED + "[ERROR] " + msg + Style.RESET_ALL)


def info(msg: str):
    print(Fore.CYAN + "[INFO] " + msg + Style.RESET_ALL)


def run_cmd(cmd: list[str], show_output=False, cwd: str | None = None):
    try:
        if show_output:
            # Печатаем вывод в реальном времени голубым
            process = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(Fore.CYAN + line.rstrip() + Style.RESET_ALL)
            process.wait()
            if process.returncode != 0:
                raise RuntimeError("Команда завершилась ошибкой")
        else:
            result = subprocess.run(cmd, cwd=cwd)
            if result.returncode != 0:
                raise RuntimeError("Команда завершилась ошибкой")
    except Exception as e:
        error(f"Ошибка при выполнении: {' '.join(cmd)}\n{e}")
        sys.exit(1)


def check_python():
    info("Проверка Python...")
    result = shutil.which("python")
    if not result:
        error("Python не найден! Установите Python и добавьте его в PATH.")
        sys.exit(1)
    success("Python найден.")


def install_deps():
    info("Установка зависимостей...")
    run_cmd([sys.executable, "-m", "pip", "install", "--quiet", "pillow", "pyinstaller"])
    success("Зависимости установлены.")


def build_exe(name: str, icon: str, src: str):
    info(f"Сборка {name}.exe ...")
    run_cmd([
        "pyinstaller",
        "--noconfirm", "--onefile", "--windowed",
        "--icon", icon,
        "--uac-admin",
        src
    ], show_output=True)
    success(f"{name}.exe собран.")


def build_dir(name: str, icon: str, src: str):
    info(f"Сборка {name} ...")
    run_cmd([
        "pyinstaller",
        "--noconfirm", "--onedir", "--windowed",
        "--icon", icon,
        "--uac-admin",
        src
    ], show_output=True)
    success(f"{name} собран.")


def move_files():
    info("Перемещение файлов...")
    dist = os.path.join(BASEDIR, "dist")

    for exe in ["Launcher.exe", "LoadWin.exe", "Restart.exe", "Shutdown.exe", "PrivateSpace.exe"]:
        src = os.path.join(dist, exe)
        dst = os.path.join(BASEDIR, exe)
        if os.path.exists(src):
            shutil.move(src, dst)

    success("Файлы перемещены.")


def cleanup():
    info("Очистка временных папок...")
    for folder in ["build", "dist"]:
        path = os.path.join(BASEDIR, folder)
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
    success("Очистка завершена.")


def main():
    check_python()
    install_deps()

    build_exe("Launcher", os.path.join(BASEDIR, "Icons", "Main.ico"), os.path.join(BASEDIR, "Launcher.py"))
    build_exe("LoadWin", os.path.join(BASEDIR, "Icons", "win.ico"), os.path.join(BASEDIR, "LoadWin.py"))
    build_exe("Restart", os.path.join(BASEDIR, "Icons", "restart.ico"), os.path.join(BASEDIR, "Restart.py"))
    build_exe("Shutdown", os.path.join(BASEDIR, "Icons", "shutdown.ico"), os.path.join(BASEDIR, "Shutdown.py"))
    build_exe("PrivateSpace", os.path.join(BASEDIR, "Icons", "Main.ico"), os.path.join(BASEDIR, "PrivateSpace.py"))

    move_files()
    cleanup()

    success("Сборка завершена успешно!")
    time.sleep(5)


if __name__ == "__main__":
    main()
