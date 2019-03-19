from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name = "forms-page"),
    path('snippet',views.snippet_detail)
]