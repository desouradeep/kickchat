from django.contrib import admin
from chat.models import user, message

class chatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(user)
admin.site.register(message)
