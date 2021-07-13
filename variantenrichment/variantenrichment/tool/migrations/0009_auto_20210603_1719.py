# Generated by Django 3.0.13 on 2021-06-03 15:19

from django.db import migrations, models
import uuid
import variantenrichment.tool.models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0008_auto_20210528_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='inheritance',
            field=models.FileField(blank=True, upload_to=variantenrichment.tool.models.get_project_directory),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1cac8dd5-e51c-4a95-9f29-e2e516679b70'), editable=False, primary_key=True, serialize=False),
        ),
    ]