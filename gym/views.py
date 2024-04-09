from django.shortcuts import render, redirect, HttpResponse
from gym.models import Plan, Plan_features
from purchase.models import Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as xlogout
# Create your views here.
def home(request):
    p=Plan.objects.all()
    p_f=Plan_features.objects.all()
    return render(request, 'index.html', {'p':p, 'p_f':p_f})

def ilogin(request):
    return render(request, 'login.html')

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        passx = request.POST.get("passx")
        user = authenticate(username=uname, password=passx)
        if user is not None:
            login(request, user)

            # messages.success(request, "Logged in")
            return redirect('home')
        else:
            # messages.info(request,'invalid credentials')
            return redirect('ilogin')  
    return redirect('home') 

def logout(request):
    xlogout(request)
    return redirect('home')

def signup(request):
    return render(request, 'signup.html')

def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("uname")
        email = request.POST.get('email')
        passx = request.POST.get("passx")
        passy = request.POST.get("passy")
        
        if passx==passy:
        

            u = User.objects.create_user(username=uname, email=email, password=passy)
            u.first_name = fname
            u.last_name = lname

            u.save()
            # messages.success(request, "Your account has been created")
            print('success')
            return redirect("home")
    else:

        return HttpResponse("404 error") 

def join_plan(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            try:
                b=Booking.objects.get(user_id=request.user.pk)
                return redirect('my_plan') 
            except:
                p=Plan.objects.get(pk=id)
                # b=Booking.objects.filter(user_id=request.user.pk)
                # print(b)
                return render(request, 'join_plan.html', {'p':p}) 
           
                          
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("Please Login For Join Plan")  

def handle_join_plan(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            phone=request.POST.get('phone')
            img=request.FILES['id_image']
            

            
            b=Booking(user_id=request.user.pk, plan_id=id, phone=phone, id_proof=img)
            b.save()
            return redirect('home') 

        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error") 

def my_plan(request):
    if request.user.is_authenticated: 
        try:          
            b=Booking.objects.get(user_id=request.user.pk)
            return render(request, 'my_plan.html', {'b':b})
        except:
            return redirect('home')            
    else:
        return HttpResponse("404 error")

def edit_plan(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            b=Booking.objects.get(pk=id)
            p=Plan.objects.all()
            # b=Booking.objects.filter(user_id=request.user.pk)
            # print(b)
            return render(request, 'edit_plan.html', {'p':p, 'b':b})        
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error")  

def handle_edit_plan(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            p=request.POST.get('pname')
            phone=request.POST.get('phone')
            img=request.FILES['id_image']
            
            b=Booking.objects.get(pk=id)
            b.plan_id=p
            b.phone=phone
            b.id_proof=img
            b.save()
            return redirect('home')        
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error")        

def delete_plan(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            b=Booking.objects.get(pk=id)
            b.delete()
            return redirect('home')   

        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error")    
