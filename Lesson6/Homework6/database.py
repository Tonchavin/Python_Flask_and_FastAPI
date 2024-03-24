from databases import Database
from sqlalchemy import MetaData, Table, Column, create_engine, ForeignKey, Date
from sqlalchemy import Integer, String, DECIMAL


DB_URL = "sqlite:///../mydatabase.db"

db = Database(DB_URL)

metadata = MetaData()

users = Table("users", metadata,
              Column('id', Integer, primary_key=True),
              Column('firstname', String(80), nullable=False),
              Column('lastname', String(80), nullable=False),
              Column('email', String(128), nullable=False),
              Column('password_hash', String(128), nullable=False),
              )

items = Table("items", metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String(128), nullable=False),
              Column('description', String(512), nullable=True),
              Column('price', DECIMAL, nullable=False),
              )

orders = Table("orders", metadata,
               Column('id', Integer, primary_key=True),
               Column('user_id', ForeignKey('users.id'), nullable=False),
               Column('item_id', ForeignKey('items.id'), nullable=False),
               Column('date', Date, nullable=False),
               Column('status', String(64), nullable=False),
               )

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)
