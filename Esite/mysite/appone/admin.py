from django.contrib import admin

# Register your models here.

from .models import Item, Item_detail
from .models import Image
from .models import Category
from .models import Sub_category
from .models import Review
# from .models import sub_cat_item
from .models import Colors
from .models import Item_colors
from .models import Size_chart
from .models import Item_size
from .models import Banner_image
from .models import Cart
from .models import Address
from .models import Order
from .models import Order_status
from .models import Coupon_code
from .models import Coupon_used
from .models import Item_trend
from .models import Banner_image_mobile
from .models import Payment_method
from .models import Circular_banner
from .models import Trending_product
from .models import Hot_right_now
from .models import Hot_right_now_mobile
from .models import Deal_you_dont_miss
from .models import Offer_poster
from .models import Offer_poster_mobile
from .models import Type
from .models import Details
from .models import Item_detail

admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Colors)
admin.site.register(Item_colors)
admin.site.register(Size_chart)
admin.site.register(Item_size)
admin.site.register(Banner_image)
admin.site.register(Order)
admin.site.register(Coupon_code)
admin.site.register(Coupon_used)
admin.site.register(Item_trend)
admin.site.register(Banner_image_mobile)
admin.site.register(Order_status)
admin.site.register(Payment_method)
admin.site.register(Circular_banner)
admin.site.register(Trending_product)
admin.site.register(Hot_right_now)
admin.site.register(Hot_right_now_mobile)
admin.site.register(Deal_you_dont_miss)
admin.site.register(Offer_poster)
admin.site.register(Offer_poster_mobile)
admin.site.register(Type)
admin.site.register(Review)
admin.site.register(Item_detail)
admin.site.register(Details)
# admin.site.register(sub_cat_item)