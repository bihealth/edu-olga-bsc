# Generated by Django 3.0.13 on 2021-03-09 17:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0003_auto_20210305_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundset',
            name='file',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='backgroundset',
            name='population',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7c291355-6576-4102-b104-06bf637c4319'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='BackgroundJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('new', 'New'), ('running', 'Running'), ('done', 'Finished')], default='new', max_length=7)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.Project')),
            ],
        ),
    ]
