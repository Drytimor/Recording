from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from record.models import Customers


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Customers.objects.create(user=instance)
#     instance.customers.save()





