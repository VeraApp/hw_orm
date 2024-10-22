import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json

from models import create_tables, Publisher, Book, Shop, Stock, Sale

def load_test_data(filename, session):
    with open(filename, 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


DSN = 'postgresql://postgres:1@localhost:5434/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

load_test_data("test_data.json", session)
publisher_name = input('Введите имя автора или его id :')

subq = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Book).\
    join(Publisher, Book.id_publisher == Publisher.id).\
    join(Stock, Book.id == Stock.id_book).\
    join(Shop, Stock.id_shop == Shop.id).join(Sale, Stock.id == Sale.id_stock)
if publisher_name.isdigit():
    subq = subq.filter(Publisher.id == int(publisher_name)).all()
else:
    subq=subq.filter(Publisher.name.like(f'%{publisher_name}%')).all()

for res in subq:
    print('|', res[0].center(25), '|', res[1].center(10), '|', str(res[2]).center(5), '|', str(res[3].date()).center(10))

session.close()