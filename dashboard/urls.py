from django.urls import path,include
#now import the views.py file into this code
from . import views

urlpatterns=[
   path('',views.Login,name='login'),
   path('signup/',views.SignUP,name='signup'),
   path('getnewface/',views.newface,name='newface'),
   path('verifyface/',views.verifyface,name='verifyface'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('logout/',views.logout,name="logout"),
   path('download/',views.download,name="download"),
   path('add_profile/',views.add_profile,name='add_profile'),
   path('profiles/', views.profiles, name= 'profiles'),
   path('edit_profile/<int:id>/',views.edit_profile,name='edit_profile'),
   path('delete_profile/<int:id>/',views.delete_profile,name='delete_profile')
  ]