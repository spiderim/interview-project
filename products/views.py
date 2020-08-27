from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product ,Like,Comment
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from accounts.models import UserProfile

def home(request):
    qs=Product.objects.all()
    user=request.user
    context={
    'qs':qs,
    'user':user,
    }

    return render(request,'products/home.html',context)

@login_required(login_url="/accounts/login")
def mainhome(request):
    ab=UserProfile.objects.filter(user=request.user)
    k=""
    for obj in ab:
        k=obj.institute    
    qs=Product.objects.filter(institute=k)
    user=request.user
    context={
    'qs':qs,
    'user':user,
    'institute':k,
    
    }
    return render(request,'products/mainhome.html',context)


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.user.last_name=='Fourth Year' or request.user.last_name=='Third Year':
            if request.POST.get('compname') and request.POST.get('body'):
                product = Product()
                product.compname=request.POST.get('compname')
                product.body=request.POST.get('body')
                product.pub_date=timezone.datetime.now()
                product.hunter=request.user
                ab=UserProfile.objects.filter(user=request.user)
                for obj in ab:
                    product.institute=obj.institute
                    print(obj.institute)
                product.save()
                return redirect('/products/'+str(product.id))
            else:
                return render(request,'products/create.html',{'error':'something not added !'})

        else:
            return render(request,'products/create.html',{'error':'Only 3rd or 4th year can create post!'})


    else:
        return render(request,'products/create.html')


def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    comments=Comment.objects.all().filter(post_id=product_id).order_by('-date_comment')
    if request.method =='POST':
        comment=Comment()
        comment.message=request.POST.get('message')
        comment.user_id=request.user.first_name
        comment.post_id=product
        comment.date_comment=timezone.now()
        comment.save()
        messages.success(request, 'Comment sucessfully added !')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'products/detail.html',{'product':product,'comments':comments})
    
    

@login_required(login_url="/accounts/signup")
def like_post(request):
    user=request.user
    if request.method=='POST':
        productid=request.POST.get('productid')
        product_obj=Product.objects.get(id=productid)
        #if user.username!= product_obj.hunter.username:

        if user in product_obj.liked.all():

            product_obj.liked.remove(user)
        else:
            product_obj.liked.add(user)

        like,created=Like.objects.get_or_create(user=user,product_id=productid)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        like.save()
        if like.value=='Like':
            return redirect('liked')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

        #else:
            #messages.success(request, "You cannot like yourself !")
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

       



@login_required(login_url="/accounts/signup")
def user_detail(request):
    first_name=request.user.first_name
    last_name=request.user.last_name
    email=request.user.email
    userextend=UserProfile.objects.filter(user=request.user)
    user_posts=Product.objects.filter(hunter=request.user)
    context={
    'first_name':first_name,
    'last_name':last_name,
    'email':email,
     'user_posts':user_posts,
     'user_extend':userextend,
    }
    return render(request,'products/user_detail.html',context)

@login_required(login_url="/accounts/signup")
def update(request):
    userextend=UserProfile.objects.filter(user=request.user)
    if request.method =='POST':
        if(len(request.POST.get('username'))<3):
            messages.error(request, 'Username must have at least 3   chracter!')
            return redirect('update')
        try:
            user=User.objects.get(username=request.POST.get('username'))
            if(request.user.username==user.username):
                raise Exception()
            messages.error(request, 'username is already taken !')
            return redirect('update')
        except:
            owner=request.user
            owner.username=request.POST.get('username')
            owner.first_name=request.POST.get('first_name')
            owner.last_name=request.POST.get('last_name')
            owner.email=request.POST.get('email')
            owner.save()
            k=""
            for obj in userextend:
                obj.phone_num=request.POST.get('phone_num')
                obj.age=request.POST.get('age')
                obj.save()
            messages.success(request, 'Profile details updated.')
            return redirect('user_detail')
        
    else:
        first_name=request.user.first_name
        last_name=request.user.last_name
        email=request.user.email
        age=0
        phone_num=""
        for obj in userextend:
            phone_num=obj.phone_num
            age=obj.age
        context={
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'age':age,
        'phone_num':phone_num,
         }

        return render(request,'products/update.html',context)

    
def delete_post(request,product_id=None):
    post_to_delete=Product.objects.get(id=product_id)
    post_to_delete.delete()
    messages.success(request, 'sucessfully deleated')
    return redirect('user_detail')


@login_required
def editpost(request,product_id):
   
    product= get_object_or_404(Product,id=product_id)

    if request.method=='POST':
        if request.POST.get('compname') and request.POST.get('body'):
            product.compname=request.POST.get('compname')
            product.body=request.POST.get('body')
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            return render(request,'products/create.html',{'error':'something not added !'})
    else:
        return render(request,'products/edit.html',{'product':product})

def liked(request):
    product=Product.objects.filter(liked=request.user)
    return render(request,'products/liked.html',{'product':product})