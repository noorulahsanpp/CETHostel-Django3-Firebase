from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import requests
import json

# Create your views here.
from firebase_admin import messaging

from HostelApp.firebase_init import FirebaseInit
from HostelApp.test import cloudMessaging, send_to_token


@login_required
def feehome(request):
    return render(request, 'fee/feehome.html')

@login_required()
def postfee(request):
    if request.method == 'GET':
        return render(request, 'fee/postfee.html')
    else:
        veg = request.POST['veg']
        nonveg = request.POST['nonveg']
        month = request.POST['month']
        due = request.POST['duedate']
        common = request.POST['common']
        rent = request.POST['rent']
        if veg == "" or nonveg == "" or month == "" or due == "" or common == "" or rent == "":
            return render(request, 'fee/postfee.html', {'error': 'Field cannot be empty'})
        else:
            if validateFee(month):
                return render(request, 'fee/postfee.html', {'error': 'Fee already updated in this date. Please contact the admin'})
            else:
                db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'fee').document(month)
                data = {
                    u'veg': veg,
                    u'nonveg': nonveg,
                    u'date': month,
                    u'duedate': due,
                    u'common': common,
                    u'rent': rent
                }
                db.set(data)
                cloudMessaging('Fee updated')
                # send_to_token()
                return render(request, 'fee/postfee.html', {'success': 'Successfully updated'})

@login_required
def viewfee(request):
    if request.method == 'GET':
        db = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'fee')
        docs = db.stream()
        result = []
        for doc in docs:
            result.append(doc.to_dict())

        return render(request, 'fee/viewfee.html', {'result': result})

dbFeeValidation = FirebaseInit.store.collection(u'inmates').document(u'LH').collection(u'fee')

def validateFee(month):
    docs = dbFeeValidation.where(u'date', u'==', month).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        return True

def paidfee(request):
    if request.method == 'GET':
        return render(request, 'fee/paidfee.html')


