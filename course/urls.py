from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from taskTest.views import CourseViewSet, DirectionViewSet, LessonMaterialViewSet, LessonViewSet



router = DefaultRouter()

router.register('api/v1/direction', DirectionViewSet, basename='direction')
router.register('api/v1/course', CourseViewSet, basename='course')
router.register('api/v1/lesson', LessonViewSet, basename='lesson')
router.register('api/v1/material', LessonMaterialViewSet, basename='material')


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/login/' , include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
urlpatterns += router.urls