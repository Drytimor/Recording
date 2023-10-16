from django.db import models
from django.contrib.auth.models import User
from project_recording.validators import PhoneNumberValidator
from django.db.models import F, Q

# Create your models here.


class AbstractInfo(models.Model):
    """Передает общую информацию:
       номер телефона"""
    phone_number = models.CharField(max_length=20,
                                    unique=True,
                                    validators=[PhoneNumberValidator])

    class Meta:
        abstract = True


class Activity(models.TextChoices):
    SPORT = "SP", "спорт"
    TOURISM = "TR", "туризм"
    EDUCATION = "ED", "образование"
    SCIENCE = "SC", "наука"
    SUNDRY = "SN", "разное"


class Organization(AbstractInfo):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=50,
                                default=Activity.SUNDRY,
                                choices=Activity.choices)

    profile = models.JSONField(null=True,
                               blank=True)
    photo = models.ImageField(upload_to='photo_organization',
                              width_field=150,
                              height_field=150,
                              null=True,
                              blank=True)

    class Meta:
        db_table = 'organization'


class Customer(AbstractInfo):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    hobby = models.CharField(max_length=50,
                             default=Activity.SUNDRY,
                             choices=Activity.choices)
    photo = models.ImageField(upload_to='photo_customer',
                              width_field=150,
                              height_field=150,
                              null=True,
                              blank=True)

    class Meta:
        db_table = 'customer'


class Employee(AbstractInfo):

    organization = models.ForeignKey('organization',
                                     on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    profile = models.JSONField(null=True,
                               blank=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photo_employee',
                              width_field=150,
                              height_field=150,
                              null=True,
                              blank=True)

    class Meta:
        db_table = 'employee'


class Events(models.Model):

    PAID = "PAID"
    FREE = "FREE"
    PAYMENT_TARIFF_CHOICES = [
        (PAID, "платно"),
        (FREE, "бесплатно"),
    ]

    OPEN = "OPEN"
    CLOSED = "CLOSE"
    STATUS_OPENING_CHOICES = [
        (OPEN, "открыт"),
        (CLOSED, "закрыт"),
    ]

    organization = models.ForeignKey('organization',
                                     on_delete=models.CASCADE)
    events_employee = models.ManyToManyField('employee')
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_tariff = models.CharField(max_length=4,
                                     choices=PAYMENT_TARIFF_CHOICES)
    status_opening = models.CharField(max_length=10,
                                      choices=STATUS_OPENING_CHOICES,
                                      default=OPEN)
    limit_clients = models.PositiveSmallIntegerField()
    quantity_clients = models.PositiveSmallIntegerField(default=0)
    price_event = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'events'
        constraints = [
            models.CheckConstraint(check=Q(quantity_clients__lte=F("limit_clients")),
                                   name="check_quantity_clients"),
            models.CheckConstraint(check=Q(limit_clients__gt=0),
                                   name="check_limit_clients"),
        ]


class Recordings(models.Model):

    event = models.ForeignKey('events', on_delete=models.CASCADE)
    customer = models.ForeignKey('customer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'recordings'
        constraints = [
            models.UniqueConstraint(fields=['event', 'customer'],
                                    name='unique_recording_customer')
        ]


class HistoryRecordings(models.Model):

    PAID = "PAID"
    CANCELED = "CANC"
    STATUS_RECORDING_CHOICES = [
        (PAID, "оплачено"),
        (CANCELED, "отменено"),
    ]

    recording_id = models.PositiveBigIntegerField()
    event_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField()
    status_recording = models.CharField(max_length=4, choices=STATUS_RECORDING_CHOICES)
    date_recording = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'history_recording'



