from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Checking if user has already made that enquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(
                    request, 'You had already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        # Saving contact inquiry to db

        contact = Contact(
            listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Sending mail to realtors
        send_mail(
            'Propery Listing Inquiry',  # Subject of mail
            'There has been inquiry for ' + listing + \
            '. Sign into the admin pannel for more info',  # message
            'ishworpanta10@gmail.com',  # from email
            [realtor_email],  # receiptant
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon. ')

        return redirect('/listings/'+listing_id)
