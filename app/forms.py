from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"class" : "form-control", 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={"class" : "form-control", 'placeholder': 'Почта'}),
            'phone': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Номер телефона'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Сообщение', 'rows': 5}),
        }


# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=30, label='Имя',help_text='Введите данные имени',
#                            widget=forms.TextInput(
#                                attrs={"class" : "form-control", 'placeholder': 'Имя'}
#                            ))
#     email = forms.EmailField(label='Почта',help_text='Введите данные почты',
#                            widget=forms.EmailInput(
#                                attrs={"class" : "form-control", 'placeholder': 'Почта'}
#                            ))
#     phone = forms.CharField(max_length=13, label='Номер телефона',help_text='Введите номер телефона',
#                            widget=forms.TextInput(
#                                attrs={"class" : "form-control", 'placeholder': "Номер телефона"}
#                            ))
#     message = forms.CharField(label='Сообщение',help_text='Введите данные сообщение',
#                            widget=forms.Textarea(
#                                attrs={"class" : "form-control", 'placeholder': 'Сообщение',
#                                       'rows': 7}
#                            ))
