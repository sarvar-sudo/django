from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import movie, ViewUser, site_about, live_chanel

# Register your models here.
admin.site.register(movie)
admin.site.register(ViewUser)
admin.site.register(site_about)
admin.site.register(live_chanel)


