from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import *
from django.db.models import *

from database.models import Restaurants, Mosque, ReviewRating
from .forms import CreateUserForm, ProfileForm, ReviewForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'login')
def index(request):
    return render(request, 'profileapp/home.html')

@login_required(login_url = 'login')
def about(request):
    return render(request, 'profileapp/about_us.html')

@login_required(login_url = 'login')
def restos(request):
    restos = Restaurants.objects.all()
    return render(request, 'profileapp/restos_all.html', {'restos': restos})

@login_required(login_url = 'login')
def resto_detail(request):
    return render(request, 'profileapp/resto_detail.html')

@login_required(login_url = 'login')
def mosques(request):
    mosques = Mosque.objects.all()
    return render(request, 'profileapp/mosques_all.html', {'mosques': mosques})

@login_required(login_url = 'login')
def mosque_details(request):
    return render(request, 'profileapp/mosque_details.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'profileapp/profile.html', context)

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong password or username')
            return redirect('login')
    return render(request, 'profileapp/login_page.html')

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Аккаунт успешно создан!')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Неверные данные!')
            return redirect('register')

    context = {'form': form}
    return render(request, 'profileapp/register_page.html', context)

@login_required(login_url = 'login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')

@login_required(login_url = 'login')
def restos_detail(request, id):
    restos = Restaurants.objects.get(id=id)
    reviews = ReviewRating.objects.filter(resto_id=id)

    get_favourites = get_object_or_404(Restaurants, id=id)

    is_fav = False
    if get_favourites.favourite.filter(username=request.user.username).exists():
        is_fav = True

    return render(request,'profileapp/rest_detail.html', {'rest':restos, 'reviews': reviews, 'is_fav': is_fav})

def mosque_detail(request, id):
    mosques = Mosque.objects.get(id=id)
    return render(request, 'profileapp/mosque_details.html', {'mosques': mosques})

def donations(request):
    return render(request, 'profileapp/donations.html')

def FavouriteView(request, pk):
    resto = get_object_or_404(Restaurants, id = request.POST.get('fav_id'))
    if resto.favourite.filter(username=request.user.username).exists():
        resto.favourite.remove(request.user)
    else:
        resto.favourite.add(request.user)
    return HttpResponseRedirect(reverse('restos_detail', args = [str(pk)]))

def post_favourite_list(request):
    user = request.user
    favourite_lists = user.favourite.all()
    context = {
        'favourite_lists' : favourite_lists
    }
    return render(request, "profileapp/favorites.html", context)

class SearchView(View):
    def post(self, request):
        try:
            if request.method == "POST" and len(request.POST.get("search_field")) > 0:
                searching_text = request.POST.get("search_field")
                return redirect("search_success", text=searching_text)
            else:
                return render(request, "profileapp/search.html",
                              {"empty_res": "There is no mosque"})
        except Exception as e:
            print(e)
            return render(request, "profileapp/search.html",
                          {"empty_res": f"No mosque have been found by {request.POST.get('search_field')}"})

class SearchSuccessView(View):
    def get(self, request, text):

        fields = [field for field in Mosque._meta.fields if isinstance(
            field, CharField) or isinstance(field, TextField)]

        queries = [Q(**{field.name + "__icontains": text}) for field in fields]
        qs = Q()
        for query in queries:
            qs = qs | query

        search_res = Mosque.objects.filter(qs)
        return render(request, "profileapp/search.html",
                      {"search_res": search_res, "empty_res": "There is no mosque"})

class SearchView2(View):
    def post(self, request):
        try:
            if request.method == "POST" and len(request.POST.get("search_field")) > 0:
                searching_text = request.POST.get("search_field")
                return redirect("search_success2", text=searching_text)
            else:
                return render(request, "profileapp/searchh.html",
                              {"empty_res": "There is no mosque"})
        except Exception as e:
            print(e)
            return render(request, "profileapp/searchh.html",
                          {"empty_res": f"No mosque have been found by {request.POST.get('search_field')}"})

class SearchSuccessView2(View):
    def get(self, request, text):

        fields = [field for field in Restaurants._meta.fields if isinstance(
            field, CharField) or isinstance(field, TextField)]

        queries = [Q(**{field.name + "__icontains": text}) for field in fields]
        qs = Q()
        for query in queries:
            qs = qs | query

        search_ress = Restaurants.objects.filter(qs)
        return render(request, "profileapp/searchh.html",
                      {"search_ress": search_ress, "empty_res": "There is no mosque"})

def submit_review(request, resto_id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, resto__resto_id =resto_id)
            print(reviews)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.resto_id = resto_id
                data.user_id = request.user.id
                data.save()
                return redirect(url)