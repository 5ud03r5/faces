
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

from .views import ChangePassword, Login, Logout, CreateView, CreateComment, Messages, Register, SendMessage, userProfile, updateProfile


urlpatterns = [
        
        
        path('', views.mainPage, name="main_page"),
        path('login/', views.Login.as_view(), name='login'),
        path('logout/', views.Logout.as_view(), name='logout'),
        path('register/', views.Register.as_view(), name="register"),
#        path('profile/<str:pk>', UserProfile.as_view(), name="profile"),
        path('profile/<str:pk>', views.userProfile, name="profile"),
#        path('add_post/', views.AddPost.as_view(), name="add_post"),
        path('change_password/<str:pk>', views.ChangePassword.as_view(), name="change_password"),
        path('messages/', views.Messages.as_view(), name="messages"),
        path('conversation/<str:pk>', views.SendMessage.as_view(), name="conversation"),
        path('profiles/', views.Profiles.as_view(), name='profiles'),
        path('delete/<str:pk>', views.DeleteObject.as_view(), name='delete'),
        path('update_profile/<str:pk>', views.updateProfile, name='update_profile'),
        
        
 
]