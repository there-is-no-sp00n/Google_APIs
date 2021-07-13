'''

Copyright 2021, Aninda Zaman, All rights reserved.

'''


#this will only work with Tong To Me B&H
#need to add this module to le_sheets_essentials.py

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

from send_order_info import send_tong_order_info

# tells the program what scopes to look into
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# these are the credentials from the API control panel, also shared with the .json file
credentials = ServiceAccountCredentials.from_json_keyfile_name('TongToMe_Secret.json', scope)

# authorize with the credential before to start accessing information
gc = gspread.authorize(credentials)

# open the exact sheet with the proper title
sheet = gc.open('Tong To Me (B&H): Responses').sheet1

result = sheet.get_all_records()


def get_active_rows():
    # this is how you get all the active rows, you shall have to subtract 1 because of the header row...
    max_rows = len(sheet.get_all_values())
    max_rows = max_rows - 1

    return max_rows

#figure out which of the rows' info haven't been confirmed
def determine_new_rows(x): #takes in the number of active rows
    file = open("order_totz_tong_to_me.txt", "r")
    num = int(file.readline())
    file.close()

    return x - num


#prepare the individual orders to send out to be confirmed
#x represents active rows
#y represensts the new rows since last check
def tong_order_prep(x, y):
    #this gets the difference between current active rows and previously dealth with rows
    #ie: however many new orders have come in
    y = x - y
    while y < x:
        print("x, y: ", x, y)
        #print(result)
        order_spec = []

        order_spec.append(result[y].get('Name'))
        cust_num = str(result[y].get('Phone'))
        if(cust_num[0] != '8'):
            cust_num = '+880' + cust_num
            order_spec.append(cust_num)
        else:
            cust_num = '+' + cust_num
            order_spec.append(cust_num)
        order_spec.append(result[y].get('Address'))
        cig_holder = result[y].get('B&H Regular')
        #print('johnny' + cig_holder + 'karate')
        #print(type(cig_holder))
        if(cig_holder != ""):
            order_spec.append(str(cig_holder))
        else:
            order_spec.append(0)
        cig_holder = result[y].get('B&H Light')
        if (cig_holder != ""):
            order_spec.append(str(cig_holder))
        else:
            order_spec.append(0)
        cig_holder = result[y].get('B&H Switch')
        if (cig_holder != ""):
            order_spec.append(str(cig_holder))
        else:
            order_spec.append(0)
        cig_holder = result[y].get('B&H Platinum')
        if (cig_holder != ""):
            order_spec.append(str(cig_holder))
        else:
            order_spec.append(0)
        cig_holder = result[y].get('Any notes?')
        if (cig_holder != ""):
            order_spec.append(result[y].get('Any notes?'))
        else:
            order_spec.append('N/A')
        #order_spec.append(result[y].get('Pick How Many COVID-19 Kit You Need'))

        print(order_spec)

        send_tong_order_info(order_spec)
        y = y + 1
        file = open("order_totz_tong_to_me.txt", "w")
        file.write(str(y))
        file.close()
        #break



    return x


'''

Copyright 2021, Aninda Zaman, All rights reserved.

'''
