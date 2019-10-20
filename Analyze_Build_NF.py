"""
Created on Sat Oct 19 17:31:03 2019

@author: Rishabh
"""
import pandas as pd
from pyfcm import FCMNotification
import sys


if len(sys.argv)<2:
    print("Invalid Usage. Correct Usage : python MySQLConnection.py type_code[1/2/3] [BCAST MSG if typecode=1]")
    sys.exit(1)

type_code = int(sys.argv[1])

if type_code==1 and len(sys.argv)<3:
    print("Invalid Usage. BCAST MSG is mandatory for type_code=1")
    sys.exit(1)
elif type_code==1:
    bcast_msg = str(sys.argv[2])

df = pd.read_csv('~/WINZO/Data.csv')
#df.head()
#df.info()

#Configuration
APP_API_KEY = ""
FCM_EXPCTD_LEN = 152

df["gender2"] = df["gender"]
df["gender2"].replace({"Female":"women","Male":"men"},inplace=True)
df["smfPG"].replace({5:6},inplace=True)

#df.head()
#print(df['fCM'].tail())
push_service = FCMNotification(api_key=APP_API_KEY)

succ_cnt = 0
fail_cnt = 0

for ind in df.index:
    FCM_Reg_ID = df['fCM'][ind]
    GUID = df['GUID'][ind]
    NF = "Hey "+str(df['Name'][ind].split()[0])+", Do you know that people who liked games "+str(df['fmfPG'][ind])+" & "+str(df['smfPG'][ind])+" also liked game "+str((df['fmfPG'][ind]*df['smfPG'][ind]) - 7)+" Play Now."
    if type_code==1:
        NF = "Hey "+str(df['Name'][ind].split()[0])+bcast_msg
        
#    print("User :",GUID)
#    print("FCM Reg ID :",FCM_Reg_ID)
#    print("Notification :",NF)
    if len(FCM_Reg_ID)==FCM_EXPCTD_LEN:
        registration_id = FCM_Reg_ID
        message_title = "WINZO Misses You!"
        if type_code==1:
            message_title = "Broadcast from WINZO!"
        message_body = NF
        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
        if result['success']==1 and result['failure']==0:
            succ_cnt+=1
        else:
            fail_cnt+=1
    
print(succ_cnt,"messages sent successfully &",fail_cnt,"failed");
