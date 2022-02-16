from django.urls import path

from creators.views import ProductCreating

urlpatterns = [
    path('/creating', ProductCreating.as_view())
]

