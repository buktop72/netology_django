import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
# from tests.conftest import course_factory, students_factory

# 1 проверка получения 1го курса
@pytest.mark.django_db
def test_courses_retrieve(api_client, course_factory):
    course = course_factory()  # создаем курс на фабрике
    url = reverse("courses-detail", args=(course.id,))  # создаем url
    response = api_client.get(url)  # с тестового клиента отправляем запрос
    assert response.status_code == HTTP_200_OK  # проверяем код возврата
    assert course.id == response.data['id']        # Провереяем, что вернулся курс, который создали
    assert course.name == response.data['name']    # или так


# 2 проверка получения списка курсов
@pytest.mark.django_db
def test_courses_list(api_client, course_factory):
    courses = course_factory(_quantity=5)  # сделать на фабрике 5 курсов
    url = reverse("courses-list")
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert len(courses) == len(response.data)


# 3 проверка фильтрации списка курсов по `id`
# создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
@pytest.mark.django_db
def test_filter_id(api_client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-list")
    # передаем id одного курса в фильтр
    id = 3
    data = {'id': id}
    response = api_client.get(url, data=data)
    response_json = response.json()  # преобразуем ответ в jason
    assert response.status_code == HTTP_200_OK
    assert response_json[0]['id'] == id


# 4 проверка фильтрации списка курсов по `name`
@pytest.mark.django_db
def test_filter_name(api_client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse("courses-list")
    response = api_client.get(url, data={'name': f'{courses[0].name}'})
    assert response.status_code == HTTP_200_OK
    resp_data = response.data
    assert courses[0].name == resp_data[0]['name']


# 5 тест успешного создания курса
@pytest.mark.django_db
def test_course_create(api_client):
    course = {'name': 'test_Course'}
    url = reverse("courses-list")
    response = api_client.post(url, data=course)
    assert response.status_code == HTTP_201_CREATED
    resp = api_client.get(url, data={'name': f'{course["name"]}'})
    resp_json = resp.json()
    assert resp_json[0]['name'] == course['name']


# 6 тест успешного обновления курса
@pytest.mark.django_db
def test_course_update(api_client, course_factory):
    # создание курса
    course = course_factory(name='test_course')
    data_id = course.id  # получаем id созданного курса

    # проверяем, что курс создан
    data = {'name': 'test_course'}
    url = reverse("courses-list")
    response = api_client.get(url, data=data)
    assert response.status_code == HTTP_200_OK

    # обновляем
    up_data = {'id': data_id, 'name': 'update_test_course'}
    url_upd = reverse("courses-detail", args=(data_id,))
    response_upd = api_client.patch(url_upd, data=up_data)
    assert response_upd.status_code == HTTP_200_OK

    # # проверяем что имя обновилось
    response_get = api_client.get(url, data={'id': data_id})
    response_get_json = response_get.json()
    assert response_get_json[0]['name'] == 'update_test_course'


# 7 тест успешного удаления курса
@pytest.mark.django_db
def test_curse_delete(api_client, course_factory):
    # создание курса
    course = course_factory(name='test_del_course')
    data_id = course.id  # получаем id созданного курса

    # проверяем, что курс создан
    data = {'name': 'test_del_course'}
    url = reverse("courses-list")
    response = api_client.get(url, data=data)
    assert response.status_code == HTTP_200_OK

    # Удаляем курс
    url_del = reverse("courses-detail", args=(data_id,))
    response_upd = api_client.delete(url_del, args=data_id,)
    assert response_upd.status_code == HTTP_204_NO_CONTENT
