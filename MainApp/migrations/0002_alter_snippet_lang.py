# Generated by Django 4.2 on 2024-01-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('cpp', 'C++')], max_length=30),
        ),
    ]