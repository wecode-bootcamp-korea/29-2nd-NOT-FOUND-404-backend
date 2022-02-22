import jwt,json

from django.views import View
from django.http import JsonResponse

from products.models import Product, ProductObject, ProductStatusEnum, Curriculum
from .models import Creator
from users.models import User
from reviews.models import Review
from communities.models import Media, ProductThumbnailMedia, ProductCoverMedia, ProductObjectMedia, UserMedia, ReviewMedia
from core.s3_storages import s3_client

class ProductView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        product = Product(**data)
        product.save()

        return JsonResponse({'message':product.pk}, status=201)

    @login_decorator
    def patch(self, request, product_id):
        data = json.loads(request.body)
        product = Product.objects.filter(id=product_id)
        product.update(**data)

        return JsonResponse({'message':product.pk}, status=201)

class ProductMediaView(View):
    def post(self, request, product_id):
        media_category = request.POST.get('mediaCategory', None)
        files = request.FILES.getlist("images", None)

        for file in files:
            image_url = s3_client.upload(file)
            image_info = Media(storage_path=image_url)
            image_info.save()

            if media_category=='productCover':
                product = Product.objects.get(id=product_id)
                product_cover_media_info = ProductCoverMedia(media=image_info, product=product)
                product_cover_media_info.save()

            if media_category=='productThumbnail':
                product = Product.objects.get(id=product_id)
                product_thumbnail_media_info = ProductThumbnailMedia(media=image_info, product=product)
                product_thumbnail_media_info.save()
        return JsonResponse({"message": "Image Upload Success"})

class ProductObjectView(View):
    @login_decorator
    def post(self, request, product_id):
        data_list = request.POST.getlist("dataList")
        files = request.FILES.getlist("image", None)

        json_data = [json.loads(data) for data in data_list]

        for i in range(0, len(files)):
            data = json_data[i]

            product_object = ProductObject.objects.create(
                product_id = product_id,
                title      = data['title'],
                content    = data['content']
            )

            image_url = s3_client.upload(files[i])
            image_info = Media(storage_path=image_url)
            image_info.save()

            product_object_media = ProductObjectMedia(media=image_info, product_object=product_object)
            product_object_media.save()

        return JsonResponse({"message" : "Image Upload Success"})

class ProductCurriculumView(View):
    def post(self, request, product_id):
        data = json.loads(request.body)
        curriculums = [Curriculum(product_id=product_id, description=curriculum)
                       for curriculum in data['curriculums']]

        Curriculum.objects.bulk_create(curriculums)

        return JsonResponse({"message" : "SUCCESS"})

class CreatorRegisterView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            file = request.FILES.get("image", None)
            user = request.user

            name = data['name']
            description = data['description']

            image_url = s3_client.upload(file)
            image_info = Media(storage_path=image_url)
            image_info.save()

            user_media = UserMedia(media=image_info, user=user)
            user_media.save()

            Creator.objects.create(
                user=user,
                name=name,
                description=description
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message" : "KEYERROR"}, status=401)

