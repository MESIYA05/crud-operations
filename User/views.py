from django.shortcuts import render , redirect
from.models import Usersinfo
from.forms import userform


# Create your views here.

def getuser(request):
    user = Usersinfo.objects.all()
    return render(request,"/userdetail.html",context={"user":user})




def createuser(request):
    if request.method =="POST":
        post=userform(request.POST)
        if post.is_valid():
            post.save()
            return redirect('/user')
    formss=userform()
    return render(request,"/adduser.html",context={"formss":formss})


def edituser(request,id):
    user=Usersinfo.objects.get(id=id)
    if request.method == "POST":
        put=userform(request.POST,instance=user)
        if  put.is_valid():
            put.save()
            return redirect('/user')
    return render(request,"/edituser.html",context={"user":user})


def deleteuser(request,id):
    user=Usersinfo.objects.get(id=id)
    if request.method == "POST":
       user.delete()
       return redirect('/user')
    return render(request, "/userdelete.html",context={"user":user.Fullname})
