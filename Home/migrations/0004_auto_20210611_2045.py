# Generated by Django 2.2.19 on 2021-06-11 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_account_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='balance', to=settings.AUTH_USER_MODEL),
        ),
    ]