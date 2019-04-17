from peewee import *


database_proxy = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database = database_proxy


class History(BaseModel):
    src_amount = FloatField()
    src_currency = CharField()
    tgt_amount = FloatField()
    tgt_currency = CharField()
