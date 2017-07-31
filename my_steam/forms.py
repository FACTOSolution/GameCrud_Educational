from django import forms
from .models import Game, Profile
from django.core.exceptions import ValidationError

class AddGameForm(forms.ModelForm):
    def clean_cover_img(self):
        data = self.cleaned_data['cover_img']

        try:
            if data:
                file_type = data.content_type.split('/')[0]

                if len(data.name.split('.')) == 1:
                    raise ValidationError(_('File type is not supported'))

                if file_type in settings.TASK_UPLOAD_FILE_TYPES:
                    pass
                else:
                    raise ValidationError(_('File Type is not supported'))
        except:
            pass

        return data

    class Meta:
        model = Game
        fields = ['title','publisher','platform','cover_img','genre']

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 42
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('steam_id', 'steam_username')
