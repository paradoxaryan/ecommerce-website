# Generated by Django 4.0.5 on 2022-07-14 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0012_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.item_trend'),
        ),
    ]
