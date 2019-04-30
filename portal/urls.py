from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import CustomLoginForm


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='portal/login.html', authentication_form=CustomLoginForm), name='login'),
    # url(r'^login/$', LoginView.as_view(template_name='portal/login.html',),
    #     name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    url(r'^signup/$', views.signup, name='signup')
]
