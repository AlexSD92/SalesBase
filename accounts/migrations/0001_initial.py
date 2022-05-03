# Generated by Django 4.0.3 on 2022-05-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.TextField(max_length=50, null=True)),
                ('account_ind', models.TextField(max_length=50, null=True)),
                ('account_size', models.PositiveIntegerField(null=True)),
                ('account_rev', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
