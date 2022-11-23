import os
if os.path.isfile("env.py"):
    import env
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
        'client_secret': os.environ.get('STRIPE_CLIENT_SECRET'),
    }

    return render(request, template, context)
