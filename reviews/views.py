import json

from django.http  import JsonResponse
from django.views import View

from .models      import Review
from users.utils  import login_decorator

class ReviewView(View):
    def get(self, request, product_id):
        reviews = Review.objects.filter(product_id=product_id)
        results = [
            {
                'user_name' : review.user.name,
                'user_id'   : review.user.id,
                'product_id': review.product.id,
                'content'   : review.content,
                'review_id' : review.id  

            } for review in reviews
        ]
        return JsonResponse({'results': results}, status=200)

    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        Review.objects.create(
            user       = request.user,
            content    = data['content'],
            product_id = data['product_id'],
        )
        
        return JsonResponse({'message':'success'}, status=201)

    @login_decorator
    def delete(self, request):
            Review.objects.filter(id=request.GET.get['review_id'], user_id=request.user).delete()
            return JsonResponse({'message': 'No content'}, status=204)
    
    @login_decorator
    def patch(self, request):
        try:
            data = json.loads(request.body)

            review = Review.objects.get(user=request.user, id=data['review_id'])

            review.update(content=data['content'])
        except Review.DoesNotExist:
            return JsonResponse({'message': 'No review available'}, status=400)