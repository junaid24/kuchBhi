import socket
import mysql.connector
import csv
import sys

HOST, PORT = '192.168.12.30', 8889 #Server IP and port
#var =  #URI from server contains fcm token
data_age = 57
data_guid = "506C4415-AD4A-4947-E1E5-392BFEE6CB29"
data_last_seen = "2019-09-11 02:13:29"
data_curBal = 538
data_totEar = 923
data_totSpend = 742
data_gftAmt = 616
data_email = "tortor.nibh.sit@justofaucibus.ca"
data_lat = 48.27032
data_lon = 45.19534
data_lvl = 1
data_mobile = "91-229-120-8116"
data_gndr = "Male"
data_fmfPG = 4
data_smfPG = 6
data_occ = "Salaried"

def connectionEstablish(hst,usr,pas,auth):
    try:
        print("Establishing Connection")
        connection = mysql.connector.connect(host=hst,
                                         user=usr,
                                         passwd=pas,
                                         auth_plugin=auth) 
        print("Established Connection.")
        return connection
    finally:
        return None

def insertDB(name,token,connection):
    try:
        print("Running Query for : ", name)
        queryData = "'" + str(name) + "'" + "," + str(data_age) + "," + "'" + str(data_last_seen) + "'" + "," + "'" + str(data_guid) + "'" + "," + str(data_curBal) + "," +  str(data_totEar) + "," + str(data_totSpend) + "," + str(data_gftAmt) + "," + "'" + str(data_occ) + "'" + "," + "'" + str(data_email) + "'" + "," + str(data_lat) + "," + str(data_lon) + "," + str(data_lvl) + "," + "'" + str(token) + "'" + "," + "'" + str(data_mobile) + "'" + "," + "'" + str(data_gndr) + "'" + "," + str(data_fmfPG) + "," + str(data_smfPG) 
        print(queryData)
        mySql_select_Table_Query = """
        INSERT INTO `WINZO_PS`.`usr_act_info`
        (`Name`,
        `Age`,
        `lastSeen`,
        `GUID`,
        `currBal`,
        `totalEar`,
        `totalSpend`,
        `giftAmt`,
        `Occupation`,
        `email`,
        `latitude`,
        `longitude`,
        `level`,
        `fCM`,
        `mobile`,
        `gender`,
        `fmfPG`,
        `smfPG`)
        VALUES
        (""" + queryData + """);
        """
        print(mySql_select_Table_Query)
        cursor = connection.cursor()
        #    last_days = '90'  
        result = cursor.execute(mySql_select_Table_Query)
        connection.commit()
        print("Query Executed.")
        #    records = cursor.fetchall()
        #finally:
        #connection.close()
    finally:
        print("terminated")
        return None

def findVal(data,var,delm):
    reqDataStrt = data.find(var) 
    if( reqDataStrt == -1 ):
        return
    reqDataStrt += len(var);
    reqDataEnd = data.find(delm,reqDataStrt)
    print(data[reqDataStrt:reqDataEnd])    
    return data[reqDataStrt:reqDataEnd]

def clientCode(data,connection):
    return 2

def main():
    print("Establishing Connection")
    connection = mysql.connector.connect(host="",
                                     user="",
                                     passwd="",
                                     auth_plugin='')
    print("Established Connection.")
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print(f'Serving HTTP on port {PORT} ...')
    while True:
        client_connection, client_address = listen_socket.accept()
        request_data = client_connection.recv(1024)
        rr = request_data.decode('utf-8')
        #clientCode(rr,mysqlConnection)
        fcm = findVal(rr,"fcm_token=","?")
        #fcm = findVal(data,"fcm_token=","?")
        name = findVal(rr,"name="," ")
        print(fcm)
        print(name)
        insertDB(name,fcm,connection)
        print(rr)
        http_response = b"""\
HTTP/1.1 200 OK


"""
        client_connection.sendall(http_response)
        client_connection.close()
    connection.close()

main()
