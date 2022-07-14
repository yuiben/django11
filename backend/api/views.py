from unittest import result
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize


from products.models import Product
from products.serializers import ProductSerializer


def api_home_test(request, *args, **kwargs):
    #request -> HttpRequest ->Django
    print(request.GET) # Url query params
    print(request.POST)
    body = request.body #byte string of JSON data(body ở đây nhận requests.get bên py_clint basic là json nhưng ở dạng b'{})
    # để chuyển dạng byte string về dạng dict trong python ta làm như sau
    data = {}
    try:
        data = json.loads(body) # Byte String of Json data -> Python Dict
    except:
        pass
    print(body) #output la -> b'{"query": "Hello world"}'
    print(data.keys())
    print(data) #sau khi json.loads(body) -> {'query': 'Hello world'}
    
    #data['headers'] = request.headers #request.META ->
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)

def api_home_test1(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    data2 = {}
    if model_data:
        #de covert dữ liệu sang dict ta làm kiểu này
        #Đây là cách 1
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        #đây là cách 2 (nhanh hơn)
        #data2 = model_to_dict(model_data)
        #Với cách 2 ta có thể lựa chọn phần từ thêm vào dict data2
        data2 = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data2)


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    API VIEW
    """
    # if request.method != "POST":
    #     return Response({"Detail": "GET not allowed"}, status=405)
    instance = Product.objects.all().order_by("?").first()
    result = {}
    if instance:
        #data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        result = ProductSerializer(instance).data
    return Response(result)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    API VIEW
    """
    # if request.method != "POST":
    #     return Response({"Detail": "GET not allowed"}, status=405)
    result = request.data
    serialize = ProductSerializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
        # print(serialize.data)
        # data = serialize.data
        instance = serialize.data
        print(instance)
        return Response(serialize.data)
    return Response({"Invalid" : "Not good data"}, status=400)