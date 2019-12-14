from peewee import (
    SqliteDatabase, Model, SQL,
    AutoField, CharField, IntegerField, TextField, TimestampField, DateTimeField, DateField
)

db = SqliteDatabase("db.sqlite")

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
        
class Proxy(Model):
    id = AutoField
    host = TextField(null=False)    
    http_port = TextField(null=False)
    ssl_port = TextField(null=False)
    ftp_port = TextField(null=False)
    socks_port = TextField(null=False)
    username = TextField(null=False)
    password = TextField(null=False)
    type = TextField(null=True)    # http, https, socks5
    vendor = TextField(null=False)
    created_at = TimestampField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    payed_till = DateField(null=True)
    status = IntegerField(null=False, default=1)    # 1 - active    
    class Meta:
        database = db
        db_table = 'proxy'

class Attempt(Model):
    id = AutoField
    login_id = IntegerField(null=False)
    login_url = TextField(null=False)
    proxy_id = TextField(null=True)
    created_at = TimestampField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    msg =  TextField(null=False, default='')
    error = TextField(null=True)
    success = IntegerField(null=True)
    class Meta:
        database = db
        db_table = 'attempts'

def main():
    Login.create_table()
    Attempt.create_table()
    Proxy.create_table()

if '__main__' ==  __name__:
    main()
