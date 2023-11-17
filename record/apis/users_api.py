from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from record.services.users_services import create_user


class CreateUserApi(APIView):

    class InputSerializer(serializers.Serializer):

        username = serializers.CharField(label="Логин",
                                         max_length=150,
                                         help_text="Обязательное поле. Не более 150 символов."
                                                   "Только буквы, цифры и символы @/./+/-/_.",
                                         error_messages={
                                             "max_length": "Не более 150 символов"
                                         })
        password = serializers.RegexField(label="Пароль",
                                          regex=r"(?=.*[\d])(?=.*[!@#$%^&*.])(?=.*[a-z])(?=.*[A-Z])"
                                                r"[0-9a-zA-Z!@#$%^&*.]{6,}",
                                          max_length=128,
                                          help_text="Обязательное поле. Не более 128 символов."
                                                    "Пароль должен содержать латинские заглавные и строчные буквы,"
                                                    "цифры, спецсимволы. Длина пароля не менее 6 символов",
                                          error_messages={
                                              "invalid": "Ненадежный пароль",
                                              "max_length": "Не более 128 символов"
                                          })
        password2 = serializers.CharField(label="Пароль",
                                          help_text="Повторите пароль",
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
                                          error_messages={
                                              "max_length": "Не более 150 символов"
                                          })
        email = serializers.EmailField(label="Почта",
                                       help_text='Введите действующую почту',
                                       error_messages={
                                           "invalid": "email invalid",
                                       })
        phone_number = serializers.RegexField(label="Номер телефона",
                                              regex=r"^((8|\+7)?)[\d]{10}$",
                                              help_text="Введите номер телефона из 11 цифр",
                                              error_messages={
                                                  "invalid": "Проверьте правильность номера",
                                              })
        birth_date = serializers.DateField(label="Дата рождения",
                                           )
        photo = serializers.ImageField(label="Фото",
                                       required=False
                                       )

        def validate(self, data: dict):
            if data['password'] != data['password2']:
                raise serializers.ValidationError({
                    "password2": "пароли не совпадают"
                })
            del data['password2']
            return data

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)








