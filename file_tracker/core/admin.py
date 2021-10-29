from django.contrib import admin

from .models import user_entry

class user_entry_Admin(admin.ModelAdmin):
    pass

admin.site.register(user_entry, user_entry_Admin)