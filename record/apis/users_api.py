from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from project_recording.validators import PhoneNumberValidator
from record.models import ActivitysChoices
from record.services.users_services import create_user


class CreateUserApi(APIView):

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(label="Логин",
                                         max_length=150,
                                         help_text="Required. 150 characters or fewer. "
                                                   "Letters, digits and @/./+/-/_ only.",
                                         validators=[UnicodeUsernameValidator()],
                                         error_messages={
                                             "unique": "A user with that username already exists.",
                                         })
        password = serializers.CharField(label="Пароль",
                                         max_length=128,
                                         help_text="Required. 150 characters or fewer. "
                                                   "Letters, digits and @/./+/-/_ only."
                                         )
        password2 = serializers.CharField(label="Пароль",
                                          max_length=128,
                                          help_text="Повторите пароль"
                                          )
        first_name = serializers.CharField(label="Имя",
                                           max_length=150,
                                           help_text='Введите ваше имя',
                                           error_messages={
                                               "max_length": "Не более 150 символов"
                                           })
        last_name = serializers.CharField(label="Фамилия",
                                          max_length=150,
                                          help_text='Введите вашу фамилию',
                                          )
        email = serializers.EmailField(label="Почта",
                                       help_text='Введите действующую почту'
                                       )
        phone_number = serializers.CharField(label="Номер телефона",
                                             max_length=20,
                                             validators=[PhoneNumberValidator()]
                                             )
        birth_date = serializers.DateField(label="Дата рождения",
                                           )
        photo = serializers.ImageField(label="Фото",
                                       required=False
                                       )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)








