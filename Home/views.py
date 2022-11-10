from django.shortcuts import render, redirect
from .forms import Transaction_form,Advert_form
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Transaction,Advert
from Account.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from datetime import timedelta,datetime
from django.core.serializers import serialize
import csv,json

from django.core.serializers import serialize

def init_payment(request):


    form = Transaction_form()

    if request.method == "POST":
        form = Transaction_form(request.POST)
        if form.is_valid():
            form.instance.user = request.user

            payment = form.save()
            messages.success(request, "Confirm payment!!!")
            return render(request, 'Home/payment.html',
                          {"payment": payment})

    return render(request, "Home/Trans.html", {"form": form})


def trans(request):
    past = datetime.today() - timedelta(minutes=20)

    cust = Transaction.objects.filter(user=request.user,date_created__lte=datetime.today(), date_created__gt=past)
    p = Paginator(cust, 3)
    page_number = request.GET.get('page')
    
    try:
        page = p.page(page_number)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)

    context = {"cust": page}
    return render(request, "Home/home-page.html", context)


def delete_single(request, cust_id):
    cust = Transaction.objects.filter(id=cust_id)
    cust.delete()
    return redirect(init_payment)

def delete_trans(request, trans_id):
    cust = Transaction.objects.filter(id=trans_id)
    cust.delete()
    return redirect(trans)


def log_out(request):
    logout(request)
    return redirect('sign_in')


def verify_payment(request, ref):
    payment = Transaction.objects.get(ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request,"Verification and payment succesful")
    else:
        messages.success(request,"Verification failed")
    return redirect(init_payment)




def advert(request):
    try:
        pro=request.user.profile
    except Profile.DoesNotExist:
        messages.info(request, "Profile must be created")
        return redirect("profile")
    form=Advert_form()
    if request.method=="POST":
        form=Advert_form(request.POST)
        if form.is_valid():
                form.instance.fullname=request.user.profile.fullname
                form.instance.email=request.user.email
                form.instance.phone=request.user.profile.phone
                form.save()
                send_mail(
                    "Advert "+str(request.user.profile.fullname),
                    str(form.cleaned_data.get("task")) +"  "+str(request.user.profile.phone),
                    request.user.email,
                    ['rcabiodun03@gmail.com','chukwukelvin141@gmail.com','nelsonnkana7@gmail.com'],
                )
                messages.info(request,"Form submitted!!")
                return redirect("advert")
    return render(request,"Home/advertisement.html",{"form":form})

'''
def printout(request):
    response =  (content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename= Transacations' + '.csv'
    writer = csv.writer(response)
    writer.writerow(['AMOUNT', 'EMAIL', 'USER', 'DATE', 'VERIFIED'])

    trans = Transaction.objects.all()

    for trans in trans:
        writer.writerow([trans.amount, trans.email, trans.user, trans.date_created, trans.verified])

    return response
'''