# Generated by Django 4.0.3 on 2022-06-12 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50, null=True, verbose_name='Contact Name')),
                ('contact_role', models.CharField(max_length=50, null=True, verbose_name='Contact Role')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('progress', models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive')], default=('AC', 'Active'), max_length=2, verbose_name='Status')),
                ('slug', models.SlugField(default='', editable=False, max_length=255)),
                ('contact_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.accountsmodel', verbose_name='Contact Company')),
                ('contact_opp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opportunities.opportunitiesmodel', verbose_name='Contact Opportunity')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
    ]