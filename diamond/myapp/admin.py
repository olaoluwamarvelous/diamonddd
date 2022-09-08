from django.contrib import admin
from .models import teamdetail, testimonyp, ContactModel, Post, Comment
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created']
    list_filter = ['created', 'email']
    list_display = ['name', 'subject', 'email', 'created', 'messagess']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'position']

    search_fields = ['name', 'position']
    list_filter = ['created']
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro']
    list_filter = ['date_added']
    list_display = ['title', 'intro', 'date_added']



# Register your models here.
admin.site.register(teamdetail, TeamAdmin)
admin.site.register(testimonyp)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)