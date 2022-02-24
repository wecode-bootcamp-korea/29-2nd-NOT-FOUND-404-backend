from django.urls import path

from .views import CategoryListView, CategoryProductListView, MainProductListView, ProductLikeView, ProductDetailView

urlpatterns = [
  path('/categories', CategoryListView.as_view()),
  path('/categories/<int:subcategory_id>', CategoryProductListView.as_view()),
  path('/lists', MainProductListView.as_view()),
  path('/likes', ProductLikeView.as_view()),
  path('/<int:product_id>', ProductDetailView.as_view()),
]