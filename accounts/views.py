from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                user=User.objects.get(username=request.POST.get('username'))
                return render(request,'accounts/signup.html',{'error':'Username has already taken !'})
            except User.DoesNotExist:
                if(len(request.POST.get('password1'))<6):
                    return render(request,'accounts/signup.html',{'error':'atleast 6 chracter required for password !'})
                elif(len(request.POST.get('username'))<3):
                    return render(request,'accounts/signup.html',{'error':'Username must have at least 3 chracter!'})
                elif(len(request.POST.get('first_name'))<1):
                    return render(request,'accounts/signup.html',{'error':'Name not added!'})
                elif(request.POST.get('institute')==None or request.POST.get('institute')==""):
                    return render(request,'accounts/signup.html',{'error':'institute not added!'})
                elif(request.POST.get('last_name')==None or request.POST.get('last_name')==""):
                    return render(request,'accounts/signup.html',{'error':'year not added!'})
                elif(request.POST.get('email')==None or request.POST.get('email')==""):
                    return render(request,'accounts/signup.html',{'error':'email not added!'})

                user=User.objects.create_user(request.POST.get('username'),request.POST.get('email'),password=request.POST.get('password1'))
                user.first_name=request.POST.get('first_name')
                user.last_name=request.POST.get('last_name')
                user.save()
                institute=request.POST.get('institute')
                if(request.POST.get('phone_num')==None or request.POST.get('phone_num')==""):
                    phone_num="0000000000"
                else:
                    phone_num=request.POST.get('phone_num')
                if(request.POST.get('age')==None or request.POST.get('age')==""):
                    age=0
                else:
                    age=request.POST.get('age')
                user_profile=UserProfile()
                user_profile.institute=institute
                user_profile.age=age
                user_profile.phone_num=phone_num
                user_profile.user=user
                user_profile.save()
                auth.login(request,user)
                return redirect('mainhome')
        else:
            return render(request,'accounts/signup.html',{'error':'password not match !'})
    else:
        return render(request,'accounts/signup.html')


	

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('mainhome')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect !'})

    else:
        return render(request,'accounts/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')