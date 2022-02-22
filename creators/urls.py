from django.urls import path

from .views import ProductView, ProductMediaView, ProductObjectView, ProductCurriculumView, CreatorRegisterView

urlpatterns = [
    path('/creating', ProductView.as_view()),
    path('/media/<int:product_id>', ProductMediaView.as_view()),
    path('/class-detail/<int:product_id>', ProductObjectView.as_view()),
    path('/curriculum/<int:product_id>', ProductCurriculumView.as_view()),
    path('/register', CreatorRegisterView.as_view())
]