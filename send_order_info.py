'''

Copyright 2021, Aninda Zaman, All rights reserved.

'''


from twilio.rest import Client
import time

#these are gotten from the Twilio client
account_sid = 'account_sid'
auth_token = 'account_auth_tok'
client = Client(account_sid, auth_token)

"""
message = client.messages.create\
    (
    from_='whatsapp:+14155238886',
    body='Testing.. Testing.. 123.. Testing... \n'
             ':: Visit: www.buddhi.tech/tong-to-me',
    to='whatsapp:+'
    )
"""

#message to be sent out for tong orders
def send_tong_order_info(x): #takes in a list
    #print("here")
    message = client.messages.create \
            (
            from_='whatsapp:+14155238886',
            body='*** TONG TO ME ***\n\n'
                 'NEW ORDER PLACED\n'
                 '\nName: ' + x[0] +
                 '\nPhone: ' + str(x[1]) +
                 '\nAddress: ' + x[2] +
                 '\nB&H Regular: ' + str(x[3]) +
                 '\nB&H Light: ' + str(x[4]) +
                 '\nB&H Switch: ' + str(x[5]) +
                 '\nB&H Platinum: ' + str(x[6]) +
                 '\nAny Notes: ' + str(x[7]) +
                 '\n\n ::: Process ASAP, Visit Google Sheet if needed :::',
            to='whatsapp:+'
        )
    time.sleep(2)
    message = client.messages.create\
        (
        from_='whatsapp:+14155238886',
        body='*** TONG TO ME ***\n\n'
             'NEW ORDER PLACED\n'
             '\nName: ' + x[0] +
             '\nPhone: '  + str(x[1]) +
             '\nAddress: ' + x[2] +
             '\nB&H Regular: ' + str(x[3]) +
             '\nB&H Light: ' + str(x[4]) +
             '\nB&H Switch: ' + str(x[5]) +
             '\nB&H Platinum: ' + str(x[6]) +
             '\nAny Notes: ' + str(x[7]) +
             '\n\n ::: Process ASAP, Visit Google Sheet if needed :::',
        to='whatsapp:+'
        )

#message to be sent out
def send_order_info(x): #takes in a list
    print("here")
    message = client.messages.create\
        (
        from_='whatsapp:+14155238886',
        body='NEW ORDER PLACED\n'
             '\nName: ' + x[0] +
             '\nPhone: '  + str(x[1]) +
             '\nAddress: ' + x[2] +
             '\n# of COVID Kits: ' + str(x[3]) +
             '\n\n ::: Process ASAP, Visit Google Sheet if needed :::',
        to='whatsapp:+'
        )

#print(message.sid)


'''

Copyright 2021, Aninda Zaman, All rights reserved.

'''
