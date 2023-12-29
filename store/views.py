from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    banner = Banner.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.all()
    e_product = Product.objects.filter(category__name = 'Electornics')

    context = {
        'banner':banner,
        'category':category,
        'brand':brand,
        'product':product,
        'e_product':e_product,
    }
    return render(request, 'store/index.html',context)

def product_details(request,slug):
    product = Product.objects.get(slug=slug)
    releted_product = Product.objects.filter(Q(category__name = product.category.name) | Q(brand__name = product.brand.name)).exclude(slug=slug)

    context = {
        'product':product,
        'releted_product':releted_product,
    }
    return render(request,'store/product_details.html', context)


def product_search(request):
    query = request.GET['q']
    product = Product.objects.filter(Q(product_name__icontains=query)| Q(category__name__icontains=query))
    context ={
        'product':product
    }
    return render(request,'store/product_search.html',context)


@login_required(login_url='login')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item, created = Cart_Product.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check the order item is in the order
        if order.cart_product.filter(product__slug=product.slug).exists():
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, 'This product quantity updated')
            return redirect('product_details', slug=slug)
        
        else:
            order.cart_product.add(cart_item)
            messages.info(request, 'This Product was add to cart')
            return redirect('product_details', slug=slug)
    else:
        ordered_date = timezone.now()
        order =Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.cart_product.add(cart_item)
        messages.info(request, "this Product quantity was updated")
        return redirect("product_details", slug=slug)
    


def card_increment(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item, created = Cart_Product.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check the order item is in the order
        if order.cart_product.filter(product__slug=product.slug).exists():
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, 'This product quantity updated')
            return redirect('cart_summary')
        
        
    else:
        messages.info(request, "this Product quantity was updated")
        return redirect("cart_summary")
    

def card_decrement(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item, created = Cart_Product.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check the order item is in the order
        if order.cart_product.filter(product__slug=product.slug).exists():
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.info(request, 'This product quantity remove')
                return redirect('cart_summary')
        
        
            else:
                cart_item.delete()
                messages.info(request, "this Product delete")
                return redirect("cart_summary")
    

@login_required(login_url='login')
def remove_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check the order item is in the order
        if order.cart_product.filter(product__slug=product.slug).exists():
            cart_item = Cart_Product.objects.filter(user=request.user, ordered=False)[0]
            cart_item.delete()
            messages.info(request, 'This product Delete')
            return redirect('cart_summary')
    
    else:
        messages.info(request, "this Product Empty")
        return redirect("/")




def cart_summary(request):
    try:
        order =Order.objects.get(user= request.user, ordered=False)
        context={
            'order':order
        }
        return render(request, 'store/cart-summary.html',context)
    
    except ObjectDoesNotExist:
        messages.error(request, 'yor cart is empty')
        return redirect('/')
    

def not_found(request,exception):
    return render(request, 'store/404.html')