#this will only work with Oshud Delivery

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

from send_order_info import send_order_info

# tells the program what scopes to look into
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# these are the credentials from the API control panel, also shared with the .json file
credentials = ServiceAccountCredentials.from_json_keyfile_name('Oshud_Secret.json', scope)

# authorize with the credential before to start accessing information
gc = gspread.authorize(credentials)

# open the exact sheet with the proper title
sheet = gc.open('Oshud Delivery (COVID-19 Kit): Responses').sheet1

result = sheet.get_all_records()


def get_active_rows():
    # this is how you get all the active rows, you shall have to subtract 1 because of the header row...
    max_rows = len(sheet.get_all_values())
    max_rows = max_rows - 1

    return max_rows

#figure out which of the rows' info haven't been confirmed
def determine_new_rows(x): #takes in the number of active rows
    file = open("order_totz.txt", "r")
    num = int(file.readline())
    file.close()

    return x - num

def tong_order_prep():
    x = 0
    return x

#prepare the individual orders to send out to be confirmed
#x represents active rows
#y represensts the new rows since last check
def covid_order_prep(x, y):
    #this gets the difference between current active rows and previously dealth with rows
    #ie: however many new orders have come in
    y = x - y
    while y < x:
        print("x, y: ", x, y)
        #print(result)
        order_spec = []

        order_spec.append(result[y].get('Name'))
        order_spec.append(result[y].get('Phone'))
        order_spec.append(result[y].get('Address'))
        order_spec.append(result[y].get('Pick How Many COVID-19 Kit You Need'))

        print(order_spec)

        send_order_info(order_spec)
        y = y + 1

    file = open("order_totz.txt", "w")
    file.write(str(y))
    file.close()

    return x