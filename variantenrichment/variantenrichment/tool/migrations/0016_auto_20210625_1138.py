# Generated by Django 3.0.13 on 2021-06-25 09:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0015_auto_20210625_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1c71f231-2ab2-4432-891e-7c514bd952a3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
