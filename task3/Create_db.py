from sqlalchemy import Table, ForeignKey, INT, String, create_engine, MetaData, Column
from sqlalchemy.orm import mapper, relation
import os
import random

#создаеv базу данных описанную в Accounting.py
if os.path.exists("accounting.db"):
    os.remove("accounting.db")
e = create_engine("sqlite:///accounting.db")

metadata = MetaData()
table_workers = Table('workers', metadata,
                      Column('id', INT, primary_key=True),
                      Column('name', String(50)),
                      Column('salary', INT),
                      Column('chief_id', INT, ForeignKey('chiefs.id')),
                      )

table_chief = Table('chiefs', metadata,
                    Column('id', INT, primary_key=True),
                    Column('chief_name', String(50)),
                    Column('salary', INT)
                    )
metadata.create_all(e)

class Worker(object):
    def __init__(self, name='', salary=0, chief_id=0):
        self.name = name
        self.salary = salary
        self.chief_id = chief_id

    def repr(self):
        return "<Person(id:{%d}, name:{%s},salary:{%i}, chief_id:{%i})>" % (
            self.id, self.name, self.salary, self.chief_id)


class Chief(object):
    def __init__(self, chief_name="", salary=0):
        self.chief_name = chief_name
        self.salary = salary

    def repr(self):
        return "<Chief(id:{%d}, chief_name:{%s}, salary:{%i})>" % (self.id, self.chief_name, self.salary)


mapper(Worker, table_workers)
mapper(Chief, table_chief,
       properties={"regions": relation(Chief, uselist=True)})


conn = e.connect()

#===============================================================================================================
#заполняем поля таблиц случайными данными

def fill_worker(names,worker_amount,chief_amount):
    worker_insert = []
    for i in range(worker_amount):
        rand_name = random.randrange(len(names))
        rand_salary = random.randrange(10000, 110000)
        rand_chief = random.randrange(1, chief_amount)
        worker_insert.append({'name': names[rand_name], 'salary': rand_salary, 'chief_id': rand_chief})
    return worker_insert

def fill_chief(names,chief_amount):
    chief_insert = []
    for i in range(chief_amount):
        rand_name = random.randrange(len(names))
        rand_salary = random.randrange(10000, 110000)
        chief_insert.append({'chief_name': names[rand_name], 'salary': rand_salary})
    return chief_insert

def tables_fill():
    names = 'Александр,Алексей,Анатолий,Андрей,Антонин,Аркадий,Артем,Архип,' \
            'Афанасий,Борис,Вадим,Валентин,Валерий,Василий,Виктор,Владимир' \
            ',Вячеслав,Геннадий,Георгий,Глеб,Демьян,Денис,Дмитрий,Евгений,Егор,Елисей'
    names = names.split(',')
    worker_amount = 20
    chief_amount = 5
    conn.execute(table_workers.insert(), fill_worker(names,worker_amount,chief_amount))
    conn.execute(table_chief.insert(), fill_chief(names,chief_amount))
tables_fill()
