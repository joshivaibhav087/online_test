from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Quiz
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
import binascii
import os
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from django.contrib import messages
import pyrebase
from django.contrib import auth
import json
# from firebase import firebase
firebaseConfig = {
'apiKey': "AIzaSyBDBRPFSBSiYAPj-9yggYxtYyv8HjvtLXo",
'authDomain': "online-test-83d73.firebaseapp.com",
'databaseURL': "https://online-test-83d73-default-rtdb.firebaseio.com",
'projectId': "online-test-83d73",
'storageBucket': "online-test-83d73.appspot.com",
'messagingSenderId': "674632990124",
'appId': "1:674632990124:web:0f66cb8b7b5b558e71ce09",
'measurementId': "G-8C84V7GKYN"
}
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()



# Create your views here.
from Crypto.Cipher import AES
import base64
def python_view(request):
    if request.method == "POST":
        ans1 = request.POST['question1']
        ans2 = request.POST['question2']
        ans3 = request.POST['question3']
        ans4 = request.POST['question4']
        ans5 = request.POST['question5']
        ans6 = request.POST['question6']
        ans7 = request.POST['question7']
        ans8 = request.POST['question8']
        ans9 = request.POST['question9']
        ans10 = request.POST['question10']
        count=0
        if ans1 == "ans1":
            count+=1
        if ans2 == "ans2":
            count+=1
        if ans3 == "ans3":
            count+=1
        if ans4 == "ans4":
            count+=1
        if ans5 == "ans5":
            count+=1
        if ans6 == "ans6":
            count+=1
        if ans7 == "ans7":
            count+=1
        if ans8 == "ans8":
            count+=1
        if ans9 == "ans9":
            count+=1
        if ans10 == "ans10":
            count+=1
        percentage = (count/10)*100
        my_formatter = "{0:.2f}"
        output = my_formatter.format(percentage)
        result = Quiz(user = request.user, python=output)
        result.save()
        data = {"python score":result.python}
        data2 = json.dumps(data)
        database.child("users").child("details").set(data2)
        return redirect("/quiz/java/")
        
    return render(request, "quiz/python_quiz.html")

def java_view(request):
    if request.method == "POST":
        ans1 = request.POST['question1']
        ans2 = request.POST['question2']
        ans3 = request.POST['question3']
        ans4 = request.POST['question4']
        ans5 = request.POST['question5']
        ans6 = request.POST['question6']
        ans7 = request.POST['question7']
        ans8 = request.POST['question8']
        ans9 = request.POST['question9']
        ans10 = request.POST['question10']
        count=0
        if ans1 == "ans1":
            count+=1
        if ans2 == "ans2":
            count+=1
        if ans3 == "ans3":
            count+=1
        if ans4 == "ans4":
            count+=1
        if ans5 == "ans5":
            count+=1
        if ans6 == "ans6":
            count+=1
        if ans7 == "ans7":
            count+=1
        if ans8 == "ans8":
            count+=1
        if ans9 == "ans9":
            count+=1
        if ans10 == "ans10":
            count+=1
        percentage = (count/10)*100
        my_formatter = "{0:.2f}"
        output = my_formatter.format(percentage)        
        print(ans1,ans2,ans3)
        result = Quiz.objects.filter(user=request.user).last()
        result.java = output
        result.save()
        data = {"java score":result.java}
        data2 = json.dumps(data)
        database.child("users").child("details1").set(data2)
        return redirect("/quiz/c/")
    return render(request, "quiz/java_quiz.html")

def c_view(request):
    if request.method == "POST":
        ans1 = request.POST['question1']
        ans2 = request.POST['question2']
        ans3 = request.POST['question3']
        ans4 = request.POST['question4']
        ans5 = request.POST['question5']
        ans6 = request.POST['question6']
        ans7 = request.POST['question7']
        ans8 = request.POST['question8']
        ans9 = request.POST['question9']
        ans10 = request.POST['question10']
        count=0
        if ans1 == "ans1":
            count+=1
        if ans2 == "ans2":
            count+=1
        if ans3 == "ans3":
            count+=1
        if ans4 == "ans4":
            count+=1
        if ans5 == "ans5":
            count+=1
        if ans6 == "ans6":
            count+=1
        if ans7 == "ans7":
            count+=1
        if ans8 == "ans8":
            count+=1
        if ans9 == "ans9":
            count+=1
        if ans10 == "ans10":
            count+=1
        percentage = (count/10)*100
        my_formatter = "{0:.2f}"
        output = my_formatter.format(percentage)
        print(ans1,ans2,ans3)
        result = Quiz.objects.filter(user=request.user).last()
        result.c = output
        result.save()
        data = {"c score":result.c}
        data2 = json.dumps(data)
        # final_data = data2.replace('\\','"')
        # print(final_data)
        database.child("users").child("details2").set(data2)
        pk = request.user.id
        return redirect(f"/quiz/score/{pk}/")
    return render(request, "quiz/c_quiz.html")

def score_view(request,pk):
    user = User.objects.filter(id=pk).last()
    score = Quiz.objects.filter(user=user).last()

    return render(request, "quiz/score.html",{'score':score})