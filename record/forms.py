from django.forms import ModelForm, CharField, EmailField
from django.contrib.auth.models import User
from record.models import Customers


class CreateUserFrom(ModelForm):

    first_name = CharField(max_length=150,
                           help_text='Введите ваше имя',
                           error_messages={
                               "max_length": "Не более 150 символов"
                           })
    last_name = CharField(max_length=150,
                          help_text='Введите вашу фамилию')
    email = EmailField(help_text='введите действующую почту')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class CreateCustomersForm(ModelForm):

    class Meta:
        model = Customers
        exclude = ["user"]



