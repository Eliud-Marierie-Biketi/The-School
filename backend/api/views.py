from django.http import JsonResponse
from django.views import View

class ItemListView(View):
    def get(self, request):
        data = {'items': ['item1', 'item2', 'item3']}  # Example data
        return JsonResponse(data)
