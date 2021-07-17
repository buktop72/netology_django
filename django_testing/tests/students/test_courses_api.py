import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


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
def test_course_update(api_client):
    # создание курса
    course = {'name': 'test_course'}
    url = reverse("courses-list")
    response = api_client.post(url, data=course)
    assert response.status_code == HTTP_201_CREATED

    # проверяем, что курс создан
    response_get = api_client.get(url, data={'name': f'{course["name"]}'})
    response_get_json = response_get.json()
    assert response_get_json[0]['name'] == course['name']

    # обновляем
    response_json = response.json()
    url_upd = reverse("courses-detail", args=(response_json["id"], ))
    course_update = {'name': 'test_course_update'}
    resp_upd = api_client.patch(url_upd, data=course_update)
    assert resp_upd.status_code == HTTP_200_OK

    # проверяем
    resp_get = api_client.get(url, data={'name': f'{course_update["name"]}'})
    resp_get_json = resp_get.json()
    assert resp_get_json[0]['name'] == course_update['name']


# 7 тест успешного удаления курса
@pytest.mark.django_db
def test_curse_delete(api_client):
    course = {'name': 'Test_course'}
    url = reverse("courses-list")
    resp = api_client.post(url, data=course)
    url_get = reverse("courses-list")
    api_client.get(url_get, data={'name': f'{course["name"]}'})
    resp_json = resp.json()
    url_to_del = reverse("courses-detail", args=(resp_json["id"], ))
    resp_del = api_client.delete(url_to_del)
    assert resp_del.status_code == HTTP_204_NO_CONTENT
