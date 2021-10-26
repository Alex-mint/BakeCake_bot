from django.contrib import admin
from .forms import ProfileForm, MessageForm
from .models import Message, Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id','external_id', 'name','first_name','last_name'

    )
    form = ProfileForm

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','profile','order_status','text','created_at')
    list_editable = ['order_status']

    form = MessageForm





admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
