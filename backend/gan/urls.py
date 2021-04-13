from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('gan/',views.initialize_gan.as_view()),

]

