from django.urls import path
from . import views

urlpatterns = [
    path('add_musician/', views.AddMusicianCreateView.as_view(), name='add_musician'),
    path('sign_up/', views.SignUpCreateView.as_view(), name='sign_up'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit_musician/<int:pk>/', views.EditMusicianView.as_view(), name='edit_musician'),
    path('delete_musician/<int:pk>/', views.DeleteMusicianView.as_view(), name='delete_musician'),
    path('delete_musician/<int:pk>/', views.DeleteMusicianView.as_view(), name='delete_musician'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]
