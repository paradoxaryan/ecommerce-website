# Generated by Django 4.0.5 on 2022-07-31 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0020_alter_details_details_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_detail',
            name='detail_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itm_detail', to='appone.details', unique=True),
        ),
    ]
