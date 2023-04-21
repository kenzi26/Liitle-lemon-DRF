from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, throttle_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from .throttles import TenCallsPerMinutes

from  rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group


@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        items= MenuItem.objects.all()
        serialized_item= MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item= MenuItemSerializer(data= request.data)
        serialized_item.is_valid(raise_exception= True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request,id):
    item= get_object_or_404(MenuItem,pk=id)
    serialized_item= MenuItemSerializer(item)
    return Response(serialized_item.data)


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "some secret message"})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name= 'Manager').exists():
        return Response({"message":"only manager should see this"})
    else:
        return Response({"message": "YOU ARE NOT AUTHORIZED!!"}, 403)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message": "successful"})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinutes])
def throttle_check_auth(request):
    return Response({"message": "message for the logged in users only"})


@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username= request.data['username']
    if username:
        User= get_object_or_404(User, username= username)
        managers= Group.objects.get(name= "Manager")
        managers.user.set.add(User)
        return Response({"message":"okay"})

    return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST) 





#class MenuItemsView(generics.ListCreateAPIView):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer


#class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
#    queryset= MenuItem.objects.all()
#    serializer_class= MenuItemSerializer
    
