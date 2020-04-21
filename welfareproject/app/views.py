from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View
from .models import Userregistrationmodel,Thoughtsmodel,Addeventmodel
# Create your views here.

class index(View):
    def get(self,request):
       return render(request,"index.html")
    def post(self,request):
        un=request.POST.get('a1')
        pd=request.POST.get('a2')
        ad=request.POST.get('a3')
        try:
         if un=='ganesh' and pd =='grpspk' and ad=='ADMIN':
            request.session['status']=True
            return redirect('admin_login')
         elif ad=='USER':
            Userregistrationmodel.objects.get(username=un,password=pd)
            request.session['status']=True
            return redirect('user_login')
         else:
            messages.error(request,"invalid username or password!!!!! TRY AGAIN...")
            return redirect('main')
        except Userregistrationmodel.DoesNotExist:
            messages.error(request,"invalid username or password or usertype !!!!!!!!!!!!!!TRY AGAIN..")
            return redirect('main')

def user_login(request):
    return render(request,"user_login_page.html")
def admin_login(request):
    return render(request,"admin_login_page.html")

class user_reg(View):
    def get(self,request):
        return render(request,"user_reg.html")
    def post(self,request):
        un=request.POST.get('b1')
        psd=request.POST.get('b2')
        ads=request.POST.get('b3')
        eml=request.POST.get('b4')
        cnt=request.POST.get('b5')
        dte_f_br=request.POST.get('b6')
        cmpynm=request.POST.get('b7')
        status='pending'
        Userregistrationmodel(username=un,password=psd,address=ads,email=eml,contactno=cnt,date_of_birth=dte_f_br,companyname=cmpynm,status=status).save()
        messages.success(request,"Registered Successfully!!!!!!!")
        return redirect('user_reg')

class add_though(View):
    def get(self,request):
        return render(request,'add_though.html')
    def post(self,request):
        un=request.POST.get('c1')
        des=request.POST.get('c2')
        cnt=request.POST.get('c3')
        Thoughtsmodel(t_usernmae=un,description=des,t_contno=cnt).save()
        messages.success(request,"ADDED SUCCESSFULLY!!!!!!!!!!!!!!")
        return redirect('add_though')


def view_though(request):
    ts=Thoughtsmodel.objects.all()
    return render(request,"view_though.html",{"data":ts})


class add_event(View):
    def get(self,request):
        return render(request,"add_event.html")
    def post(self,request):
        un=request.POST.get('d1')
        srtdt=request.POST.get('d2')
        enddt=request.POST.get('d3')
        desp=request.POST.get('d4')
        contn=request.POST.get('d5')
        Addeventmodel(e_username=un,startdate=srtdt,enddate=enddt,descr=desp,contactno=contn).save()
        messages.success(request,"event successfully added!!!!!!!!!!!!!!!")
        return redirect('add_event')


def view_event(request):
    am=Addeventmodel.objects.all()
    return render(request,"view_event.html",{"data":am})


def user_logout(request):
    request.session['status']=False
    return redirect('main')

def adm_logout(request):
    request.session['status']=False
    return redirect('main')


def approval_users(request):
    return render(request,"approval_users.html",{"data":Userregistrationmodel.objects.filter(status='pending')})


def delete_data(request):
    dno=request.GET.get('dname')
    Userregistrationmodel.objects.filter(username=dno).update(status='rejected')
    return redirect('approval_users')


def update_data(request):
    dno=request.GET.get('dname')
    Userregistrationmodel.objects.filter(username=dno).update(status='accepted')
    return redirect('approval_users')


def accepted_users(request):
    res=Userregistrationmodel.objects.filter(status='accepted')
    return render(request,"accepted_users.html",{"data":res})


def rejected_users(request):
    res=Userregistrationmodel.objects.filter(status='rejected')
    return render(request,"rejected_users.html",{"data":res})