from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^db/', views.rds_hits, name='rds_hits'),
    url(r'^cache/', views.cache_hits, name='cache_hits'),
    url(r'^dynamo/', views.nosql_hits, name='nosql_hits'),
]