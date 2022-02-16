from django.urls import path

from .views      import KakaoSignInCallBackView

urlpatterns = {
  path('/callback', KakaoSignInCallBackView.as_view()),
}
