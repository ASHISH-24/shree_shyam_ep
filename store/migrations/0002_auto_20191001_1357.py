# Generated by Django 2.2 on 2019-10-01 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_data',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
    ]
