# from django.http import HttpResponseRedirect
import logging
from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    name = "Daniyal"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/index.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    logger.debug('Home page requested.')
    logger.info('Home')
    return render(request, 'main/home.html', locals())


def deliveryandpayment(request):
    logger.debug('Deliveryandpayment page requested.')
    logger.info('Deliveryandpaymen')
    return render(request, 'main/deliveryandpayment.html', locals())


def contacts(request):
    logger.debug('Contacts page requested.')
    logger.info('Contacts')
    return render(request, 'main/contacts.html', locals())
