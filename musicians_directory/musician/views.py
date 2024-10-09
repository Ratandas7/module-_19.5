from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from musician.models import Musician
from musician.forms import MusicianForm, SignUpForm, UserChangeData, ChangePassword
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import logout
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from album.models import Album

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = './musician/add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class SignUpCreateView(CreateView):
    form_class = SignUpForm
    template_name = './musician/sign_up.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Sign Up'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = './musician/sign_up.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)


    

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logged out Successfully!')
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    model = Album
    template_name = './musician/profile.html'
    context_object_name = 'albums'
    def get_queryset(self):
        return Album.objects.filter(author=self.request.user)


@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = './musician/add_musician.html'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = './musician/delete_musician.html'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    form_class = UserChangeData
    template_name = './musician/edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Profile!')
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class ChangePasswordView(PasswordChangeView):
    form_class = ChangePassword
    template_name = './musician/change_password.html'
    success_url = reverse_lazy('change_password')

    def form_valid(self, form):
        messages.success(self.request, 'Password Changed Successfully!')
        return super().form_valid(form)





    