import mongoengine as me


class Video(me.Document):
    meta = {'collection': 'video'}
    title = me.StringField(max_length=150, required=True)
    summary = me.StringField(max_length=300)
    genres = me.ListField(me.ReferenceField('Genre'))
    release_date = me.DateField()
    runtime = me.IntField(required=True)
    url = me.StringField(required=True)


class Genre(me.Document):
    meta = {'collection': 'genre'}
    name = me.StringField(max_length=50, required=True, unique=True)
