from builtins import id

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from account.models import Profile
from cart.models import Cart
from main.models import Jewelry


def cart_view(request):
    try:
        cart_id = request.session['cart_id']
    except:
        cart_id = None
    if cart_id:
        cart = Cart.objects.get(id=cart_id)

        context = {'cart': cart}
    else:
        context = {'empty': True}
    return render(request, 'cart.html', context)


def cart_add_htmx(request):
    request.session.set_expiry(86400)

    jewelry_id = int(request.POST.get('id', ''))
    jewelry = Jewelry.objects.get(id=jewelry_id)

    try:
        cart_id = request.session['cart_id']
    except:
        cart_new = Cart()
        cart_new.save()
        request.session['cart_id'] = cart_new.id
        cart_id = cart_new.id
    cart = Cart.objects.get(id=cart_id)

    cart.jewelries.add(jewelry)
    cart.save()
    return HttpResponse(
        '<span class="position-absolute top-0 start-100 translate-middle p-1 bg-danger border border-light rounded-circle"> </span>')


def cart_del_htmx(request, cart_id, jewl_id):
    cart = Cart.objects.get(id=cart_id)
    jewl = cart.jewelries.get(id=jewl_id)
    cart.jewelries.remove(jewl)
    cart.save()
    context = {'cart': cart}
    return HttpResponse('')
