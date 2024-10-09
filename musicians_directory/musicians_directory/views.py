from django.shortcuts import render
from album.models import Album
from django.views.generic import ListView


class HomeView(ListView):
    model = Album
    template_name = 'home.html'