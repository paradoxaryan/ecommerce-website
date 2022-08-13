# Generated by Django 4.0.5 on 2022-06-29 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sub_category_id',
        ),
        migrations.CreateModel(
            name='sub_cat_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='appone.item')),
                ('sub_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_of_subcat', to='appone.sub_category')),
            ],
        ),
    ]