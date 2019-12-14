from peewee import *

db = SqliteDatabase("testdb.sqlite")

class Login(Model):
    id = AutoField
    login = CharField(null=False)
    password = CharField(null=False)
    status = IntegerField(null=False, default=0)
    msg = TextField(null=True)
    created_at = TimestampField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    
    class Meta:
        database = db
        db_table = 'logins'
        
Login.create_table()

