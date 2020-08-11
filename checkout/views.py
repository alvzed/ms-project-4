from django.shortcuts import render, redirect
from django.conf import settings

from .models import UserProfile

import stripe


def subscribe(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    product = stripe.Product.retrieve("prod_HoW9lL2kill8wX")

    context = {
        'product': product,
    }

    return render(request, 'checkout/subscribe.html', context)


def create_customer(request):
    # Reads application/json and returns a response
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # Create a new customer object
    user_email = request.user.email
    user_id = request.user
    customer = stripe.Customer.create(
        email=user_email
    )
    # At this point, associate the ID of the Customer object with your
    # own internal representation of a customer, if you have one.
    existing_user = UserProfile.objects.filter(user=user_id).exists()
    if existing_user:
        return redirect('/library/')
    else:
        UserProfile.objects.get_or_create(user=user_id, stripe_ID=customer.id,
                                   is_delinquent=customer.delinquent)
        return redirect('/checkout/')
