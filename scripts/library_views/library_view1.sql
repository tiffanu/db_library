-- Cокрытие полей с персональной информацией
-- посетителей, бравших книгу в библиотеке
create view library.res as
select res_id, name, begin_date, end_date
from library.Reserve
order by begin_date, end_date