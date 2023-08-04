from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import profile

# Unregister your models here.

admin.site.unregister(Group) 


# Register your models here.

admin.site.register(profile)




# Extend User model

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]



# Unregister User.

admin.site.unregister(User)

#Re-register User
admin.site.register(User, UserAdmin)


# Extend User model

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]


