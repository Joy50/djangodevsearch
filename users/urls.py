from django.urls import path
from .views import profiles,userProfile,loginUser,logoutUser,registerUser

urlpatterns = [
    path('login/',loginUser,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('register/',registerUser,name="register"),
    path('',profiles,name="profiles"),
    path('profile/<str:pk>',userProfile,name="user-profile"),
]
