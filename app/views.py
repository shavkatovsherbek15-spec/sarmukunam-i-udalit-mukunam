from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from .serializers import UserSerializer, ArtistSerializer, AlbumSerializer
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
from .models import Artist, Album
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class clock(UserRateThrottle):
    rate = '5/min'

@api_view(['GET', 'POST'])
@throttle_classes[(clock)]
def hello(request):
    if request.method == 'POST':
        print(request.data)
        return Response({"dingili": "bobo" + str(request.data)})
    return Response({"bugun": "payshanba"})


class Apiview(APIView):
    serializer_class = ArtistSerializer
    throttle_classes = [(clock)]

    def get(self, request):
        artist = Artist.obejcts.all()
        return Response(artist)
    
    def post(self, request):
        return Response({'dingil': "kalon"})
    
# class Generic(ListModelMixin,GenericAPIView):

#     def get(self, request, *args, **kwargs):
#         return list(request, *args, **kwargs)


class listcreate(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
class retrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]

class AlbumViewset(viewsets.ModelViewSet):
    #queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    throttle_scope  = "vaqt"

    def get_queryset(self):
        return Album.objects.all()
