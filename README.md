# Проект "Библиотека"



Имеется база данных недавно построенной библиотеки. В ней находится информация об имеющихся книгах, их жанрах и расположении, об авторах и о всех бронированиях книг. Планируется выявить, какие произведения/авторы/жанры являются самыми популярными, и благодаря этому выбрать вектор развития нашей библиотеки.


`library.Book`  

О каждом произведении есть запись в таблице: идентификатор, название и количество экземпляров у библиотеки.

`library.Author`  

В таблице перечислены авторы произведений, чьи книги сейчас лежат на полках заведения. В ней присутствуют ФИО автора, дата рождения и смерти.

`library.Reserve`  

Таблица с бронированием книг. В неё занесены данные о посетителе: его ФИО, паспорт, адрес, номер телефона - а также сроки бронирования.

---

БД имеет 2 НФ.
