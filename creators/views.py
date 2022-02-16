import jwt,json

from django.views import View
from django.http import JsonResponse,HttpResponse
from django.db import transaction

from products.models import Product
from users.models import User

# 작성중

class ProductCreating(View):
    # @login_decorator
    def post(self, request):

        pending_product_id = request.GET.get('productId', None)
        data = json.loads(request.body)

        if pending_product_id:
            pending_product = Product.objects.filter(id=pending_product_id)

            for field in data:
                pending_product.field = data[field]

            pending_product.save()

            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        else:
            with transaction.atomic():
                new_product = Product()

                for field in data:
                    new_product.field = data[field]

                new_product.save()

class ProductUpdate(View):
    def post(self, request):

        data = json.loads(request.body)

        user = request.user
        user = User.objects.filter(kakao_id=user.kakao_id)












