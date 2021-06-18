from django.urls import path
from calculator import views

urlpatterns = [
    path('<str:dish>/', views.recipes)  # URL типа http://127.0.0.1:8000/omlet/?servings=17
                                        # значение переменных dishб servings принимает views.recipes
]
