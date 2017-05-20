from sqlalchemy import Table, ForeignKey, INT, String,  MetaData, Column, select


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