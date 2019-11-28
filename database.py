from peewee import *
from os import path

ROUTE = path.dirname(path.realpath(__file__))

dBs = SqliteDatabase(path.join(ROUTE, "schedules.db"))


class Schedules(Model):
    task = CharField()
    place = CharField()
    date = CharField()
    time = CharField()

    class Meta:
        database = dBs


Schedules.create_table(fail_silently=True)


class Users(Model):
    company = CharField()
    amount = CharField()
    date = CharField()

    class Meta:
        database = dBs


Users.create_table(fail_silently=True)
