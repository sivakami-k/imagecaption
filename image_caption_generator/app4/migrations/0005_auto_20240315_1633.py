# Generated by Django 3.2.7 on 2024-03-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0004_alter_child_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awareness',
            name='awareness_videos',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='awareness',
            name='instructions',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]