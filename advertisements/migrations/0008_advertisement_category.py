# Generated by Django 3.1.6 on 2021-03-09 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='advertisement', to='advertisements.category'),
        ),
    ]
