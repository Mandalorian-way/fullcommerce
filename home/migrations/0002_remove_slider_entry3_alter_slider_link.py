# Generated by Django 5.0.6 on 2024-06-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='entry3',
        ),
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.CharField(default='#', max_length=255),
        ),
    ]
