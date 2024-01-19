# Generated by Django 4.2.9 on 2024-01-16 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vrexApp', '0006_schoolform_date_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolform',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requested_forms', to=settings.AUTH_USER_MODEL),
        ),
    ]
