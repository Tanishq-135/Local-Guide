from django.contrib import admin
from home.models import Contact, Food, Shopping, Service, User, UserProfile
# Register your models here.

admin.site.register(Contact)
admin.site.register(Food)
admin.site.register(Shopping)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(UserProfile)