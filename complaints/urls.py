from django.conf.urls import url
from . import views
from .forms import ComplaintAddForm


app_name = "complaints"

urlpatterns = [

    url(r'^add/$', views.ComplaintAddView.as_view(), name='add'),
    url(r'^update/$', views.ComplaintUpdateView.as_view(), name="update"),
    url(r'^delete/$', views.ComplaintDeleteView.as_view(), name="delete"),

]
