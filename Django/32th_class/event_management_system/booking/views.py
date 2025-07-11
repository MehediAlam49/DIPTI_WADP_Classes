from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,hashers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from booking.models import *

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            EventUserModel.objects.create_user(
                profile_image=profile_image,
                username=username,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                password=confirm_password,
            )
            return redirect('loginPage')
    return render(request, 'signupPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('loginPage')


def home(request):
    bookingData = EventBookingModel.objects.filter(created_by = request.user)
    return render(request, 'home.html', {'bookings':bookingData})
def myBooking(request):
    bookingData = EventBookingModel.objects.filter(created_by = request.user)
    return render(request, 'myBooking.html', {'bookings':bookingData})
def profile(request):
    return render(request, 'profile.html')


def addBooking(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_description = request.POST.get('event_description')
        event_date = request.POST.get('event_date')
        event_type = request.POST.get('event_type')
        status = request.POST.get('status')

        EventBookingModel.objects.create(
            created_by = request.user,
            event_title=event_title,
            event_description=event_description,
            event_date=event_date,
            event_type=event_type,
            status=status,
        )
        return redirect('myBooking')
    return render(request, 'addBooking.html')


def editBooking(request,id):
    return render(request, 'editBooking.html')
def viewBooking(request,id):
    return render(request, 'viewBooking.html')
def deleteBooking(request,id):
    return redirect('myBooking')


def changePassword(request):
    return render(request, 'changePassword.html')
def changeStatus(request,id):
    return render(request, 'changeStatus.html')