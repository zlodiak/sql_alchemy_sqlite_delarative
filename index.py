import random
from sqlalchemy import create_engine, Table, MetaData, select, Column, String, Integer
from sqlalchemy.sql import and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///db.sqlite3')
connection = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()


class Quotes(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    text = Column(String(1000), nullable=False)
    weight = Column(Integer, nullable=False)


quotes_json = []
with open("text.txt") as file_handler:
    for line in file_handler:
        quotes_json.append(
            Quotes(text=line, weight=random.randint(1, 10))
        )


session.add_all(quotes_json)
session.commit()


result = session.query(Quotes).filter(Quotes.weight > 3).filter(Quotes.weight < 8)
for row in result:
    print(row.id, row.text[:20] + '...', row.weight)





