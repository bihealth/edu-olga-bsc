# Generated by Django 3.0.13 on 2021-03-05 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6feb996a-08f9-44be-92b7-5d0d1158a9d9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
