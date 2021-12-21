from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check_username'),
    path('test/', views.test, name='test'),
]

urlpatterns += htmx_urlpatterns
