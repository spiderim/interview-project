
from django.contrib import admin
from django.urls import path,include
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainhome/',views.mainhome,name='mainhome'),
    path('',views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),

]
