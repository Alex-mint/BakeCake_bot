from django import forms
from .models import Profile, Message

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'external_id',
            'name',
            'first_name',
            'last_name',

        )
        widgets = {
            'name':forms.TextInput,
            'external_id':forms.TextInput,
            'first_name':forms.TextInput,
            'last_name':forms.TextInput,

        }
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'id',
            'text',
            'number_levels',
            'form',
            'topping',
            'berries',
            'decor',
            'title',

        )
        widgets = {
            'id':forms.TextInput,
            'text':forms.TextInput,
            'number_levels':forms.TextInput,
            'form':forms.TextInput,
            'topping':forms.TextInput,
            'berries':forms.TextInput,
            'decor':forms.TextInput,
            'title':forms.TextInput,

        }