# Generated by Django 2.2.19 on 2021-06-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_transaction_viewed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('task', models.TextField(max_length=300)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
