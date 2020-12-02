import locale
from datetime import datetime
import firebase_admin
from firebase_admin import firestore

import pytz
from django.shortcuts import render

# Create your views here.
from HostelApp.firebase_init import FirebaseInit


def setmenu(request):
    if request.method == 'GET':
        return render(request, 'foodmenu/setmenu.html')
    else:
        breakfast = request.POST['breakfast']
        lunch = request.POST['lunch']
        evening = request.POST['evening']
        dinner = request.POST['dinner']
        date = request.POST['date']
        newDate = ''+date+' 12:00:00'
        dd = datetime.strptime(newDate, '%Y-%m-%d %H:%M:%S')
        if breakfast == "" or lunch == "" or evening == "" or dinner == "" or date == "":
            return render(request, 'foodmenu/setmenu.html', {'error': 'Field cannot be empty'})
        else:
            if validateMenu(date):
                return render(request, 'foodmenu/setmenu.html', {'error': 'Fee already updated in this date. Please contact the admin'})
            else:
                db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'foodmenu').document(str(dd))
                data = {
                    u'breakfast': breakfast,
                    u'lunch': lunch,
                    u'eve': evening,
                    u'dinner': dinner,
                    u'date': dd
                }
                db.set(data)
                return render(request, 'foodmenu/setmenu.html', {'success': 'Successfully updated'})

def validateMenu(date):
    db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'foodmenu')
    docs = db.where(u'date', u'==', date).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        return True



def todaydate():
    today = datetime.datetime.now(pytz.timezone('UTC')).replace(hour=0, minute=0,second=0, microsecond=0).timestamp()
    return today

def viewmenu(request, no):
    if request.method == 'GET':
        db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'foodmenu')
        docs = db.stream()
        result = []
        for doc in docs:
            result.append(doc.to_dict())

        return render(request, 'foodmenu/viewfoodmenu.html', {'result': result})

