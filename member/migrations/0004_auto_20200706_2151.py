# Generated by Django 3.0.5 on 2020-07-06 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_ticket_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='user_id',
            new_name='username',
        ),
        migrations.AddField(
            model_name='ticket',
            name='reg_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
