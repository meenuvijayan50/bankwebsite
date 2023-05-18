
from django.contrib import admin

from .models import City, Country, Person,Account

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Account)
