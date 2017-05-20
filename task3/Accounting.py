'''Структура таблиц следующая:
2 таблицы, рабочие и гачальники,начальники имеют поля id, chief_name, salary
рабочие имеют поля id, name, salary chief_id, где поле chief_id связано
с полем id из таблицы начальников. Таблицы между собой имеют связь однин ко многим.'''

from sqlalchemy import create_engine, select

from task3 import Table_struct as struct

e = create_engine("sqlite:///accounting.db")

t_workers = struct.table_workers
t_chief = struct.table_chief

join_obj = struct.table_workers.join(t_chief,
                              t_workers.c.chief_id == t_chief.c.id)
select_stmt = select([t_workers, t_chief]).select_from(join_obj)
result = e.execute(select_stmt).fetchall()
for row in result:
    if row[2] > row[6]:
        print(row[1])

