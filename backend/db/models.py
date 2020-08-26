import mongoengine as me


class Video(me.Document):
    title = me.StringField(max_length=150, required=True)
    summary = me.StringField(max_length=300)
    genres = me.ListField(me.ReferenceField('Genre'))
    release_date = me.DateField()
    runtime = me.IntField(required=True)


class Genre(me.Document):
    name = me.StringField(max_length=50, required=True)
