"""
Created on Sat Oct 19 15:31:50 2019

@author: Rishabh
"""

import mysql.connector
import csv
import sys


if len(sys.argv)<2:
    print("Invalid Usage. Correct Usage : python MySQLConnection.py type_code[1/2/3] [Name if typecode=2]")
    sys.exit(1)

type_code = int(sys.argv[1])

try:
    print("Establishing Connection")
    connection = mysql.connector.connect(host="",
                                         user="",
                                         passwd="",
                                         auth_plugin='')
    print("Established Connection. Running Query.")
    if type_code==1:
        #Broadcast Notification
        mySql_select_Table_Query = "SELECT * FROM WINZO_PS.usr_act_info"
    elif type_code==2:
        #User Specific Notification
        if len(sys.argv)!=3:
            print("Invalid Usage. Name is mandatory if type_code = 2")
            sys.exit(1)
        user_name = str(sys.argv[2])
        mySql_select_Table_Query = "SELECT * FROM WINZO_PS.usr_act_info WHERE Name = '" + user_name + "';"
    elif type_code==3:
        #Notify Dormant Users
        mySql_select_Table_Query = """
        SELECT * FROM WINZO_PS.usr_act_info WHERE lastSeen < NOW() - INTERVAL 90 DAY;
        """
    else:
        print("Invalid Usage. Correct Usage : python MySQLConnection.py type_code[1/2/3]")
        sys.exit(1)
        
    print(mySql_select_Table_Query)
    
    cursor = connection.cursor()
    
    last_days = '90'
    
    result = cursor.execute(mySql_select_Table_Query)
    print("Query Executed.")
    records = cursor.fetchall()
finally:
    connection.close()
    
    
print("Total number of rows in table is: ", cursor.rowcount)
#print(type(records))
#print(type(records[0]))
#print(type(records[0][0]))
#print("\nPrinting each name in record")
#for row in records:
#    print(row)

csv_file_path = '~/WINZO/Data.csv'
# Continue only if there are rows returned.
if records:
    # New empty list called 'output'. This will be written to a file.
    output = list()

    # The row name is the first entry for each entity in the description tuple.
    column_names = list()
    for i in cursor.description:
        column_names.append(i[0])

    output.append(column_names)
    for row in records:
        output.append(row)

    # Write result to file.
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in output:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query")
    
cursor.close()
