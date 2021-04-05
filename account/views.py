from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
import pyrebase
from django.contrib import auth

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
authe = firebase.auth()
database = firebase.database()


# Create your views here.
def home_view(request):
    return render(request,'account/home.html')

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email1']
            phone = request.POST['phone']
            id_prof = request.FILES['idproof']
            password = request.POST['password']
            password1 = request.POST['password1']

            # if password == password1:
            #     user = authe.create_user_with_email_and_password(username,password)
                # uid = user['localId']

            try:
                user = User.objects.get(username=username)
                return redirect("/account/register/")

                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
                user.save()
            except:
                pass
            user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
            user.save()
            account = Account(user=user, phone = phone, id_proof = id_prof)
            account.save()
            messages.success(request, 'registered successfully')

            return redirect("/account/login/")
    else:
        messages.warning(request, 'invalid input')   
        return redirect('/account/login')

    return render(request, "account/register.html")

def logins_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        
        

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                    return redirect('/')
            messages.success(request, 'logged-in successfully') 
            return redirect("/quiz/python/")
        else:
            messages.warning(request, 'invalid username and password')
            return redirect("/account/login/")
        # user = authe.sign_in_with_email_and_password(username, password)
        # session_id = user['idToken']
        # request.session['uid'] = str(session_id)
    return render(request,'account/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'logged-out successfully')

    return redirect("/account/home/")

def redirect_view(request):
    return redirect("/account/home/")