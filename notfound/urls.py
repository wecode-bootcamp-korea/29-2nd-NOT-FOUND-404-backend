from django.urls import path,include

urlpatterns = [
    path('creators', include('creators.urls')),
    path('users', include('users.urls')),
    path('products', include('products.urls')),
    path('communities', include('communities.urls')),
    path('reviews', include('reviews.urls'))
]
