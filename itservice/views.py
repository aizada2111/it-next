from django.shortcuts import render
from .models import *


#CRUD
#---------------------READ(viev)----------------------
def index(request):
    return render(
        request,
        'itservice/index.html'
    )

def it_about(request):
    return render(
        request,
        'itservice/it_about.html'
    )

def it_blog(request):
    return render(
        request,
        'itservice/it_blog.html'
    )

def it_blog_detail(request):
    return render(
        request,
        'itservice/it_blog_detail.html'
    )

def it_blog_grid(request):
    return render(
        request,
        'itservice/it_blog_grid.html'
    )

def it_career(request):
    return render(
        request,
        'itservice/it_career.html'
    )

def it_cart(request):
    return render(
        request,
        'itservice/it_cart.html'
    )

def it_checout(request):
    return render(
        request,
        'itservice/it_checout.html'
    )

def it_computer_repair(request):
    return render(
        request,
        'itservice/it_computer_repair.html'
    )

def it_contact(request):
    return render(
        request,
        'itservice/it_contact.html'
    )

def it_contact_2(request):
    return render(
        request,
        'itservice/it_contact_2.html'
    )

def it_data_recovery(request):
    return render(
        request,
        'itservice/it_data_recovery.html'
    )

def it_error(request):
    return render(
        request,
        'itservice/it_error.html'
    )

def it_faq(request):
    return render(
        request,
        'itservice/it_faq.html'
    )

def it_home(request):
    return render(
        request,
        'itservice/it_home.html'
    )

def it_home_dark(request):
    return render(
        request,
        'itservice/it_home_dark.html'
    )

def it_mobile_service(request):
    return render(
        request,
        'itservice/it_mobile_service.html'
    )

def it_network_solution(request):
    return render(
        request,
        'itservice/it_network_solution.html'
    )

def it_news(request):
    return render(
        request,
        'itservice/it_news.html'
    )

def it_price(request):
    return render(
        request,
        'itservice/it_price.html'
    )

def it_privacy_policy(request):
    return render(
        request,
        'itservice/it_privacy_policy.html'
    )

def it_service(request):
    return render(
        request,
        'itservice/it_service.html'
    )

def it_service_detail(request):
    return render(
        request,
        'itservice/it_service_detail.html'
    )

def it_service_list(request):
    return render(
        request,
        'itservice/it_service_list.html'
    )

def it_shop(request):
    return render(
        request,
        'itservice/it_shop.html'
    )

def it_shop_detail(request):
    return render(
        request,
        'itservice/it_shop_detail.html'
    )

def it_techn_support(request):
    return render(
        request,
        'itservice/it_techn_support.html'
    )

def it_term_condition(request):
    return render(
        request,
        'itservice/it_term_condition.html'
    )

def make_appointment(request):
    return render(
        request,
        'itservice/make_appointment.html'
    )



