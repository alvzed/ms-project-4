from django.shortcuts import render, redirect
from django.conf import settings

from .models import UserProfile

import stripe


def subscribe(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.public_key = settings.STRIPE_PUBLIC_KEY

    product = stripe.Product.retrieve("prod_HoW9lL2kill8wX")

    price = stripe.Price.retrieve("price_1HEt6yFztXrGefLPT4HmsC83"),

    context = {
        'product': product,
        'price': price,
        'stripe': stripe,
    }

    return render(request, 'checkout/subscribe.html', context)


def create_customer(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    user_email = request.user.email
    user_id = request.user
    # Create a new Stripe customer object
    customer = stripe.Customer.create(
        email=user_email
    )

    # Create a new UserProfile object if it doesn't already exist
    existing_user = UserProfile.objects.filter(user=user_id).exists()
    if existing_user:
        return redirect('/library/')
    else:
        UserProfile.objects.get_or_create(user=user_id, stripe_ID=customer.id,
                                          is_delinquent=customer.delinquent)
        return redirect('/checkout/')


def plan(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.public_key = settings.STRIPE_PUBLIC_KEY

    product = stripe.Product.retrieve("prod_HoW9lL2kill8wX")

    price = stripe.Price.retrieve("price_1HEt6yFztXrGefLPT4HmsC83")

    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_profile.current_plan_ID = product.id
    user_profile.current_price_ID = price
    user_profile.save()
    return redirect('/checkout/')


def payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.public_key = settings.STRIPE_PUBLIC_KEY

    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    stripe.checkout.Session.create(
        success_url=('https://8000-e111429f-0ac1-4c29-982e-be58b81b8bae.ws-eu01.gitpod.io/checkout/payment'),
        cancel_url=('https://8000-e111429f-0ac1-4c29-982e-be58b81b8bae.ws-eu01.gitpod.io/checkout/'),
        payment_method_types=["card"],
        line_items=[
            {
                "price": user_profile.current_price_ID,
                "quantity": 1,
            },
        ],
        mode="subscription",
    )

    context = {
        'user_profile': user_profile,
        'Stripe': stripe,
    }

    return render(request, 'checkout/payment.html', context)
