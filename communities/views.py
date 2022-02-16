import json

from django.views import View
from django.http  import JsonResponse

from .models         import Community
from creators.models import Creator
from products.models  import Product
from users.utils     import login_decorator

class CommunityView(View):
    def get(self, request, product_id):
        product       = Product.objects.get(id=product_id)
        creator       = Creator.objects.get(id=product.creator.id)
        user_id       = creator.user.id
        announcements = Community.objects.filter(product_id=product_id, user_id=user_id)
        communities   = Community.objects.filter(product_id=product_id).exclude(user_id=user_id)

        if communities.exists():
            reviews = [
                {
                    'user_id'    : community.user.id,
                    'name'       : community.user.name,
                    'product_id' : community.product.id,
                    'content'    : community.content,
                    'id'         : community.id,
                    'post_id'    : community.parent_review.id
                } for community in communities if community.parent_review
            ]
            communities = [
                {
                    'user_id'   : community.user.id,
                    'product_id': community.product.id,
                    'content'   : community.content,
                    'id'        : community.id,
                    'name'      : community.user.name


                } for community in communities if not community.parent_review
            ]
        else: 
            reviews     = []
            communities = []
            
        if announcements.exists():
            announcements = [
                {
                    'user_id'       : announcement.user.id,
                    'creator_name'  : creator.name,
                    'product_id'    : announcement.product_id,
                    'content'       : announcement.content,
                    'creator_image' : [str(query.media.storage_path) for query in creator.user.usermedia_set.all()][0]
                } for announcement in announcements
            ][0]
        else: 
            announcements = []

        return JsonResponse({'communities':communities, 'announcements':announcements, 'reviews':reviews}, status=200)

    @login_decorator
    def post(self, request, product_id):
        data = json.loads(request.body)

        Community.objects.create(
            user             = request.user,
            content          = data['content'],
            product_id       = product_id,
        )
        
        return JsonResponse({'message':'success'}, status=201)

    @login_decorator
    def delete(self, request, community_id):
        Community.objects.filter(id=community_id, user=request.user).delete()
        return JsonResponse({'message': 'No content'}, status=204)
    
    @login_decorator
    def patch(self, request, community_id):
        try:
            data = json.loads(request.body)

            community = Community.objects.get(user=request.user, id=community_id)

            community.content = data['content']
            community.save()

        except Community.DoesNotExist:
            return JsonResponse({'message': 'No community available'}, status=400)

class CommunityReviewView(View):
    @login_decorator
    def post(self, request, commnity_id):
        data = json.loads(request.body)
    
        Community.objects.create(
            user       = request.user,
            content    = data['content'],
            product_id = data['product_id'],
            parent_id  = commnity_id
        )

        return JsonResponse({'message':'success'}, status=201)