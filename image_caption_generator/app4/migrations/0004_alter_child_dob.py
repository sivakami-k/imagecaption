# Generated by Django 3.2.7 on 2024-03-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0003_alter_parent_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='dob',
            field=models.CharField(max_length=50),
        ),
    ]
