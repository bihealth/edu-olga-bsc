# Generated by Django 3.0.13 on 2021-07-15 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0023_auto_20210713_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('363d0694-fcac-4ca3-ab1f-a941cc8b97c6'), editable=False, primary_key=True, serialize=False),
        ),
    ]