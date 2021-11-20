from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.

def signin(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            print("Take another username")
        elif User.objects.filter(email=email).exists():
            print("Take another email")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save();
            print("User created")

    else:
        return render(request, 'signin.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            print("invalid credentials")


    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)