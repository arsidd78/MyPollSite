from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('',views.IndexView.as_view(),name='home'),
    path('detail/<str:pk>/',views.DetailView.as_view(),name='detail'),    
    path('vote/<str:pk>/',views.Vote,name='vote'),
    path('result/<str:pk>/',views.ResultView.as_view(),name='result'),
    path('authentication/',views.Authenticate,name='authenticate'),
    path('login/',views.login,name='login'),
    path('add_question/',views.Add_question.as_view(),name='add_question'),
    path('signup/',views.SignUp,name='sign_up_form'),
    path('registration/',views.Registration,name='registration'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/profile/',views.Profile,name='profile'),
    path('signout/',views.signout,name='sign-out'),
]