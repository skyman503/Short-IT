from django.shortcuts import render, redirect
from .models import UrlModel
from secrets import token_urlsafe
from django.http import JsonResponse
from ShortIT.settings import url_length, home_url

# Homepage view
def index(request):
    return render(request, 'main/index.html')

# Generating new uniqe url
def make_new_url():
    url = token_urlsafe(url_length)
    unique = 1
    # Checking if url is uniqe
    while unique is not None:
        try:
            unique = UrlModel.objects.get(old_url=url)
            url = token_urlsafe(url_length)
        except UrlModel.DoesNotExist:
            unique = None
            new_url = url
    return new_url

# Saving form via ajax
def add_url(request):
    if request.is_ajax():
        old_url = request.POST.get('old_url', None) # getting data from input old_url
        new_url = make_new_url()
        if 'http:' in old_url[:5] or 'https:' in old_url[:6]:
            if old_url and new_url:
                pair = UrlModel(old_url=old_url, new_url=new_url)
                pair.save()
                response = {
                    'msg': 'Your form has been submited',
                    'valid': 1,
                    'new_url': str(home_url) + 'r/' + str(pair.new_url),
                }
            return JsonResponse(response)
        else:
            response = {
                'msg': 'Enter a valid url !',
                'valid': 0,
            }
            return JsonResponse(response)

# Redirecting url to its original form
def connect(request, new_url):
    try:
        url = UrlModel.objects.get(new_url=new_url)
    except url.DoesNotExist:
        return redirect('main:index')

    old_url = url.old_url
    return redirect(old_url)


