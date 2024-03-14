from django.shortcuts import render, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import FreeShortedUrls, FreeGeneratedQR
from django.core.exceptions import ObjectDoesNotExist
from urlshortener_app.forms import FastShortUrl, FastGenerateQR
from .short_the_url_modules.short_the_url import UrlShortener, GenerateQR
import requests
from requests.exceptions import MissingSchema, ConnectionError, InvalidURL
import time


def base(request):
    return render(request, "base.html")


def short_to_dest_url(request, short_url):
    try:
        if short_url[:2] == "QR":
            dest_object = FreeGeneratedQR.objects.get(url_in_db=short_url)
        else:
            dest_object = FreeShortedUrls.objects.get(url_in_db=short_url)

        if (int(time.time()) - dest_object.dead_link_time) >= 0:
            return render(request, 'urlshortener/error_link_dead_time.html')
        
        return HttpResponseRedirect(dest_object.destination_url)
    except ObjectDoesNotExist:
        return render(request, 'urlshortener/error_link_not_found.html')

def index(request):
    url_fast_short = FastShortUrl()
    qr_form = FastGenerateQR()
    hostname = request.META["HTTP_HOST"]
    scheme = request.scheme
    
    if request.method == 'POST':
        if request.POST.get('action') == 'url':
            destination_url = request.POST.get('input_url')
        
            if (destination_url.split('/')[0] != 'https:'):
                destination_url = 'https://' + destination_url
        
            time_option = request.POST.get('options_time')
        
            try:
                requests.get(url=destination_url)
                result_url = UrlShortener.short_url_free(host_url=scheme + "://" + hostname + "/")
                FreeShortedUrls.objects.create(destination_url=destination_url, ttl=int(time_option) / 60, dead_link_time=int(time.time()) + int(time_option), url_in_db=result_url[0])
                return render(request, "urlshortener/urlshortener_main_page.html", {'form': url_fast_short, 'form_qr': qr_form, 'short_url': result_url[1]})
            except Exception as exception:
                exceptions = {
                    'MissingSchema': {
                                    'form': url_fast_short,
                                    'error': 'Не удалось сократить URL!',
                                    'form_qr': qr_form
                                    },
                    'ConnectionError': {
                                    'form': url_fast_short,
                                    'error_connection': destination_url,
                                    'form_qr': qr_form,
                                    },
                    'InvalidURL': {
                                    'form': url_fast_short,
                                    'error_invalid_url': 'Неверно указан URL!',
                                    'form_qr': qr_form
                                }
                }
                return render(request, "urlshortener/urlshortener_main_page.html", context=exceptions[exception.__class__.__name__])
        elif request.POST.get('action') == 'qr':
            destination_url = request.POST.get('input_url_qr')
            if (destination_url.split('/')[0] != 'https:'):
                destination_url = 'https://' + destination_url
        
            time_option_qr = request.POST.get('options_time_qr')
        
            try:
                requests.get(url=destination_url)
                result_qr_list = GenerateQR.generate_qr_free(host_url=scheme + "://" + hostname + "/")
                FreeGeneratedQR.objects.create(destination_url=destination_url, ttl=int(time_option_qr) / 60, dead_link_time=int(time.time()) + int(time_option_qr), url_in_db=result_qr_list[1])
                return render(request, "urlshortener/urlshortener_main_page.html", {'form': url_fast_short, 'form_qr': qr_form, 'text_under_qr': "Ваш QR-код", 'path_to_qr': result_qr_list[0]})
            except Exception as exception:
                exceptions = {
                    'MissingSchema': {
                                    'form': url_fast_short,
                                    'error': 'Не удалось сократить URL!',
                                    'form_qr': qr_form,
                                    'text_under_qr': "Здесь будет QR-код после его генерации",
                                    },
                    'ConnectionError': {
                                    'form': url_fast_short,
                                    'error_connection': destination_url,
                                    'form_qr': qr_form,
                                    'text_under_qr': "Здесь будет QR-код после его генерации",
                                    },
                    'InvalidURL': {
                                    'form': url_fast_short,
                                    'error_invalid_url': 'Неверно указан URL!',
                                    'form_qr': qr_form,
                                    'text_under_qr': "Здесь будет QR-код после его генерации"
                                }
                }
                return render(request, "urlshortener/urlshortener_main_page.html", context=exceptions[exception.__class__.__name__])
    else:        
        return render(request, "urlshortener/urlshortener_main_page.html", {'form': url_fast_short, 'form_qr': qr_form, 'text_under_qr': "Здесь будет QR-код после его генерации"})

