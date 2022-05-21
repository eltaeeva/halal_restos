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
    path('mosque_detail/<int:id>', views.mosque_detail, name='mosque_detail'),
    path('resto_detail/<int:id>', views.restos_detail, name = 'restos_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/success/<str:text>', views.SearchSuccessView.as_view(), name='search_success'),
    path('searchh/', views.SearchView2.as_view(), name='searchh'),
    path('searchh/success2/<str:text>', views.SearchSuccessView2.as_view(), name='search_success2'),
    path('favourite/<int:pk>', views.FavouriteView, name="favourite_restos"),
    path('favourites/', views.post_favourite_list, name='post_favourite_list'),
    path('submit_review/<int:resto_id>/', views.submit_review, name='submit_review'),
    path('donations/', views.donations, name='donations'),
]