from django.conf.urls import url
from . import views

app_name = 'transactions'


urlpatterns = [
    url(r"^add$", views.TransactionAddView.as_view(), name='add'),
    url(r'^get_otp/(?P<otp_1>[0-9]+)/(?P<otp_2>[0-9]+)/$', views.GetOtpView.as_view(),
        name='get_otp'),
    url(r'^list/$', views.TransactionListView.as_view(), name='list'),
]
