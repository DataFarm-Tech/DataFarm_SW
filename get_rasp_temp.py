from df_imports import *
from pkg import *
from db_connect import connect

pkg_install()
pkg_update()
pip_req()

os.system("clear")
run = True


############################################################################ 
######   GET ENV VARIABLES FROM SYSTEM LINUX KERNEL 
############################################################################


node_id = os.environ.get('NODEID')
hw_ver = os.environ.get('HW_VER')
sw_ver = os.environ.get('SW_VER')


############################################################################ 
######   FUNCTIONS TO GET SYSTEM PARAMETERS/METRICS/NETWORKING INFO  
############################################################################


def getPubIP4():
    command_output = subprocess.check_output("curl -s ifconfig.me", shell=True)
    command_output_str = command_output.decode("utf-8")
    return command_output_str

def getPriIP4():
    addrs = netifaces.ifaddresses(inter)
    ipv4_address = addrs[netifaces.AF_INET][0]['addr']
    ipv4_str = str(ipv4_address)
    return ipv4_str

def getGatewayIP4():
    gateway_address = netifaces.gateways()['default'][netifaces.AF_INET][0]
    return gateway_address

def getPriIP6():
    addrs = netifaces.ifaddresses(inter)
    ipv6_address = addrs[netifaces.AF_INET6][0]['addr']
    ipv6_str = str(ipv6_address)
    return ipv6_str

def getMAC():
    mac_address = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac_address[e:e+2] for e in range(0, 11, 2)])

def getLoc():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    loc_tuple = (latitude, longitude)
    loc = ','.join(map(str,loc_tuple))
    return loc

def getTime():
    current_time = datetime.datetime.now()
    return current_time



######################################################################################
######   FUNCTIONS FOR SYSTEM CHECKING EXAMPLE: CHECKING IF SYSTEM IS READY
######################################################################################



def check_internet(host="8.8.8.8", port=53, timeout=3):
    print("CONNECTING TO 8.8.8.8 (GOOGLE)")


    try:
        print("PENDING......")
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print(Fore.YELLOW+"[SUCCESS] return 1: ABLE TO CONNECT TO 8.8.8.8")
        print(Style.RESET_ALL)
        return True
    except socket.error:
        print(Fore.RED+"[ERROR] return 0: UNABLE TO CONNECT TO 8.8.8.8")
        print(Style.RESET_ALL)
        print("EXITING WITH RETURN VALUE 0")
        time.sleep(5)
        return False

def check_env():
    print("CHECKING ENVIRONMENT")
    print("PENDING......")
    time.sleep(5)

    if not node_id or not hw_ver or not sw_ver:
        print(Fore.RED+"[ERROR] return 0: ENVIRONMENTAL VARIABLES ARE NOT SET. ")
        print(Style.RESET_ALL)
        print("EXITING WITH RETURN VALUE 0")
        time.sleep(5)
        # print("NODEID=",node_id,"\n","HW_VER=",hw_ver,"\n","SW_VER=",sw_ver,"\n")
        return False

    else:
        print(Fore.YELLOW+"[SUCCESS] return 1: ENVIRONMENTAL VARIABLES INIT.")
        print(Style.RESET_ALL)
        time.sleep(5)
        return True
   


def insert_record(temp,node_id,hw_ver,sw_ver):

    ipv4_pub = getPubIP4()
    ipv4_pri = getPriIP4()
    ipv6_pri = getPriIP6()
    ipv4_gw = getGatewayIP4()
    mac_addr = getMAC()
    gps_loc = getLoc()
    time = getTime()

    add_record = ("INSERT INTO dirty_data "
                    "(mac_addr,ipv4_pri,ipv4_pub,ipv6_pri,ipv4_gw,node_id,time,hw_ver,sw_ver,gps_loc,temp) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data_record = (mac_addr,ipv4_pri,ipv4_pub,ipv6_pri,ipv4_gw,node_id,time,hw_ver,sw_ver,gps_loc,temp)

    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(add_record, data_record)
    cnx.commit()

    print(Fore.YELLOW+"[SUCCESS] return 1: ENTRY SENT.","\n")
    print(Style.RESET_ALL)
    print("TIME='"+str(time)+"'")
    print("NODEID='"+node_id+"'")
    print("SW_VER='"+sw_ver+"'")
    print("HW_VER='"+hw_ver+"'")
    print("IPV4 PUB='"+ipv4_pub+"'")
    print("IPV4 PRI='"+ipv4_pri+"'")
    print("MAC ADDRESS='"+mac_addr+"'")
    print("IPV6 PRI='"+ipv6_pri+"'")
    print("IPV4 GW='"+ipv4_gw+"'")
    print("TEMP='"+str(temp)+"'")
    print("GPS LOCATION='"+gps_loc+"'","\n")

def r_run():
    while True:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = int(f.read()) / 1000.0
            curr_time = datetime.datetime.now()
            temp = temp - 20
            insert_record(temp,node_id,hw_ver,sw_ver)
        time.sleep(60)


if not check_internet() or not check_env():
    run = False
else:
    run = True


if run:
    print(Fore.YELLOW+"[SUCCESS] return 1: RUNNING")
    print(Style.RESET_ALL)
    time.sleep(5)

    user_choice = input("Enter Interface:")
    if user_choice == "eth0":
        inter = "eth0"
        r_run()
    elif user_choice == "wlan0":
        inter = "wlan0"
        r_run()
    elif user_choice == "wlp58s0":
        inter = "wlp58s0"
        r_run()
    else:
        print("Incorrect Interface Type")

else:
    print(Fore.RED+"[ERROR] return 0: SYSTEM IS NOT READY TO RUN. ")
    print(Style.RESET_ALL)