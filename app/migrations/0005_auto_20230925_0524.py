# Generated by Django 3.2.20 on 2023-09-25 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230925_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificaterequest',
            name='certificate_content',
        ),
        migrations.RemoveField(
            model_name='certificaterequest',
            name='certificate_file_name',
        ),
    ]