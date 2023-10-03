# MessengerProject
Проект Мессенджер. 
Данный проект разрабатывался для учебной платформы SkillFactory в качестве итогового задания.
Целью было научиться взаимодействовать с REST API через JavaScript. 
В данном проекте реализованы следующие функции:
1. Регистрация и авторизация пользователей.
2. У каждого пользователя есть доступ к странице профиля.
3. Доступно редактирование профиля (Изменение имени и аватара).
4. Создание, редактирование, просмотр и удаление приватных чатов и групповых комнат, а также ограниченный доступ к чатам.
5. Возможность обмениваться сообщениями внутри чата в режиме реального времени.
6. Сообщения сохраняются в базе данных, поэтому в чате видна история переписки.

В проекте обмен сообщениями в чате построен с помощью WebSockets.
Использованы следующие библиотеки:

* channels            4.0.0
* channels-redis      4.1.0
* daphne              4.0.0
* Django              4.2.4
* django-allauth      0.55.2
* djangorestframework 3.14.0
* Pillow              10.0.0
* redis               5.0.0

