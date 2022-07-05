from django.contrib import admin
from myapp.models import Ngo, Boutique
from myapp.models import Restaurant


admin.site.register(Ngo)
admin.site.register(Restaurant)
admin.site.register(Boutique)
# admin.site.register(Contact)