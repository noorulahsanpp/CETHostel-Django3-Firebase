from datetime import date, timedelta
from datetime import datetime
import time

import pytz
from django.shortcuts import render

# Create your views here.
from HostelApp.firebase_init import FirebaseInit

w = []
def getuser(admission_number):
    docw = FirebaseInit.store.collection(u'registered')
    rr = []
    for x in range(1):
        docw = docw.where(u'admission_number', u'==', admission_number).stream()
        for doc in docw:
            print(doc.get('name'))
            rr.append(doc.get('name'))

    for doc in rr:
        print(doc)

def viewsick(request):
    if request.method == 'GET':
        # today = date.today()
        #
        # aa = today.strftime("%Y-%m-%d")
        # newDate = '' + aa + ' 12:00:00'
        # dd = datetime.strptime(newDate, '%Y-%m-%d %H:%M:%S')
        # millisec = dd.timestamp() * 1000
        # getuser('LH002')
        import datetime
        dt = datetime.datetime.now()
        startdt = dt + timedelta(-1)
        newdt = dt + timedelta(1)
        dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        docs = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'sick').where(u'date', u'>=', startdt).where(u'date', u'<=', newdt).stream()
        result = []
        breakfast = []
        for doc in docs:
            result.append(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')

            # result.append(doc.get('a'))
            # q = doc.to_dict()

        # w = q['a']
        return render(request, 'sick/viewsick.html', {'result': result, 'date': date.today(), 'breakfast':len(breakfast)})


def todaydate():
    today = datetime.datetime.now(pytz.timezone('UTC')).replace(hour=0, minute=0,second=0, microsecond=0).timestamp()
    return today



