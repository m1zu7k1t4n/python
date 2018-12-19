from django.contrib import admin
from blog.models import User, Entry

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
admin.site.register(User, UserAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_display_links = ('id', 'title')
admin.site.register(Entry, EntryAdmin)
