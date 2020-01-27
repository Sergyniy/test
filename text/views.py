from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the text index.")

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('text/', include('text.urls')),
    path('admin/', admin.site.urls),
]

