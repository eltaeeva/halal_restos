from django.contrib import admin
from .models import *

admin.site.register(Restaurants)
admin.site.register(Mosque)
admin.site.register(ReviewRating)
admin.site.register(Resto_tables)
admin.site.register(Book)
admin.site.register(NamazTime)
admin.site.unregister(User)