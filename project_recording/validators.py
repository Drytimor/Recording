from django.core.validators import RegexValidator


class PhoneNumberValidator(RegexValidator):
    """Проверяет номер телефона на соответствие"""
    regex = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"



