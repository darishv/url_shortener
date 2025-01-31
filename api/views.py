import random
import string

from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import Url
from .serializers import UrlSerializer


def generate_short_url(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(request):
    short_url= None
    source_url = None

    if request.method == 'POST':
        shortened_url = generate_short_url()

        while Url.objects.filter(shortened_url=shortened_url).exists():
            shortened_url = generate_short_url()

        data = {
            'source_url': request.POST.get('url'),
            'shortened_url': generate_short_url(),
        }

        serializer = UrlSerializer(data=data)

        if serializer.is_valid():
            serializer.save()


        short_url = shortened_url

    return render(request, 'index.html', {'shortened_url': short_url, 'source_url': source_url})


def redirect_to_long_url(request, shortened_url):
    try:
        url_instance = Url.objects.get(shortened_url=shortened_url)
        return redirect(url_instance.source_url)  # Redirect to the long URL
    except Url.DoesNotExist:
        return HttpResponseNotFound("Shortened URL not found")