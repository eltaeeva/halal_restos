from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login_user, name = 'login'),
    path('register/', views.register_user, name = 'register'),
    path('logout/', views.logout_user, name='logout'),
    path('about_us/', views.about, name = 'about_us'),
    path('restos_all/', views.restos, name = 'restos_all'),
    path('mosques_all/', views.mosques, name = 'mosques'),
    path('mosque_detail/', views.mosque_details, name='mosque_detail'),
    path('resto_detail/', views.resto_detail, name = 'resto_detail'),
]