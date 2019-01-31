from django.urls import path

from . import views


urlpatterns = [
    path('shipping', views.get_shipping_ratio, name='shipping'),
    path('top', views.get_top_good, name='top'),
    path('cohort', views.get_cohort, name='cohort'),
]