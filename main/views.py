from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product, Category
from django.core.paginator import Paginator
from datetime import datetime
from dateutil.relativedelta import relativedelta
from cart.forms import CartAddProductForm


def order_time_page(request):
    all_time = ['01:00', '02:00', '03:00', '04:00', '05:00', '06:00', 
                '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
                '13:00', '14:00', '15:00', '16:00', '17:00', '18:00',
                '19:00', '20:00', '21:00', '22:00', '23:00', '24:00',
                ]
    today_day = datetime.today()
    min_day_value = today_day.strftime("%Y-%m-%d")
    max_day_value = (today_day + relativedelta(months=2)).strftime("%Y-%m-%d")
    
    dict_obj = {
        "min_day_value": min_day_value,
        'all_time': all_time,
        'max_day_value': max_day_value,
        }
    return render(request, 'main/order_time/order_time.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        day = request.POST['date']
        time = request.POST['time']
        element = Order(
            order_name=name,
            order_phone=phone,
            order_time = time,
            order_day = day)
        element.save()
        return render(request, 'main/order_time/thx.html', {'name': name,})
    else:
        return render(request, 'main/order_time/thx.html')
    

def popular_list(request):
    products = Product.objects.filter(available=True)[:3]
    return render (request,
                   'main/index/index.html',
                   {'products': products})
    
    
def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm
    return render(request, 
                  'main/product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})
    
    

def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 10)
    current_page = paginator.page(int(page))
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        paginator = Paginator(products.filter(category=category), 10)
        current_page = paginator.page(int(page))
        
    return render(request,
                  'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': current_page,
                   'slug_url': category_slug})