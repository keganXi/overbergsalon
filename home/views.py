# sendemail/views.py


from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template

from .form import ContactForm

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def homepage(request):
    context = {}
    return render(request, "home/index.html", context)


def pricing_list(request):
    context = {}
    return render(request, "home/PricingPage.html", context)


def product_list(request):
    context = {}
    return render(request, "home/ProductPage.html", context)


def portfolio(request):
    context = {}
    return render(request, "home/PortfolioPage.html", context)


def contact_us(request):
    Contact_Form = ContactForm
    if request.method == "POST":
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template("home/contact_form.txt")

            content = {
                'contact_name': request.POST.get('contact_name'),
                'contact_email': request.POST.get('contact_email'),
                'contact_content': request.POST.get('content'),
            }

            content = template.render(content)

            email = EmailMessage(
                "New contact form email",
                content,
                "Overberg Unisex Beauty Salon" + "",
                ["overbergunisexbeautysalon@Gmail.com"],
                headers={"Reply To": contact_email},
            )

            email.send()

    return render(request, "home/ContactPage.html", {"form": Contact_Form})
