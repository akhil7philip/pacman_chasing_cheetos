from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'v1/product/', views.ProductAPIView.as_view(), name='Product')
]

urlpatterns = format_suffix_patterns(urlpatterns)
