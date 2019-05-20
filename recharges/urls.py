from django.conf.urls import url
from . import views

app_name = 'recharges'


urlpatterns = [
    url(r'^create/offer_pack/(?P<offer_pack_id>[0-9]+)/$', views.create_with_offer_pack, name='create_with_offer_pack'),
    url(r'^create/custom_pack/$', views.create_with_custom_pack, name='create_with_custom_pack'),
               ]
