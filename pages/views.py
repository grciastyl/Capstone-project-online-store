from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"New contact message from {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # your email
                fail_silently=False,
            )

            # Optional: show success message
            messages.success(request, "Thank you! Your message has been sent.")
            return redirect('contact')  # redirect to avoid re-submission

    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})



def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def signup_view(request):
    return render(request, 'users/signup.html')
