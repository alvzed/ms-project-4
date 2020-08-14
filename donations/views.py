import math
from django.conf import settings
from django.shortcuts import render, redirect, reverse

import stripe


# Create your views here.
def donate(request):
    """ a view to to return the landing page """

    user = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.public_key = settings.STRIPE_PUBLIC_KEY
    context = {
        'user': user,
        'stripe': stripe,
    }

    return render(request, 'donations/donate.html', context)


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['donationAmount']) * 100

        try:
            customer = stripe.Customer.create(
                email=request.POST['InputEmail'],
                name=request.POST['InputName'],
                source=request.POST['stripeToken']
            )

            charge = stripe.Charge.create(
                customer=customer,
                amount=amount,
                currency='eur',
                description='donation',
            )

            return redirect(reverse('success', args=[amount]))
        except:
            # THIS IS A BAD IDEA
            # this except should, and will, not be bare in future versions
            return redirect(reverse('failure'))


def success(request, args):
    amount = args
    donation = math.trunc((int(amount) / 100))

    context = {
        'amount': amount,
        'currency': '€',
        'donation': donation,
    }
    return render(request, 'donations/success.html', context)


def failure(request):
    return render(request, 'donations/failure.html')
