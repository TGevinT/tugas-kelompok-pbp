# Generated by Django 4.1 on 2022-10-28 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaksin', '0002_remove_vaksin_is_doctor_remove_vaksin_is_pasien_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]