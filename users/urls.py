from django.urls import path

from .views import KakaoSignInCallBackView

urlpatterns = {
  path('/signin/callback', KakaoSignInCallBackView.as_view())
}
