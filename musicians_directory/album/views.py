from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from album.models import Album
from album.forms import AlbumForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = './album/add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = './album/add_album.html'
    success_url = reverse_lazy('profile')