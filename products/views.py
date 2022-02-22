from django.http  import JsonResponse
from django.views import View

from .models import Product, ProductStatus

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.select_related('creator','subcategory').get(id=product_id, status_id=ProductStatus.OPEN.value)

            product_result = {
                'title'              : product.title,
                'subcategory'        : product.subcategory.name,
                'creator_id'         : product.creator.id,
                'price'              : product.price,
                'description'        : product.description,
                'curriculum'         : [{'curriculum': curriculum.description,
                                            'id' : curriculum.id} for curriculum in product.curriculum_set.all()],
                'level'              : product.level,
                'duration'           : product.duration,
                'subtitle'           : product.subtitle,
                'creator_description': product.creator.description,
                'creator_name'       : product.creator.name,
                'creator_image'      : [query.media.storage_path for query in product.creator.user.usermedia_set.all()][0],
                'likes'              : len(product.productlike_set.all()),
                'objects'            : [{'title': object.title,
                                        'content': object.content,
                                        'image': [query.media.storage_path for query in object.productobjectmedia_set.all()][0],
                                        'id' : object.id} 
                                    for object in product.productobject_set.all()],
                'cover_images'       : [query.media.storage_path for query in product.productcovermedia_set.all()],
                'thumbnail'          : [query.media.storage_path for query in product.productthumbnailmedia_set.all()][0],
            }
            return JsonResponse({'product_result': product_result}, status=200) 
              
        except Product.DoesNotExist:
            return JsonResponse({'message': 'product_id error'}, status=400)