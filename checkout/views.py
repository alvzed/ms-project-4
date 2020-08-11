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
    try:
        # Create a new customer object
        user_email = request.user.email
        user_id = request.user.id
        customer = stripe.Customer.create(
            email=user_email
        )
        # At this point, associate the ID of the Customer object with your
        # own internal representation of a customer, if you have one.

        print(user_email)
        print(request.user.id)
        print(customer)

        u = UserProfile.objects.create(user=user_id, stripe_ID=customer.id,
                                       is_delinquent=customer.delinquent)
        print(u)

        return redirect('/checkout/')
    except Exception as e:
        return print(e)
