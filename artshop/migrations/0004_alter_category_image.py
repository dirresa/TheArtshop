# Generated by Django 4.1.7 on 2023-05-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artshop', '0003_remove_product_public_day_remove_product_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='artshop/categories/default.png', upload_to='artshop/categories'),
        ),
    ]
