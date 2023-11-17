from django.db import transaction
from django.contrib.auth.models import User
from record.models import Customers


@transaction.atomic
def create_user(username, email, password, first_name, last_name,
                phone_number, birth_date, photo=None):
    user = User(username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                )
    user.full_clean()
    user.save()
    profile = Customers(user=user,
                        phone_number=phone_number,
                        birth_date=birth_date,
                        )
    profile.full_clean()
    profile.save()













