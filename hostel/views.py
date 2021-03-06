import json

import requests
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib import auth
from datetime import datetime, timedelta

# Create your views here.
from django.template.defaultfilters import upper
from firebase_admin import messaging

from HostelApp.firebase_init import FirebaseInit
from hostel.models import MessSec


def home(request):
    return render(request, 'hostel/home.html')

def adminLogin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('adminHome')
        else:
            return render(request, 'hostel/admin_login.html', {'error': 'Username or Password does not match'})
    else:
        return render(request, 'hostel/admin_login.html')

def test(request):
    import datetime
    dt = datetime.datetime.now()
    startdt = dt + timedelta(-1)
    newdt = dt + timedelta(0)
    dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
    docs = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'attendance').where(u'date', u'>=',
                                                                                                     startdt).where(
        u'date', u'<=', newdt).stream()
    result = []
    absents = []
    total = 0;
    for doc in docs:
        result.append(doc.to_dict())
        # print(f'{doc.id} => {doc.to_dict()}')
        absents.append(doc.get('absents'))
        print(doc.get('absents'))
        print(doc.get('total_absentees'))
        total = doc.get('total_absentees')
    return render(request, 'hostel/testhome.html', {'total': total})
def contacts(request):
    return render(request, 'hostel/contacts.html')

def invoice(request):
    import datetime
    date = datetime.date.today()
    return render(request, 'hostel/invoice.html', {'date': date})

def mailcompose(request):
    return render(request, 'mailbox/compose.html')

def mailread(request):
    return render(request, 'mailbox/read-mail.html')

def mailbox(request):
    return render(request, 'mailbox/mailbox.html')

def invoiceprint(request):
    import datetime
    date = datetime.date.today()
    return render(request, 'hostel/invoice-print.html', {'date': date})

def contactus(request):
    return render(request, 'hostel/contact-us.html')

def calendar(request):
    return render(request, 'hostel/calendar.html')

def studentdetails(request, adno):
    db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'users').where(u'admission_no', u'==', adno)
    result = []
    docs = db.stream()
    if request.method == 'GET':

        for doc in docs:
            result.append(doc.to_dict())
            print(doc.to_dict())
        return render(request, 'hostel/studentdetails.html', {'result': result})

def adminHome(request):
    import datetime
    dt = datetime.datetime.now()
    startdt = dt + timedelta(-1)
    newdt = dt + timedelta(0)
    dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
    docs = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'attendance').where(u'date', u'>=',
                                                                                                     startdt).where(
        u'date', u'<=', newdt).stream()
    result = []
    absents = []
    total = 0;
    for doc in docs:
        result.append(doc.to_dict())
        # print(f'{doc.id} => {doc.to_dict()}')
        absents.append(doc.get('absents'))
        print(doc.get('absents'))
        print(doc.get('total_absentees'))
        total = doc.get('total_absentees')
    return render(request, 'hostel/testhome.html', {'total': total})

def MHHome(request):
    return render(request, 'hostel/MHhome.html')

def LHHome(request):
    return render(request, 'hostel/LHhome.html')

def landingPage(request):
    return render(request, 'hostel/login.html')

def viewcomplaints(request):
    result = []
    db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'complaints')
    docs = db.stream()
    for doc in docs:
        result.append(doc.to_dict())
    if request.method == 'GET':
        return render(request, 'hostel/viewcomplaints.html', {'result': result})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'hostel/loginuser.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'hostel/loginuser.html', {'error':'Invalid username or password'})
        else:
            login(request, user)
            return redirect('home')

def loginMessSec(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = auth.authenticate(username=username, password=request.POST['password'])
        if user is not None:
            messSec = get_object_or_404(MessSec, username=username)
            auth.login(request, user)
            if messSec.hostel == 'LH':
                return redirect('LHHome')
            else:
                return redirect('MHHome')
        else:
            return render(request, 'hostel/loginMessSec.html', {'error': 'Username or Password does not match'})
    else:
        return render(request, 'hostel/loginMessSec.html')

def adminSignup(request):
    if request.method == 'GET':
        return render(request, 'hostel/adminSignup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'hostel/adminSignup.html', {'error': 'Username already taken'})
        else:
            return render(request, 'hostel/adminSignup.html', {'error': 'Password does not match'})


def signupMessSec(request):
    if request.method == 'GET':
        return render(request, 'hostel/signupMessSec.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                messSec = MessSec()
                messSec.username = request.POST['username']
                messSec.hostel = request.POST['hostel']
                messSec.save()
                return redirect('home')
            except IntegrityError:
                return render(request, 'hostel/signupMessSec.html', {'error': 'Username already taken'})
        else:
            return render(request, 'hostel/signupMessSec.html', {'error': 'Password does not match'})

@login_required
def logoutAdmin(request):
    # POST is used here because browsers load all the anchor tags in the website background to load pages faster
    if request.method == 'POST':
        logout(request)
        return render(request, 'hostel/login.html')

def absentees(request):
    if request.method == 'GET':
        import datetime
        dt = datetime.datetime.now()
        startdt = dt + timedelta(-1)
        newdt = dt + timedelta(0)
        dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        docs = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'attendance').where(u'date', u'>=',startdt).where(u'date', u'<=', newdt).stream()
        result = []
        absents = []
        total= 0;
        for doc in docs:
            result.append(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            absents.append(doc.get('absents'))
            print(doc.get('absents'))
            print(doc.get('total_absentees'))
            total = doc.get('total_absentees')
        return render(request, 'hostel/absentees.html', {'total': total, 'absents':absents})

def studentregistration(request):
    if request.method == 'GET':
        return render(request, 'hostel/studentregistration.html')
    else:
        adnumber = upper(request.POST['adnumber'])
        block = upper(request.POST['block'])
        dept = request.POST['dept']
        hostel = request.POST['hostel']
        name = request.POST['name']
        room = request.POST['room']
        sem = request.POST['sem']

        if adnumber == "" or block == "" or dept == "" or hostel == "" or name == "" or room == "" or sem == "":
            return render(request, 'hostel/studentregistration.html', {'error': 'Field cannot be empty'})
        else:
            if(checkStudent(adnumber)):
                return render(request, 'hostel/studentregistration.html', {'error': 'Student already registered'})
            else:
                db = FirebaseInit.store.collection(u'registered').document(
                    str(adnumber))
                data = {
                    u'admission_no': adnumber,
                    u'block': block,
                    u'department': dept,
                    u'hostel': hostel,
                    u'name': name,
                    u'room': room,
                    u'semester': sem,
                    u'app_reg': 'no'
                }
                db.set(data)
                return render(request, 'hostel/studentregistration.html', {'success': 'Student Successfully registered'})


# def checkStudent(adnumber):
#     db = FirebaseInit.store.collection(u'registered')
#     docs = db.where(u'admission_number', u'==', adnumber).stream()
#     for doc in docs:
#         print(f'{doc.id} => {doc.to_dict()}')
#         return True

def sendNotification(request):
    import datetime
    dt = datetime.datetime.now()
    dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
    if request.method == 'POST':

        db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'notification').document()
        data = {
            u'topic': request.POST['topic'],
            u'description': request.POST['description'],
            u'date': dt,
        }
        db.set(data)
        cloudMessaging(request.POST['topic'], request.POST['description'])
        return render(request, 'hostel/sendnotification.html', {'success':'Notificaiton successfully pushed'})
    else:
        return render(request, 'hostel/sendnotification.html')
def checkStudent(adnumber):
    db = FirebaseInit.store.collection(u'registered').document(adnumber)
    doc = db.get()
    if doc.exists:
        return True


def allinmates(request):
    db = FirebaseInit.store.collection(u'registered').where(u'hostel', u'==', 'LH')
    result = []
    docs = db.stream()
    if request.method == 'GET':

        for doc in docs:
            result.append(doc.to_dict())
        return render(request, 'hostel/allinmates.html', {'result': result})
    else:

        semester = request.POST['sem']
        block = request.POST['block']
        department = request.POST['dept']
        room = request.POST['room']
        if semester != "" and block != "" and department != "":
            docs = db.where(u'semester', u'==', semester).where(u'block', u'==', block).where(u'department', u'==',
                                                                                              department).stream()
        elif semester != "" and block != "" and department == "":
            docs = db.where(u'semester', u'==', semester).where(u'block', u'==', block).stream()
        elif semester != "" and block == "" and department != "":
            docs = db.where(u'semester', u'==', semester).where(u'department', u'==', department).stream()
        elif block != "":
            docs = db.where(u'block', u'==', block).stream()
        elif department != "":
            docs = db.where(u'department', u'==', department).stream()
        elif semester != "":
            docs = db.where(u'semester', u'==', semester).stream()
        elif room != "":
            docs = db.where(u'room', u'==', room).stream()

        for doc in docs:
            result.append(doc.to_dict())

        return render(request, 'hostel/allinmates.html', {'result': result})

def viewallstudents(request):
    db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'users')
    result = []
    docs = db.stream()
    if request.method == 'GET':

        for doc in docs:
            result.append(doc.to_dict())
        return render(request, 'hostel/viewallstudents.html', {'result': result})
    else:

        semester = request.POST['sem']
        block = request.POST['block']
        department = request.POST['dept']
        room = request.POST['room']
        if semester != "" and block != "" and department != "":
            docs = db.where(u'semester', u'==', semester).where(u'block', u'==', block).where(u'department', u'==', department).stream()
        elif semester != "" and block != "" and department == "":
            docs = db.where(u'semester', u'==', semester).where(u'block', u'==', block).stream()
        elif semester != "" and block == "" and department != "":
            docs = db.where(u'semester', u'==', semester).where(u'department', u'==', department).stream()
        elif block != "":
            docs = db.where(u'block', u'==', block).stream()
        elif department != "":
            docs = db.where(u'department', u'==', department).stream()
        elif semester != "":
            docs = db.where(u'semester', u'==', semester).stream()
        elif room != "":
            docs = db.where(u'room', u'==', room).stream()

        for doc in docs:
            result.append(doc.to_dict())

        return render(request, 'hostel/viewallstudents.html', {'result': result})

def cloudMessaging(topic, message):
    serverToken = 'AAAAV2T8TEY:APA91bFsiEsolm7K1DP-adrzsUmtcpy4JTXAvz2sI3C5euSuyJFn1XKu-mnBpxLHx3fNUbbN3W2wlLB4MYnqKwW1-wN9Qgy6K9oOmzstW5tu6VQ2JLrc-18y5cCZF-biTF-7RNd6ooq-'
    deviceToken = 'fU25nVuNQHOWzInVdaHP5V:APA91bG6FFqqmxWtg6-duWSayekjpo24TyjclHgG-hPiqPHWrOmhn7gbOIEPLxPilygW-NKVqxpiuHpppL3jqPJ6CbHPQZgOfKcN3V9jVKg02OAEPkQ1GDtt7-EmE6t2kbHHeGG7d7vD'

    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

    body = {
      "to": "/topics/LH",
      "notification": {
        "title": topic,
        "body": message,
          # "image":'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'
      },
      "data": {
        # "story_id": "story_12345"
      }
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())

def viewnotification(request):
    result = []
    db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'notification')
    docs = db.stream()
    for doc in docs:
        result.append(doc.to_dict())
    if request.method == 'GET':
        return render(request, 'table/data.html', {'result': result})

def pushnot():
    topic = 'LH'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)