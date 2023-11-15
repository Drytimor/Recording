from django.db import transaction
from django.contrib.auth.models import User
from record.models import Customers, Activitys


@transaction.atomic
def create_user(username, email, password, password2, first_name, last_name,
                phone_number, birth_date, hobby, photo=None):
    password2 = ...
    user = User(username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                )
    user.full_clean()
    profile_customer = create_profile_customer(user.pk, phone_number, birth_date, photo)
    profile_customer.full_clean()
    activitys_list = [hobby for hobby in Activitys.objects.filter(name__in=[*hobby])]
    user.save()
    profile_customer.save(customer=profile_customer.pk,
                          activitys_list=activitys_list)


def create_profile_customer(user, phone_number, birth_date, photo):
    return Customers(user=user,
                     phone_number=phone_number,
                     birth_date=birth_date,
                     photo=photo
                     )






