import json

import requests
from firebase_admin import messaging

serverToken = 'AAAAV2T8TEY:APA91bFsiEsolm7K1DP-adrzsUmtcpy4JTXAvz2sI3C5euSuyJFn1XKu-mnBpxLHx3fNUbbN3W2wlLB4MYnqKwW1-wN9Qgy6K9oOmzstW5tu6VQ2JLrc-18y5cCZF-biTF-7RNd6ooq-'
deviceToken = 'fU25nVuNQHOWzInVdaHP5V:APA91bG6FFqqmxWtg6-duWSayekjpo24TyjclHgG-hPiqPHWrOmhn7gbOIEPLxPilygW-NKVqxpiuHpppL3jqPJ6CbHPQZgOfKcN3V9jVKg02OAEPkQ1GDtt7-EmE6t2kbHHeGG7d7vD'

# headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'key=' + serverToken,
#     }

# body = {
#   "to": "/topics/LH",
#   "notification": {
#     "title": "Test",
#     "body": "New news story available.",
#       "image":'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'
#   },
#   "data": {
#     "story_id": "story_12345"
#   }
# }
# response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
# print(response.status_code)
#
# print(response.json())

# ////////////////////////////////////////////////////////

def send_to_token():
    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.
    registration_token = 'fU25nVuNQHOWzInVdaHP5V:APA91bG6FFqqmxWtg6-duWSayekjpo24TyjclHgG-hPiqPHWrOmhn7gbOIEPLxPilygW-NKVqxpiuHpppL3jqPJ6CbHPQZgOfKcN3V9jVKg02OAEPkQ1GDtt7-EmE6t2kbHHeGG7d7vD'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]

# ///////////////////////////////////////////////////////////////////
def cloudMessaging(message):


    serverToken = 'AAAAV2T8TEY:APA91bFsiEsolm7K1DP-adrzsUmtcpy4JTXAvz2sI3C5euSuyJFn1XKu-mnBpxLHx3fNUbbN3W2wlLB4MYnqKwW1-wN9Qgy6K9oOmzstW5tu6VQ2JLrc-18y5cCZF-biTF-7RNd6ooq-'
    deviceToken = 'fU25nVuNQHOWzInVdaHP5V:APA91bG6FFqqmxWtg6-duWSayekjpo24TyjclHgG-hPiqPHWrOmhn7gbOIEPLxPilygW-NKVqxpiuHpppL3jqPJ6CbHPQZgOfKcN3V9jVKg02OAEPkQ1GDtt7-EmE6t2kbHHeGG7d7vD'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
    }

    body = {
        'notification': {'title': 'Sending push form python script',
                         'body': message,
                         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Google_Lens_-_new_logo.png"
                         },
        'to':
            deviceToken,
        'priority': 'high',
        #   'data': dataPayLoad,
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())