import jwt

from django.http                import JsonResponse
from django.conf                import settings							
from .models                    import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            payload = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id=payload['id'])
            
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'} , status = 400)
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper