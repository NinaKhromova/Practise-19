from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os


pf = PetFriends()

def test_get_api_key_for_user_with_invalid_email(email=invalid_email, password=valid_password):
    """" Проверяем, что запрос ключа для  пользователя c неправильно указанным email возвращает
    статус ошибки 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = pf.get_api_key(email, password)
    # Проверяем:
    assert status == 403


def test_get_api_key_for_user_with_invalid_password(email=valid_email, password=invalid_password):
    """" Проверяем, что запрос ключа для  пользователя c неправильно указанным password возвращает
    статус ошибки 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = pf.get_api_key(email, password)
    # Проверяем:
    assert status == 403

def test_add_new_pet_with_invalid_data_name(name='%%%%%', animal_type='котЪ',
                                            age='4', pet_photo='images/0-70.jpg'):
    """Проверяем, что нельзя добавить питомца с некорректным именем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

def test_add_new_pet_with_empty_data_animal_type(name='Шаня', animal_type='???*****',
                                                 age='4', pet_photo='images/0-70.jpg'):
    """Проверяем, что нельзя добавить питомца с незаполненным типом животного"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_with_invalid_data_age(name='Шаня', animal_type='Кот',
                                           age='10000000000', pet_photo='images/0-70.jpg'):
    """Проверяем, что нельзя добавить питомца с некорректным возрастом животного"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

def test_add_new_pet_with_invalid_data_pet_photo(name='Шаня', animal_type='Кот',
                                                age='4', pet_photo='images/Боб.txt'):
    """Проверяем, что нельзя добавить питомца с некорректным типом файла изображения животного"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

def test_get_all_pets_with_valid_filter(filter='all pets'):
    """Проверяем возможность отправки запроса на список питомцев с некорректным фильтром"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 400


def test_delete_self_pet_with_invalid_id():
    """Проверяем возможность удаления питомца с некорректным id"""

    # Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Берём некорректный id питомца  и отправляем запрос на удаление
    pet_id = 1111
    status, _ = pf.delete_pet(auth_key, pet_id)

    assert status == 400


def test_add_new_pet_with_data_negative_age(name='Шаня', animal_type='Кот',
                                           age='-5', pet_photo='images/0-70.jpg'):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом животного"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_with_empty_data(name='', animal_type='',
                                     age='', pet_photo='images/0-70.jpg'):
    """Проверяем, что нельзя добавить питомца с незаполненными данными животного"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400













