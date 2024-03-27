from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view( template_name='registration/logout.html', next_page=None), name='logout'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form2/', views.form_page, name='form2'),
    path('form/', views.form_page2, name='form'),
    path('result/', views.result_page, name='result'),
]
