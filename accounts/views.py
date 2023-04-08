from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid details',extra_tags='error')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already taken', extra_tags='error')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already taken', extra_tags='error')
                return redirect('register')
            else:
               user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save();
               print('user created')
        else:
            print('password not match')
            messages.error(request,'password not matched', extra_tags='error')
        return redirect('register', {'messages': messages.get_messages(request)})
    else:
         return render(request, 'registration.html')
