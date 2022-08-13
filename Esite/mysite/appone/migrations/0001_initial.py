# Generated by Django 4.0.5 on 2022-06-29 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pin_code', models.CharField(max_length=6)),
                ('house_no', models.TextField()),
                ('area', models.TextField()),
                ('contact', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Banner_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Banner_image_mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('category', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Circular_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_id', models.IntegerField()),
                ('color', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True)),
                ('code_desc', models.TextField()),
                ('discount', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.BooleanField(default=True)),
                ('code_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deal_you_dont_miss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Hot_right_now',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Hot_right_now_mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_unique_id', models.CharField(max_length=16)),
                ('original_price', models.IntegerField()),
                ('offer_price', models.IntegerField()),
                ('desc', models.TextField()),
                ('available', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer_poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Offer_poster_mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='address', to='appone.address')),
                ('item_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='appone.item')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methods', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Size_chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Trending_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=16)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='appone.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatched', models.BooleanField(default=False)),
                ('dispatched_on', models.DateTimeField(blank=True, null=True)),
                ('delivered', models.BooleanField(default=False)),
                ('delivered_on', models.DateTimeField(blank=True, null=True)),
                ('payment_status', models.BooleanField(default=False)),
                ('paid_on', models.DateTimeField(blank=True, null=True)),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_status', to='appone.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_item_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_siz', to='appone.size_chart'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_order', to='appone.payment_method'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Item_trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('img_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img_trend', to='appone.image')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trend', to='appone.item')),
            ],
        ),
        migrations.CreateModel(
            name='Item_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_item', models.IntegerField()),
                ('avail', models.BooleanField(default=False)),
                ('item_unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avail_size', to='appone.item')),
                ('size_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.size_chart')),
            ],
        ),
        migrations.CreateModel(
            name='Item_colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_uid_first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sample1', to='appone.item')),
                ('item_uid_second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sample2', to='appone.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_of_type', to='appone.type'),
        ),
        migrations.AddField(
            model_name='item',
            name='sub_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_of_subcat', to='appone.sub_category'),
        ),
        migrations.AddField(
            model_name='image',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='appone.item'),
        ),
        migrations.CreateModel(
            name='Coupon_used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_date', models.DateTimeField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.coupon_code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]