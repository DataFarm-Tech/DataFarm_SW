import os


def set_env(nodeid, userid, sw_ver, hw_ver):
    # Creating a map
    map = {
    "NODEID": nodeid,
    "USERID": userid,
    "SW_VER": sw_ver,
    "HW_VER": hw_ver
    }
    for key, value in map.items():
        os.system("echo '"+key+" = "+value+"' | sudo tee -a /etc/environment")

valid = True
serialnum = input("Enter S/N\n")

if serialnum.count("|") != 3:
    valid = False
    print("Error, incorrect number of delimiters")
else:
    serialnum_sub = serialnum.split("|")
    if serialnum_sub[2].count(".") != 1 and serialnum_sub[3].count("." != 1):
        valid = False
        print("Error, incorrect number of delimiters")
    else:
        print("No Errors")
        
if valid:
    set_env(serialnum_sub[0],serialnum_sub[1],serialnum_sub[2],serialnum_sub[3])
    os.system("sudo reboot")



