import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """Фикстура для API клиента"""
    return APIClient()

# создаем фабрику курсов
@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make("Course", **kwargs)  # модель, параметры
    return factory


# создаем фабрику студентов
@pytest.fixture
def students_factory():
    def factory(**kwargs):
        return baker.make('Student', **kwargs)
    return
