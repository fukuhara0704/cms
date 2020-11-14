from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

def check_age(value):
    if value < 10 or value > 100:
        raise ValidationError('10〜100歳が範囲ですよ!')


class Member(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100,
                                validators=[MinLengthValidator(5, '5文字以上です！'),
                                            RegexValidator(r'^[a-zA-Z0-9]*$', '英数字のみです！')])
    age = models.IntegerField(
        default=0, validators=[check_age])

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title