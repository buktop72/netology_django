from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advertisements.views import AdvertisementViewSet


router = DefaultRouter()

# подключение `AdvertisementViewSet`
# 'advertisements' - префикс URL, используtvsq с данным роутероv
# AdvertisementViewSet - класс viewset
router.register(r'advertisements', AdvertisementViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # адресная строка после 'api/' отправляется на обработку в роутер
    path('admin/', admin.site.urls),
]
