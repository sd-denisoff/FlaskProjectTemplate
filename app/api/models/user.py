from app.api.models import *


class User(Model):
    id = CharField(primary_key=True)
    name = TextField(null=True, default=None)

    class Meta:
        database = db
        db_table = 'Users'
