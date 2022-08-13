from django.db import models
from django.contrib.auth.models import User
from django.forms import NullBooleanField
# Create your models here.
# Admin side elements
class Category(models.Model):
    category = models.CharField(max_length=16)

    def __str__(self):
        return self.category


class Sub_category(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_cat')
    sub_category = models.CharField(max_length=16)
    sub_category_code = models.CharField(max_length=5)

    def __str__(self):
        return self.sub_category

class Type(models.Model):
    types = models.CharField(max_length=25)
    type_code = models.CharField(max_length=5)

    def __str__(self):
        return self.types

class Trending_product(models.Model):
    img = models.ImageField(upload_to="media")

class Hot_right_now(models.Model):
    img = models.ImageField(upload_to="media")

class Hot_right_now_mobile(models.Model):
    img = models.ImageField(upload_to="media")


class Deal_you_dont_miss(models.Model):
    img = models.ImageField(upload_to="media")

class Offer_poster(models.Model):
    img = models.ImageField(upload_to="media")

class Offer_poster_mobile(models.Model):
    img = models.ImageField(upload_to="media")

class Banner_image(models.Model):
    #device = models.ForeignKey(Banner_device, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media")

class Banner_image_mobile(models.Model):
    #device = models.ForeignKey(Banner_device, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media")

class Circular_banner(models.Model):
    img = models.ImageField(upload_to="media")
    name = models.CharField(max_length=16)

class Item(models.Model):

    item_unique_id = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
    item_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='item_of_type')
    sub_cat_id = models.ForeignKey(Sub_category, on_delete=models.CASCADE, related_name='item_of_subcat')
    original_price = models.IntegerField()
    offer_price = models.IntegerField()
    desc = models.TextField()
    available = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    # caption = models.CharField(max_length=100)
    # img = models.ImageField(upload_to="pics")
    # video = models.FileField(upload_to="video/%y")
    # desc = models.TextField()
    # price = models.IntegerField()
    # offer = models.BooleanField(default=False)

    def __str__(self):
        return self.item_unique_id

class Details(models.Model):
    details_name = models.CharField(max_length=100)
    details_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.details_name

class Item_detail(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='detail')
    detail_id = models.ForeignKey(Details, on_delete=models.CASCADE, related_name='itm_detail')
    details_info = models.CharField(max_length=100)



class Review(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='revw')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rev')
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.item_id.item_unique_id


class Image(models.Model):
    img = models.ImageField(upload_to="media")
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='img')
    # caption = models.CharField(max_length=100)
    # img = models.ImageField(upload_to="pics")
    # video = models.FileField(upload_to="video/%y")
    # desc = models.TextField()
    # price = models.IntegerField()
    # offer = models.BooleanField(default=False)

    def __str__(self):
        return self.item_id.item_unique_id

class Item_trend(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='trend')
    img_id = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='img_trend')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.item_id.item_unique_id



class Colors(models.Model):
    color_id = models.IntegerField()
    color = models.CharField(max_length=16)
    def __str__(self):
        return self.color

class Item_colors(models.Model):
    item_uid_first = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='sample1')
    item_uid_second = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='sample2')
    

    def __str__(self):
        return self.item_uid_first.item_unique_id

class Size_chart(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.size

class Item_size(models.Model):
    item_unique_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='avail_size')
    size_id = models.ForeignKey(Size_chart, on_delete=models.CASCADE)
    number_of_item = models.IntegerField()
    avail = models.BooleanField(default=False)

    def __str__(self):
        return self.item_unique_id.item_unique_id

# class Banner_device(models.Model):
#     device_name = models.CharField(max_length=8,unique = True)


# Coupon codes
class Coupon_code(models.Model):
    code = models.CharField(max_length=8,unique = True)
    code_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    code_desc = models.TextField()
    discount = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class Coupon_used(models.Model):
    code = models.ForeignKey(Coupon_code, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    used_date = models.DateTimeField(auto_now_add=True)
    
# Selling details

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)
    house_no = models.TextField()
    area = models.TextField()
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return self.pin_code
        
class Payment_method(models.Model):
    methods = models.CharField(max_length=30)

    def __str__(self):
        return self.methods

class Order(models.Model):
    item_uid = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='address')
    order_item_size = models.ForeignKey(Size_chart, on_delete=models.CASCADE, related_name='item_siz')
    created_on = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE, related_name='payment_order')


class Order_status(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_status')
    dispatched = models.BooleanField(default=False)
    dispatched_on = models.DateTimeField(null=True, blank=True)
    delivered = models.BooleanField(default=False)
    delivered_on = models.DateTimeField(null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    paid_on = models.DateTimeField(null=True, blank=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_trend_id = models.ForeignKey(Item_trend, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

