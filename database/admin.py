from django.contrib import admin
from .models import *

admin.site.register(Restaurants)
admin.site.register(Mosque)
admin.site.register(ReviewRating)
admin.site.unregister(User)