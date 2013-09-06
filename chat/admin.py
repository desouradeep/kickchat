from django.contrib import admin
from chat.models import message
from profiles.models import user

class chatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(user)
admin.site.register(message)
