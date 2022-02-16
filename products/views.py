from django.http  import JsonResponse
from django.views import View

from .models         import Subcategory, Product, ProductLike, Product, ProductStatusEnum
from users.utils     import login_decorator

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.select_related('creator','subcategory').get(id=product_id, status_id=ProductStatusEnum.OPEN.value)

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
                'creator_image'      : [str(query.media.storage_path) for query in product.creator.user.usermedia_set.all()][0],
                'likes'              : len(product.productlike_set.all()),
                'objects'            : [{'title': object.title,
                                        'content': object.content,
                                        'image': [str(query.media.storage_path) for query in object.productobjectmedia_set.all()][0],
                                        'id' : object.id} 
                                    for object in product.productobject_set.all()],
                'cover_images'       : [str(query.media.storage_path) for query in product.productcovermedia_set.all()],
                'thumbnail'          : [str(query.media.storage_path) for query in product.productthumbnailmedia_set.all()][0],
            }
            return JsonResponse({'product_result': product_result}, status=200) 
              
        except Product.DoesNotExist:
            return JsonResponse({'message': 'product_id error'}, status=400)

class CategoryListView(View):
    def get(self, request):
        subcategories = Subcategory.objects.all().select_related('category')

        results = [
            {
                'id': subcategory.category.id,
                'name': subcategory.name,
                'menu': [
                    {
                        'id': subcategory.id,
                        'name': subcategory.name
                    }
                ]
            } for subcategory in subcategories
        ]

        return JsonResponse({'results':results}, status=200)

class CategoryProductListView(View):
    def get(self, request, subcategory_id):
        products = Product.objects.filter(subcategory_id=subcategory_id, status_id=ProductStatusEnum.OPEN.value).select_related('creator')

        results = [
            {
                'title': product.title,
                'creator': product.creator.name,
                'price': product.price,
                'discount_rate': 33,
                'image_url': [str(media.media.storage_path) for media in  product.productthumbnailmedia_set.all()][0]
            } for product in products
        ]

        return JsonResponse({'results':results}, status=200)

class MainProductListView(View):
    def get(self, request):
        python_product    = Product.objects.filter(subcategory_id=2, status_id=ProductStatusEnum.OPEN.value)[:6]
        products_queryset = Product.objects.filter(status_id=ProductStatusEnum.OPEN.value).order_by('?').select_related('creator')[:24]

        random_products = [
            {
                'id'           : product.id,
                'title'        : product.title,
                'creator'      : product.creator.name,
                'price'        : product.price,
                'discount_rate': 33,
                'image_url'    : [str(media.media.storage_path) for media in  product.productthumbnailmedia_set.all()][0]
            } for product in products_queryset
        ]
        
        python_products = [
            {
                'id'           : product.id,
                'title'        : product.title,
                'creator'      : product.creator.name,
                'price'        : product.price,
                'discount_rate': 33,
                'image_url'    : [str(media.media.storage_path) for media in  product.productthumbnailmedia_set.all()][0]
            } for product in python_product
        ]
        results = [random_products[i:i+6] for i in range(0,len(random_products),6)]

        return JsonResponse({'random_products':random_products, 'python_products': python_products}, status=200)
    
class ProductLikeView(View):
    @login_decorator
    def post(self, request):
        productlike, is_created = ProductLike.objects.get_or_create(
            user = request.user,
            product_id = request.headers.get('product_id')
        )

        return JsonResponse({'message':'Success'}, status=201)
