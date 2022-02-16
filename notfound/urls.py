from django.urls import path, include

urlpatterns = [
    path('creators', include('creators.urls'))
]
