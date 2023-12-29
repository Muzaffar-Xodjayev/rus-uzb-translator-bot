from peewee import *
from data.config import DB_NAME, DB_USER, DB_HOST, DB_PASS, DB_PORT

# db = PostgresqlDatabase(DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASS, port=DB_PORT)
db = SqliteDatabase("data.db")


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    telegram_id = BigIntegerField(primary_key=True)
    full_name = CharField(max_length=500)
    username = CharField(max_length=300, null=True)
    join_date = DateTimeField(formats=["%d-%m-%Y %H:%M:%S"])

    class Meta:
        db_name = 'users'


class Channels(BaseModel):
    channel_id = BigIntegerField(primary_key=True)
    channel_name = CharField(max_length=200, null=True)
    channel_url = CharField(max_length=200, null=True)

    class Meta:
        db_name = 'channels'
