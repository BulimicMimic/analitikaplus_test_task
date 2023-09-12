from django.core.validators import RegexValidator
from django.db import models


class LinkShortener(models.Model):
    link_regex = RegexValidator(
        regex=r'https?:\/\/\S+',
        message='Link cannot contain such characters.',
    )
    short_link = models.CharField(
        max_length=70,
        unique=True,
        null=True,
        blank=True,
        db_index=True,
    )
    link_to_shorten = models.CharField(
        validators=[link_regex],
        max_length=1024,
        unique=True,
    )

    class Meta:
        verbose_name = 'Набор из ссылки и ее укороченной версии'
        verbose_name_plural = 'Наборы из ссылок и их укороченных версий'
