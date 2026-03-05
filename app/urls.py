from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'alboms', views.AlbumViewset)


urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('id/', views.listcreate.as_view(), name ='id'),
    path('id/', views.retrieveupdatedestroy.as_view(), name='idd'),
    path('openapi-schema/', get_schema_view(
        title = 'Albom',
        description= 'Song',
        version= '1.0.0',
        public= True
    ), name='openapi-schema' ),
    path('docs/', TemplateView.as_view(
        template_name = "swagger-ui.html",
        extra_context = {'schema_url': "openapi-schema"}
    ), name='swagger-ui'),
]