# Generated by Django 3.1.4 on 2021-10-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]
