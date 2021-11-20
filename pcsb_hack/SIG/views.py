from django.shortcuts import redirect, render
from SIG.models import SIG, classroom,coursecontent,announcement
from django.contrib import messages
from accounts.models import ExtendedUser
from django.contrib.auth.models import auth,User
from accounts.views import login
def dash(request):
    if request.user.is_authenticated:
        u = request.user
        ur = ExtendedUser.objects.get(user=u)
        role = ur.Role
        fn = request.user.first_name
        uid = request.user.id
        sig = SIG.objects.all()
        participated = ExtendedUser.objects.get(user=u)
        use = User.objects.all()
        return render(request,'dashboard.html',{'fn':fn,'uid':uid,'role':role,'title':'DashBoard','sig':sig,'ps':participated.sigs,'len':len(participated.sigs),'user':use})
    else:
        return redirect(login) 

def addsig(request):
    if request.method == "POST":
        sname = request.POST['sname']
        sdomain = request.POST['sdomain']
        sdesc = request.POST['sdesc']
        sno = request.POST['sno']
        date = request.POST['date']
        mentor = request.POST['mentor']
        e = SIG.objects.create(signame=sname,sigdomain=sdomain,sigdesc=sdesc,numbers=sno,date=date,mentor=[mentor])
        e.save()
        messages.success(request,'Course saved Successfully')
        return redirect(dash)

def delete(request):
    id = request.GET['id']
    a = SIG.objects.get(id=id)
    a.delete()
    messages.warning(request,'Course deleted Successfully')
    return redirect(dash)

def edit(request):
    u = request.user
    ur = ExtendedUser.objects.get(user=u)
    role = ur.Role
    fn = request.user.first_name
    uid = request.user.id
    sid = request.POST['sid']
    sig = SIG.objects.get(id=sid)
    return render(request,'edit.html',{'fn':fn,'uid':uid,'role':role,'title':'edit panel','sig':sig})

def editsig(request):
    sid = request.POST['sid']
    sname = request.POST['sname']
    sdomain = request.POST['sdomain']
    sdesc = request.POST['sdesc']
    sno = request.POST['sno']
    date = request.POST['date']
    sig = SIG.objects.get(id=sid)
    sig.signame = sname
    sig.sigdesc = sdesc
    sig.sigdomain = sdomain
    sig.numbers = sno
    if date != "":
        sig.date = date
    sig.save()
    messages.success(request,'Course edited Successfully')
    return redirect(dash)

def sig(request):
    u = request.user
    fn = request.user.first_name
    ur = ExtendedUser.objects.get(user=u)
    role = ur.Role
    id = int(request.GET['id'])    
    sig = SIG.objects.get(id=id)
    uid = request.user.id
    if request.user.id not in ur.sigs and request.user.id not in sig.mentor :
        messages.error(request,'You are not a part of this sig')
        return redirect(dash)
    else:
        use = User.objects.all()
        cc = coursecontent.objects.all()
        an = announcement.objects.get(sigid=id)
        cl = classroom.objects.all()
        return render(request,'sigpage2.html',{'sig':sig,'user':use,'cc':cc,'id':id,'fn':fn,'uid':uid,'role':role,'an':an,'cl':cl})

def addcc(request):
    title = request.POST['title']
    desc = request.POST['desc']
    links = request.POST['links']
    id = int(request.POST['id'])
    c = coursecontent.objects.create(title=title,desc=desc,links=links,belongs=id)
    c.save()
    url = '/sig?id='+str(id)
    messages.success(request,'content updated')
    return redirect(url)

def cldelete(request):
    id = request.GET['id']
    a = SIG.objects.get(id=id)
    a.delete()
    messages.warning(request,'Course deleted Successfully')
    id = int(request.POST['id'])
    url = '/sig?id='+str(id)
    messages.success(request,'content updated')
    return redirect(url)

def addcl(request):
    title = request.POST['topicname']
    desc = request.POST['topicdesc']
    id = int(request.POST['id'])
    c = classroom.objects.create(title=title,desc=desc,sigid=id)
    c.save()
    url = '/sig?id='+str(id)
    messages.success(request,'content updated')
    return redirect(url)

def interested(request):
    u = request.user
    ur = ExtendedUser.objects.get(user=u)
    role = ur.Role
    fn = request.user.first_name
    uid = request.user.id
    return render(request,'interested.html',{'fn':fn,'role':role})

def interestedadd(request):
    name = request.POST['sname']
    domain = request.POST['sdomain']
    desc = request.POST['sdesc']
    mentor = request.POST['mentor']
    date = request.POST['date']
    print(name,domain,desc,mentor,date)
    return redirect(dash)