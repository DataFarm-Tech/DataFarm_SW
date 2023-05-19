from df_imports import *

def connect():
    cnx = mysql.connector.connect(
        user='sql12618889', 
        password='KKleVPC9cK', 
        host='sql12.freemysqlhosting.net', 
        database='sql12618889')
    return cnx


# def drop_clean():
#     cnx = connect()
#     cursor = cnx.cursor()
#     delete_query = "DELETE FROM clean_data"
#     cursor.execute(delete_query)
#     cnx.commit()
#     cursor.close()
#     cnx.close()

# def drop_dirty():
#     cnx = connect()
#     cursor = cnx.cursor()
#     delete_query = "DELETE FROM dirty_data"
#     cursor.execute(delete_query)
#     cnx.commit()
#     cursor.close()
#     cnx.close()

# def create_tables():
#     cnx = connect()
#     cursor = cnx.cursor()
#     delete_query = "CREATE TABLE dirty_data (mac_addr varchar(255),ipv4_pri varchar(255),ipv4_pub varchar(255),ipv6_pri varchar(255),ipv4_gw varchar(255),node_id varchar(255),time datetime,hw_ver varchar(255),sw_ver varchar(255),gps_loc varchar(255),temp float)"
#     cursor.execute(delete_query)
#     cnx.commit()
#     cursor.close()
#     cnx.close()