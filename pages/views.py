from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
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

            subject = f"New contact message from {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Create and send the email
            email_message = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,  # your Gmail
                to=[settings.EMAIL_HOST_USER],        # where you want to receive it
                reply_to=[email],                     # so you can reply directly to the sender
            )
            email_message.send(fail_silently=False)

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
