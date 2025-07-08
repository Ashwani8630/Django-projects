from django.contrib import admin
from django.urls import path
from home import views
# home/urls.py




urlpatterns = [
    path("",views.index,name='home'),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="service"),
    path('physics',views.physics,name='physics'),
    path('chemistry',views.chemistry,name='chemistry'),
    path('math',views.math,name='math'),
    path('literature',views.literature,name='literature'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('search/',views.search_view,name='logout')
   
    
]
