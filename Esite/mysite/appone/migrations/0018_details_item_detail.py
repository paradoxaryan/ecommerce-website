# Generated by Django 4.0.5 on 2022-07-26 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0017_alter_cart_item_trend_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_name', models.TextField()),
                ('details_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itm_detail', to='appone.details')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='appone.item')),
            ],
        ),
    ]
