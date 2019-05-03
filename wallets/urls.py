from django.conf.urls import url
from . import views

app_name = 'wallet'


urlpatterns = [
    url(r'^$', views.WalletView.as_view(), name='wallet_view'),
]
