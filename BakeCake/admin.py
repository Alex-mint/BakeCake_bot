from django.contrib import admin
from .forms import ProfileForm
from .models import Message
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','external_id', 'name')
    form = ProfileForm

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','profile','text','created_at')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)