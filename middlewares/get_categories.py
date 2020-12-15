from django.utils.deprecation import MiddlewareMixin
from core.models import Category

class GetCategories(MiddlewareMixin):

    def process_request(self, request):

        categories = Category.objects.all()
        request.categories = categories

        return None