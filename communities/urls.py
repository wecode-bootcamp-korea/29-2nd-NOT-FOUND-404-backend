from django.urls import path

from .views      import CommunityReviewView, CommunityView

urlpatterns = {
  path('/<int:product_id>', CommunityView.as_view()),
  path('/posts/<int:community_id>', CommunityView.as_view()),
  path('/<int:community_id>/reviews', CommunityReviewView.as_view()),
}