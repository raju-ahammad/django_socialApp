# Generated by Django 2.1.4 on 2019-01-22 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
    ]
