
from django.urls import path,include
from . import views
from django.conf.urls import url



urlpatterns = [

    path('create',views.create,name='create'),
    path('<int:product_id>',views.detail,name='detail'),
    path('likes/',views.like_post,name='like_post'),
    path('info',views.user_detail,name='user_detail'),
    path('update',views.update,name='update'),
    path('delete/<int:product_id>',views.delete_post,name='delete'),
    path('edit/<int:product_id>',views.editpost,name='editpost'),
    path('liked',views.liked,name='liked'),
    


] 