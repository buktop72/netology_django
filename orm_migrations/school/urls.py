from django.urls import path

from school.views import StudentsList

urlpatterns = [
    path('', StudentsList.as_view(), name='students'),
]
