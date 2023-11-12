from django.forms import ModelForm, CharField, EmailField, CheckboxSelectMultiple
from django.contrib.auth.models import User
from record.models import Customers


class CreateUserFrom(ModelForm):

    first_name = CharField(label="Имя",
                           max_length=150,
                           help_text='Введите ваше имя',
                           error_messages={
                               "max_length": "Не более 150 символов"
                           })
    last_name = CharField(label="Фамилия",
                          max_length=150,
                          help_text='Введите вашу фамилию',
                          )
    email = EmailField(label="Почта",
                       help_text='Введите действующую почту'
                       )

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]


class CreateCustomersForm(ModelForm):

    class Meta:
        model = Customers
        exclude = ["user"]
        labels = {
            "phone_number": "Номер телефона",
            "birth_date": "Дата рождения",
            "hobby": "Увлечения",
            "photo": "Фото",
         }

        widgets = {
            "hobby": CheckboxSelectMultiple
        }



