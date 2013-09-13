from django.contrib import admin
from chat.models import message
from profiles.models import CustomUser

class chatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser)
admin.site.register(message)
