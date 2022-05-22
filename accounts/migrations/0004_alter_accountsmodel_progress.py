# Generated by Django 4.0.3 on 2022-05-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accountsmodel_account_ind_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsmodel',
            name='progress',
            field=models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive')], default=('AC', 'Active'), max_length=2, verbose_name='Status'),
        ),
    ]