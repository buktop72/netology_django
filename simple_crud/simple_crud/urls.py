from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from measurements.views import ProjectViewSet, MeasurementViewSet

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

router = DefaultRouter()
router.register('project', ProjectViewSet)
router.register('measurements', MeasurementViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(router.urls))
]
