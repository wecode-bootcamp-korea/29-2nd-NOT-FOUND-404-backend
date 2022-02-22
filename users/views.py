import jwt
import requests

from django.views     import View
from django.http      import JsonResponse
from django.conf      import settings

from .models import User, UserRankEnum


class KakaoSignInCallBackView(View):
    def post(self, request):
        access_token = request.headers['access-token']

        user_info_response = requests.post('https://kapi.kakao.com/v2/user/me?', 
                                        headers={'Authorization': f'Bearer {access_token}',
                                        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'},
                                        data=str([{"property_keys":["properties.nickname", "kakao_account.name", "kakao_account.email"]}]))

        user_info_response = user_info_response.json()

        user, is_created = User.objects.get_or_create(
            kakao_id = user_info_response['id'],
            defaults = {
                'name'    : user_info_response['properties']['nickname'],
                'nickname': user_info_response['kakao_account']['profile']['nickname'],
                'rank'    : UserRankEnum.AMATEUR.name
                } 
        )

        token = jwt.encode({'id':user.id}, settings.SECRET_KEY, settings.ALGORITHM)

        return JsonResponse({'token': token}, status=200)