from django.urls import path
from .views import *


urlpatterns = [

#---------------------READ(viev)----------------------
    path('', index),
    path('it_about/', it_about),
    path('it_blog/', it_blog),
    path('it_blog_detail/', it_blog_detail),
    path('it_blog_grid/', it_blog_grid),
    path('it_career/', it_career),
    path('it_cart/', it_cart),
    path('it_checout/', it_checout),
    path('it_computer_repair/', it_computer_repair),
    path('it_contact/', it_contact),
    path('it_contact_2/', it_contact_2),
    path('it_data_recovery/', it_data_recovery),
    path('it_error/', it_error),
    path('it_faq/', it_faq),
    path('it_home/', it_home),
    path('it_home_dark/', it_home_dark),
    path('it_mobile_service/', it_mobile_service),
    path('it_network_solution/', it_network_solution),
    path('it_news/', it_news),
    path('it_price/', it_price),
    path('it_privacy_policy/', it_privacy_policy),
    path('it_service/', it_service),
    path('it_service_detail/', it_service_detail),
    path('it_service_list/', it_service_list),
    path('it_shop/', it_shop),
    path('it_shop_detail/', it_shop_detail),
    path('it_techn_support/', it_techn_support),
    path('it_term_condition/', it_term_condition),
    path('make_appointment/', make_appointment),
]
