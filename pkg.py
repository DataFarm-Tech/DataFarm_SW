import os

def pkg_update():
    os.system("sudo apt update && sudo apt upgrade -y && sudo apt autoclean -y && sudo apt autoremove -y")
def pkg_install():
    os.system("sudo apt install python3")
    os.system("sudo apt install python3-pip")
def pip_req():
    os.system("pip install -r requirements.txt")


