# Generated by Django 4.1.5 on 2023-01-16 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0007_alter_fooditem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='quantity',
        ),
    ]