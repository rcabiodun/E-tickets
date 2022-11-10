from django.urls import path
from . import views


urlpatterns = [
    path('',views.Signup,name="sign_up"),
    path('login/',views.Signin,name="sign_in"),
    path('profile/',views.Profile_reg,name="profile")


]