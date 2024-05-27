from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def produtos_api_list(request):
    return Response('ok')