# Generated by Django 2.0.4 on 2018-08-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180805_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='display_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/category_image'),
        ),
    ]