from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import ExtendedUser
from SIG.models import SIG
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            u = User.objects.get(email=email)
            user = auth.authenticate(username=u,password=password)
            if user is not None:
             auth.login(request,user)
             return redirect('/dashboard')
            else:
             messages.error(request,"Invalid Credentials")
             return redirect('/accounts/login')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/accounts/login')
    else:    
        return render(request,"login.html",{'title':'Login'})

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        # image = request.POST['image']
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email-id already taken')
            return redirect(login)
        else:    
            n = fname+"_"+lname
            user = User.objects.create_user(username=n, password=password, email=email, first_name=fname, last_name=lname)
            user.save();
            user = ExtendedUser.objects.create(user=n,Role=role)
            user.save()
            messages.success(request,'Signedup successfully')
            return redirect(login)
    else:    
        return render(request,"signup.html",{'title':'Sign Up'})

def logout(request):
    auth.logout(request)
    return redirect(login) 

def profile(request):
    u = request.user
    ur = ExtendedUser.objects.get(user=u)
    role = ur.Role
    ps = ur.sigs
    l=0
    sigs = SIG.objects.all()
    for i in sigs:
        if u.id in i.mentor:
            l+=1
    return render(request,'profile.html',{'role':role,'len':len(ps),'l':l}) 