# Generated by Django 2.0.4 on 2018-08-05 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180805_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='display_image',
            new_name='image',
        ),
    ]