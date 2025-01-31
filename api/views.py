from django.shortcuts import render, redirect
import pyshorteners
from rest_framework.decorators import api_view

from api.models import Url
from api.serializers import UrlSerializer


def url_shortener(request):
    try:
        short_url = ""
        url = ""
        if request.method == "POST":
            url = request.POST.get("url")
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            new_url_obj = Url(source_url=url, shortened_url=short_url)
            new_url_obj.save()
        return render(
            request, "index.html", {"shortened_url": short_url, "url": url}
        )
    except:
        return render(request, "index.html")