from django.db import models
from django.contrib.auth.models import User, UserManager
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


class ActivitysChoices(models.TextChoices):
    SPORT = "sport", "спорт"
    TOURISM = "tourism", "туризм"
    EDUCATION = "education", "образование"
    SCIENCE = "science", "наука"
    ENTERTAINMENT = "entertainment", "развлечение"
    SUNDRY = "sundry", "разное"


class Activitys(models.Model):
    name = models.CharField(max_length=50,
                            default=ActivitysChoices.SUNDRY,
                            choices=ActivitysChoices.choices)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'activitys'
        constraints = [
            models.CheckConstraint(check=Q(name__in=ActivitysChoices.values),
                                   name=f"check_{db_table}")
        ]


class Organizations(AbstractInfo):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='organizations')
    name = models.CharField(max_length=255)

    activitys = models.ForeignKey('activitys',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='organizations')

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


class Customers(AbstractInfo):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='customers')
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='photo_customer',
                              width_field=150,
                              height_field=150,
                              null=True,
                              blank=True)

    class Meta:
        db_table = 'customers'


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
    PAID = "paid", "платный"
    FREE = "free", "бесплатный"


class StatusOpeningChoices(models.TextChoices):
    OPEN = "open", "открытый"
    CLOSED = "close", "закрытый"


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
    PAID = "paid", "оплачено"
    CANCELED = "canc", "отменено"


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



