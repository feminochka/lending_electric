from django.forms import ModelForm, TextInput, Textarea
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'l_name', 'email', 'tel', 'message']
        widgets = {
            'name': TextInput(attrs={

                'type': 'text',
                'name ': 'Name',
                'placeholder': 'Имя'
            }),
            'l_name': TextInput(attrs={

                'type': 'text',
                'name ': 'Last name',
                'placeholder': 'Фамилия'
            }),
            'email': TextInput(attrs={

                'type': 'email',
                'name ': 'Email',
                'placeholder': 'Email'
            }),
            'tel': TextInput(attrs={

                'type': 'text',
                'name ': 'phone',
                'placeholder': '+375(29) 5555 555'
            }),
            'message': Textarea(attrs={
                'name ': 'Message',
                'placeholder': 'Сообщение'
            })
        }
