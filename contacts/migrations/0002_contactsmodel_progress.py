# Generated by Django 4.0.3 on 2022-05-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsmodel',
            name='progress',
            field=models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive')], default=('AC', 'Active'), max_length=2, verbose_name='Status'),
        ),
    ]