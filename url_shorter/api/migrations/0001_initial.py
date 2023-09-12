# Generated by Django 3.2.3 on 2023-09-12 16:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_link', models.CharField(blank=True, max_length=70, null=True, unique=True)),
                ('link_to_shorten', models.CharField(max_length=1024, unique=True, validators=[django.core.validators.RegexValidator(message='Link cannot contain such characters.', regex='https?:\\/\\/\\S+')])),
            ],
            options={
                'verbose_name': 'Набор из ссылки и ее укороченной версии',
                'verbose_name_plural': 'Наборы из ссылок и их укороченных версий',
            },
        ),
    ]