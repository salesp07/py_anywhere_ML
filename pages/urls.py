# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, pedroView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('pedro/', pedroView, name='pedro'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
