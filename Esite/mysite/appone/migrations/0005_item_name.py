# Generated by Django 4.0.5 on 2022-07-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_remove_category_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
