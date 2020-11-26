from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='home'),
    path('countthewordsbruh/', views.count, name='count'),
    path('about_site/', views.about_page, name='about')
]
