from django.db import models
from django.contrib.auth.models import User
from project_recording.validators import PhoneNumberValidator
from django.db.models import F, Q

# Create your models here.


class AbstractInfo(models.Model):
    """Передает общую информацию:
       номер телефона"""
    phone_number_validator = PhoneNumberValidator()

    phone_number = models.CharField(max_length=20,
                                    unique=True,
                                    validators=[phone_number_validator])

    class Meta:
        abstract = True


class Activity(models.TextChoices):
    SPORT = "SP", "спорт"
    TOURISM = "TR", "туризм"
    EDUCATION = "ED", "образование"
    SCIENCE = "SC", "наука"
    ENTERTAINMENT = "ET", "развлечения"
    SUNDRY = "SN", "разное"


class Organizations(AbstractInfo):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='organizations')
    name = models.CharField(max_length=255)

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

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'organizations'
        constraints = [
            models.CheckConstraint(check=Q(activity__in=Activity.values),
                                   name=f"check_activity_{db_table}")
        ]


class Customers(AbstractInfo):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='customers')
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
        db_table = 'customers'
        constraints = [
            models.CheckConstraint(check=Q(hobby__in=Activity.values),
                                   name=f"check_hobby_{db_table}")
        ]


class Employees(AbstractInfo):

    organization = models.ForeignKey('organizations',
                                     on_delete=models.CASCADE,
                                     related_name='employees')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    profile = models.JSONField(null=True,
                               blank=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photo_employee',
                              width_field=150,
                              height_field=150,
                              null=True,
                              blank=True)

    def __str__(self):
        return f"{self.firstname}"

    class Meta:
        db_table = 'employees'


class PaymentTariffChoices(models.TextChoices):
    PAID = "PAID", "платно"
    FREE = "FREE", "бесплатно"


class StatusOpeningChoices(models.TextChoices):
    OPEN = "OPEN", "открыт"
    CLOSED = "CLOSE", "закрыт"


class Events(models.Model):

    organization = models.ForeignKey('organizations',
                                     on_delete=models.CASCADE,
                                     related_name='events')
    employee = models.ManyToManyField('employees',
                                      related_name='events')
    name = models.CharField(max_length=255)
    date_event = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status_tariff = models.CharField(max_length=4,
                                     choices=PaymentTariffChoices.choices)
    status_opening = models.CharField(max_length=10,
                                      choices=StatusOpeningChoices.choices,
                                      default=StatusOpeningChoices.OPEN)
    limit_clients = models.SmallIntegerField()
    quantity_clients = models.SmallIntegerField(default=0)
    price_event = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    description = models.TextField(null=True, blank=True)

    # def is_upperclass(self):
    #     return self.status_tariff in {
    #         self.PaymentTariffChoices.choices
    #     }

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'events'
        constraints = [
            models.CheckConstraint(check=Q(quantity_clients__lte=F("limit_clients")),
                                   name=f"check_quantity_clients_{db_table}"),
            models.CheckConstraint(check=Q(limit_clients__gt=0),
                                   name=f"check_limit_clients_{db_table}"),
            models.CheckConstraint(check=Q(status_tariff__in=PaymentTariffChoices.values),
                                   name=f"check_status_tariff_{db_table}"),
            models.CheckConstraint(check=Q(status_opening__in=StatusOpeningChoices.values),
                                   name=f"check_status_opening_{db_table}"),
            models.CheckConstraint(check=Q(start_time__lt=F("end_time")),
                                   name=f"check_time_{db_table}"),
        ]


class Recordings(models.Model):

    event = models.ForeignKey('events',
                              on_delete=models.CASCADE,
                              related_name='recordings')
    customer = models.ForeignKey('customers',
                                 on_delete=models.CASCADE,
                                 related_name='recordings')

    class Meta:
        db_table = 'recordings'
        constraints = [
            models.UniqueConstraint(fields=['event', 'customer'],
                                    name=f"unique_{db_table}_customer")
        ]


class StatusRecordingChoices(models.TextChoices):
    PAID = "PAID", "оплачено"
    CANCELED = "CANC", "отменено"


class HistoryRecordings(models.Model):

    recording_id = models.PositiveBigIntegerField()
    event_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField()
    status_recording = models.CharField(max_length=4,
                                        choices=StatusRecordingChoices.choices)
    date_recording = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'history_recordings'
        constraints = [
            models.CheckConstraint(check=Q(status_recording__in=StatusRecordingChoices.values),
                                   name="check_status_recording")
            ]



