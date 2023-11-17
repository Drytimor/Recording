from django.contrib.auth.forms import BaseUserCreationForm
from django.forms import ModelForm, EmailField
from record.models import Customers


class CreateUserForm(BaseUserCreationForm):

    email = EmailField(required=True)

    class Meta(BaseUserCreationForm.Meta):
        fields = ("username", "email")


class CreateProfileForm(ModelForm):
    class Meta:
        model = Customers
        exclude = ["user", "photo"]
