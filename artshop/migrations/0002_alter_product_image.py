# Generated by Django 4.1.7 on 2023-05-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='artshop/images/default.png', upload_to='artshop/images'),
        ),
    ]
