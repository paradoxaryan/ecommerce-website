from django.shortcuts import render,redirect
from appone.models import Address, Banner_image,Colors, Details, Image, Item_colors,Details, Item_size,Order,Coupon_code,Item, Order_status, Size_chart,Sub_category,Banner_image_mobile,Circular_banner,Trending_product,Hot_right_now,Deal_you_dont_miss,Hot_right_now_mobile,Offer_poster,Offer_poster_mobile,Item_trend, Type, Review, Cart,Item_detail
from django.contrib.auth.models import User,Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

import os
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import smtplib
import ssl
from email.message import EmailMessage


# Create your views here.



def index(request):
    print("landing")
    email_sender = 'covid19slotnotifier@gmail.com'
    email_password = 'xglatzznnkcwxbub'
    # email_receiver = 'write-email-receiver-here'
# xglatzznnkcwxbub
     

    item1 = Banner_image.objects.all()
    item2 = Banner_image_mobile.objects.all()
    item3 = Circular_banner.objects.all()
    item4 = Trending_product.objects.all()
    item5 = Hot_right_now.objects.first()
    item6 = Deal_you_dont_miss.objects.all()
    item7 = Hot_right_now_mobile.objects.first()
    item8 = Offer_poster.objects.first()
    item9 = Offer_poster_mobile.objects.first()
    item10 = Item_trend.objects.order_by('-count')[:5]
    item11 = "Guest"
    usr=request.user.username
    if usr:
        item11=usr

    if request.method == 'POST':
        passwd = request.POST.get("password")
        email_receiver = request.POST.get("mail")
        usernm = request.POST.get("usernm")
        print("username")
        print(usernm)
        if passwd:
            print(usernm)
            print(passwd)
            user = authenticate(username=usernm , password=passwd)
            print(user)
            login(request,user)
            print(request.user.username)
            print("login successful")

        else:
            usr=User.objects.filter(username=email_receiver).first()
            if not usr:
                obj=User()
                obj.username=email_receiver
                obj.password="Bharti#12"
                obj.save()

            print(email_receiver)
            subject = 'Blugi Otp'
            body = "password is Bharti#12"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            print("email sent")

        print("exit")

    
    return render(request,"index.html",{'item1':item1,'item2':item2,'item3':item3,'item4':item4,'item5':item5,'item6':item6,'item7':item7,'item8':item8,'item9':item9,'item10':item10,'item11':item11})
@login_required
def log_out(request):
    logout(request)
    return redirect("/")

def product(request):
    item = Item_trend.objects.order_by('-count')
    return render(request,"product.html",{'item':item})

def product_def(request,id,nam):
    print(id)
    item1=Image.objects.filter(item_id=id).all()
    item2 = Item_trend.objects.order_by('-count')[:5]
    item3=Item_colors.objects.filter(item_uid_first=id).all()
    item4=[]
    for i in item3:
        print(i.item_uid_second.id)
        item4.append(Item_trend.objects.filter(item_id=i.item_uid_second.id).first())


    item5 = Review.objects.filter(item_id=id).all()
    item6 = Item_trend.objects.filter(item_id=id).first()
    var=item6.count
    item6.count=var+1
    item6.save()
    print(item6.id)
    item7 = Item_detail.objects.filter(item_id=id).all()

    return render(request,"product_detail.html",{'item1':item1,'item2':item2,'item4':item4,'item5':item5,'item6':item6,'item7':item7})

def cart(request):
    usr=request.user
    print(usr.username)
    item1=Cart.objects.filter(user=usr).all()
    print(item1)
    off=0
    sm1=0
    sm2=0
    total=0
    for i in item1:
        total=total+1
        sm1=sm1 + i.item_trend_id.item_id.original_price
        sm2=sm2 + i.item_trend_id.item_id.offer_price
    if request.method == 'POST':
        cod=request.POST.get('code')
        print("test1")
        print(cod)
        cop_code = Coupon_code.objects.filter(code=cod).first()
        print("test2")
        off_percent = cop_code.discount
        print(cop_code)
        x=off_percent/100
        y=x*sm2
        off=int(y)
        print(off)

    return render(request,"cstmr/cartsection.html",{'item1':item1,'item2':sm2,'item3':sm2-off,'item4':off,'item5':total})

def addcart(request,id):
    usr=request.user
    print("test")

    print(id)
    if Cart.objects.filter(item_trend_id=id,user=usr).first():
        response = redirect('/cart')
        return response
    else:
        obj = Cart()
        obj.user = usr
        print(usr)
        print(Item_trend.objects.filter(id=id).first())
        obj.item_trend_id = Item_trend.objects.filter(id=id).first()
        obj.save()
        response = redirect('/cart')
        return response

def delcartitem(request,id):
    obj=Cart.objects.get(id=id)
    obj.delete()
    response = redirect('/cart')
    return response

def chooseaddress(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        name=request.POST.get('name')
        mobno=request.POST.get('mobno')
        code=request.POST.get('code')
        hosno=request.POST.get('hosno')
        add=request.POST.get('add')
        obj=Address()
        obj.user=User.objects.filter(username=name).first()
        obj.name=name
        obj.pin_code=code
        obj.house_no=hosno
        obj.area=add
        obj.contact=mobno
        obj.save()

    addres = Address.objects.filter(user=user).all()
    print(addres)
    item1=Cart.objects.filter(user=user).all()
    print(item1)
    sm1=0
    sm2=0
    total=0
    for i in item1:
        total=total+1
        sm1=sm1 + i.item_trend_id.item_id.original_price
        sm2=sm2 + i.item_trend_id.item_id.offer_price
    return render(request,"cstmr/Address.html",{'item6':addres,'item1':item1,'item2':sm1,'item3':sm2,'item4':sm1-sm2,'item5':total})


@login_required
def mob_view_banner(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Banner_image_mobile.objects.filter(id=id).first()
        pstrimg = request.POST.get('pstrimg')
        obj.img = pstrimg
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def add_data(request):
    Sub_cat=Sub_category.objects.all()
    item2 = Type.objects.values('types').distinct()
    user=request.user.username
    if request.method == 'POST':
        SubCat=request.POST.get('SubCat')
        subcat_var = Sub_category.objects.filter(sub_category=SubCat).first()
        tp=request.POST.get('Type')
        type_var = Type.objects.filter(types=tp).first()
        ele_var=subcat_var.sub_category_code + type_var.type_code
        Name=request.POST.get('Name')
        ori_var=request.POST.get('oriprice')
        off_var=request.POST.get('offprice')
        desc_var=request.POST.get('desc')
        avail_var=request.POST.get('avail')
        xs_var=request.POST.get('xtrasmall')
        s_var=request.POST.get('small')
        m_var=request.POST.get('medium')
        l_var=request.POST.get('large')
        xl_var=request.POST.get('xtralarge')
        txl_var=request.POST.get('twoxl')
        thxl_var=request.POST.get('threexl')
        frxl_var=request.POST.get('frxl')
        imgs_var = request.FILES.getlist('imgs')
        var=Item.objects.filter(item_unique_id__startswith=ele_var).first()
        print(var)

        if(var is None):
            obj=Item()
            obj.item_unique_id = ele_var+"00001"
            obj.name = Name
            obj.item_type = type_var
            obj.sub_cat_id = subcat_var
            obj.original_price = ori_var
            obj.offer_price = off_var
            obj.desc = desc_var
            if avail_var == "on":
                obj.available = True
            else:
                obj.available = False
            obj.save()

        else:
            obj=Item()
            obj1 = Item.objects.filter(item_unique_id__startswith=ele_var).last()
            uid = obj1.item_unique_id
            nm=int(uid[6:])
            nm=nm+1
            obj.item_unique_id = ele_var+str(nm).zfill(5)
            obj.name = Name
            obj.item_type = type_var
            obj.sub_cat_id = subcat_var
            obj.original_price = ori_var
            obj.offer_price = off_var
            obj.desc = desc_var
            if avail_var == "on":
                obj.available = True
            else:
                obj.available = False
            obj.save()

        itm_obj = Item.objects.filter(item_unique_id__startswith=ele_var).last()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="XS").first()
        obj2.number_of_item = int(xs_var)
        if int(xs_var)!=0:
            obj2.avail = True
            
        obj2.save()
            
        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="S").first()
        obj2.number_of_item = int(s_var)
        if int(s_var)!=0:
            obj2.avail = True

        obj2.save()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="M").first()
        obj2.number_of_item = int(m_var)
        if int(m_var)!=0:
            obj2.avail = True

        obj2.save()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="L").first()
        obj2.number_of_item = int(l_var)
        if int(l_var)!=0:
            obj2.avail = True

        obj2.save()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="XL").first()
        obj2.number_of_item = int(xl_var)
        if int(xl_var)!=0:
            obj2.avail = True

        obj2.save()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="2XL").first()
        obj2.number_of_item = int(txl_var)
        if int(txl_var)!=0:
            obj2.avail = True

        obj2.save()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="3XL").first()
        obj2.number_of_item = int(thxl_var)
        if int(thxl_var)!=0:
            obj2.avail = True

        obj2.save()

        obj2 = Item_size()
        obj2.item_unique_id = itm_obj
        obj2.size_id = Size_chart.objects.filter(size="4XL").first()
        obj2.number_of_item = int(frxl_var)
        if int(frxl_var)!=0:
            obj2.avail = True
            
        obj2.save()

        for i in imgs_var:
            obj3=Image()
            obj3.item_id = itm_obj
            print(i)
            obj3.img = i
            obj3.save()

        obj4=Item_trend()
        obj4.item_id = obj
        obj4.img_id = Image.objects.filter(item_id=obj).first()
        obj4.count = 0
        obj4.save()


        response = redirect('/add_data')
        return response

    return render(request,"staff/adddata.html",{'sub_cat':Sub_cat,'item2':item2})

@login_required
def add_detail(request,id):
    item1=Item.objects.filter(id=id).first()
    item2=Details.objects.all()
    item3=Item_detail.objects.filter(item_id=item1).all()
    print(item2)
    if request.method=="POST":
        detail=request.POST.get('detail')
        info=request.POST.get('info')
        obj=Item_detail()
        obj.item_id=item1
        obj.detail_id=Details.objects.filter(id=detail).first()
        obj.details_info=info
        obj.save()

    return render(request,"staff/add_item_detail.html",{"item1":item1,"item2":item2,"item3":item3})


@login_required
def del_detail(request,id,id2):
    obj=Item_detail.objects.get(id=id)
    obj.delete()
    response = redirect('add_data_detail',id=id2)
    return response


@login_required
def payment(request):
    return render(request,"cstmr/payment.html")

@login_required
def add_poster(request):
    item1 = Banner_image.objects.all()
    item2 = Banner_image_mobile.objects.all()
    item3 = Circular_banner.objects.all()#
    item4 = Trending_product.objects.all()#
    item5 = Hot_right_now.objects.first()
    item6 = Deal_you_dont_miss.objects.all()#
    item7 = Hot_right_now_mobile.objects.first()
    item8 = Offer_poster.objects.first()
    item9 = Offer_poster_mobile.objects.first()
    return render(request,"staff/add_poster.html",{'mposter1':item1,'mposter2':item2,'mposter2':item2,'mposter3':item3,'mposter4':item4,'mposter5':item5,'mposter6':item6,'mposter7':item7,'mposter8':item8,'mposter9':item9})

@login_required
def replace_banner(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Banner_image.objects.get(id=id)
        #pstrimg = request.POST.get('bannerimg1')
        os.remove(obj.img.path)
        obj.img = request.FILES.get('bannerone')
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def replace_mbanner(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Banner_image_mobile.objects.get(id=id)
        #pstrimg = request.POST.get('bannerimg1')
        os.remove(obj.img.path)
        obj.img = request.FILES.get('bannermob')
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def add_circular_banner(request):
    if request.method == 'POST':
        print("done1")
        #pstrimg = request.POST.get('bannerimg1')
        img=request.FILES.get('circularbanner')
        name=request.POST.get('itemname')
        obj=Circular_banner()
        obj.img=img
        obj.name=name
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def del_circular_banner(request,id):
    obj=Circular_banner.objects.get(id=id)
    os.remove(obj.img.path)
    obj.delete()
    response = redirect('/addposter')
    return response

@login_required
def add_trending_product(request):
    if request.method == 'POST':
        print("done1")
        #pstrimg = request.POST.get('bannerimg1')
        img=request.FILES.get('trendingp')
        obj=Trending_product()
        obj.img=img
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def del_trending_product(request,id):
    obj=Trending_product.objects.get(id=id)
    os.remove(obj.img.path)
    obj.delete()
    response = redirect('/addposter')
    return response

@login_required
def replace_hot(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Hot_right_now.objects.get(id=id)
        #pstrimg = request.POST.get('bannerimg1')
        os.remove(obj.img.path)
        obj.img = request.FILES.get('hotrn')
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def replace_mhot(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Hot_right_now_mobile.objects.get(id=id)
        #pstrimg = request.POST.get('bannerimg1')
        os.remove(obj.img.path)
        obj.img = request.FILES.get('mhotrn')
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def add_deal_dont_wanna_miss(request):
    if request.method == 'POST':
        print("done1")
        #pstrimg = request.POST.get('bannerimg1')
        img=request.FILES.get('dealp')
        obj=Deal_you_dont_miss()
        obj.img=img
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def del_deal_dont_wanna_miss(request,id):
    obj=Deal_you_dont_miss.objects.get(id=id)
    os.remove(obj.img.path)
    obj.delete()
    response = redirect('/addposter')
    return response

@login_required
def offer_poster(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Offer_poster.objects.get(id=id)
        #pstrimg = request.POST.get('bannerimg1')
        os.remove(obj.img.path)
        obj.img = request.FILES.get('offpos')
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def offer_mposter(request,id):
    if request.method == 'POST':
        print("done1")
        obj = Offer_poster_mobile.objects.get(id=id)
        #pstrimg = request.POST.get('bannerimg1')
        os.remove(obj.img.path)
        obj.img = request.FILES.get('offmpos')
        obj.save()
        print("done2")
    response = redirect('/addposter')
    return response

@login_required
def dashboard(request):
    item6 = Banner_image_mobile.objects.first()
    return render(request,"staff/index.html",{'item6':item6})

@login_required
def order_detail(request):
    item1 = Order_status.objects.filter(dispatched=False).all()
    #print(item1)
    # for i in item1:
    #     x=i
    #     print(i)
    #     print(i.order_id.user)
        #print(Order_status.objects.filter(order_id=i).first())
    return render(request,"staff/active_order.html",{'item': item1})

@login_required
def dispatch(request,id):
    obj = Order.objects.filter(id=id).first()
    obj_status = obj.order_status
    obj_status.dispatched = True
    obj_status.dispatched_on = datetime.datetime.now()  
    obj_status.save()

    #add = Address.objects.filter(id=obj.address.id).first()
    response = redirect('/order_detail')
    return response


@login_required
def order_detail_dispatched(request):
    dispatched_item = Order_status.objects.filter(dispatched=True,delivered=False).all()
    #print(item1)
    # for i in item1:
    #     x=i
    #     print(i)
    #     print(i.order_id.user)
        #print(Order_status.objects.filter(order_id=i).first())
    return render(request,"staff/dispatched_order.html",{'item': dispatched_item})

@login_required
def deliver(request,id):
    obj = Order.objects.filter(id=id).first()
    print(obj)
    obj_sts = obj.order_status
    obj_sts.delivered = True
    obj_sts.delivered_on = datetime.datetime.now()
    obj_sts.save()

    #add = Address.objects.filter(id=obj.address.id).first()
    response = redirect('/dispatched')
    return response

@login_required
def order_detail_delivered(request):
    
    item1 = Order_status.objects.filter(delivered=True).all()

    return render(request,"staff/delivered_order.html",{'item': item1})

@login_required
def update_item(request):
    if request.method == 'POST':
        itemtid=request.POST.get('itemtid')
        oriprice=request.POST.get('orip')
        print(oriprice)
        offp=request.POST.get('offp')
        print(offp)
        trend_no=request.POST.get('trend')
        print(trend_no)
        obj = Item_trend.objects.filter(id=itemtid).first()
        if trend_no:
            obj.count=trend_no
            obj.save()
        if oriprice:
            obj2 = obj.item_id
            obj2.original_price = oriprice
            obj2.save()
        if offp:
            obj3 = obj.item_id
            obj3.offer_price = offp
            obj3.save()
    item1=Item_trend.objects.order_by('-count').all()

    return render(request,"staff/update_item.html",{'item1':item1}) 



@login_required
def print_address(request,id):
    obj = Order.objects.filter(id=id).first()
    print(obj.address)
    add = Address.objects.filter(id=obj.address.id).first()
    
    # filename = obj.model_attribute_name.path
    # response = FileResponse(open(filename, 'rb'))
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")
    p.drawString(20,800,'Name: ')
    p.drawString(90,800,add.name)
    p.drawString(20,780,'Pincode: ')
    p.drawString(90,780,add.pin_code)
    p.drawString(20,760,'House no: ')
    p.drawString(90,760,add.house_no)
    p.drawString(20,740,'Area: ')
    p.drawString(90,740,add.area)
    p.drawString(20,720,'Contact: ')
    p.drawString(90,720,add.contact)
    p.line(10,700,550,700) 

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    filename=add.pin_code+".pdf"
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=filename)

    

@login_required
def coupon_code(request):
    item1 = Coupon_code.objects.all()
    if request.method == 'POST':
        cod=request.POST.get('code')
        cod_desc=request.POST.get('code_desc')
        disc=request.POST.get('disc')
        id=request.POST.get('id')
        if cod:
            cop=Coupon_code.objects.filter(id=id).first()
            cop.code=cod
            cop.save()

        if cod_desc:
            cop=Coupon_code.objects.filter(id=id).first()
            cop.code_desc=cod_desc
            cop.save()

        if disc:
            cop=Coupon_code.objects.filter(id=id).first()
            cop.discount=disc
            cop.save()

    for i in item1:
        print(i)
    return render(request,"staff/coupon_code.html",{'item1': item1})



def stafflogin(request):
    print("enter")
    if request.method == 'POST':
        print("done1")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        print("done")
        print(user)
   
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect("/dashboard")
        else:
            return render(request, "staff/signin.html")
    print("enter2")
    return render(request, "staff/signin.html")

@login_required
def stafflogout(request):
    logout(request)
    return redirect("/stafflogin")

