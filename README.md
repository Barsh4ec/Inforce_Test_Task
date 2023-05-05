# Inforce Digital Test Task

Спочатку потрібно зібрати проект використовуючи команду `docker-compose build`
Потім запустити за допомогою команди `docker-compose up`

Або, якщо без докеру, то `pip install -r requirements.txt` та `python manage.py runserver`

Після чого можна використовувати API за адресами

`127.0.0.1:8000/api/v1/token/'` - Тут можна отримати JWT токен для доступу до API за допомогою яких можна редагувати дані

`127.0.0.1:8000/api/v1/token/refresh/` - Відповідно, адреса для оновлення токену

`127.0.0.1:8000/api/v1/token/verify/` - Та підтвердження токену

Щоб використати токен, потрібно залогінитись (за 1 адресою) як адмін (admin, 1234), та отримати access токен, після чого його можна використовувати, наприклад в postman, додавши в header key - Authorization, та в поле Value ввівши JWT та access токен


`127.0.0.1:8000/api/v1/get-restaurants/` - За цією адресою можна отримати список доступних ресторанів

`127.0.0.1:8000/api/v1/add-restaurants/` - Створити ресторан `{"name":"name-of-the-restaurant", "address":"address-of-the-restaurant"}`

`127.0.0.1:8000/api/v1/update-restaurants/<str:pk>/` - Оновити дані про ресторан, pk - це id ресторану

`127.0.0.1:8000/api/v1/delete-restaurants/<str:pk>/` - Видалити ресторан, pk - це id ресторану

`127.0.0.1:8000/api/v1/get-menu/` - Отримати список меню на поточний день

`127.0.0.1:8000/api/v1/add-menu/` - Створити меню для ресторану `{"restaurant":"id-of-the-restaurant"}`

`127.0.0.1:8000/api/v1/update-menu/<str:pk>/` - Оновити меню для поточного дня `{"restaurant":"id-of-the-restaurant", "items":"items-of-menu"}` pk - це id меню

`127.0.0.1:8000/api/v1/get-employee/` - Отримати список робітників та їх голосів

`127.0.0.1:8000/api/v1/add-employee/` - додати робітника `{"name":"name-of-the-employee", "surname":"surname-of-the-employee"}`

`127.0.0.1:8000/api/v1/update-employee/<str:pk>/` - Оновити голос за меню робітника `{"name":"name-of-the-employee", "surname":"surname-of-the-employee", "voted_for":"id-of-the-menu}`


Також я створив декілька тестів, запустити які, можна командою `pytest`

А також додав перевірку коду за командою `flake8 InforceTask`