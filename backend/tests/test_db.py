from datetime import date

from mongoengine import connect

from db.models import Video, Genre


def setup_module(module):
    global testdb
    testdb = connect('testdb')


def test_video_creation():
    genre1 = Genre(name='genre1')
    genre1.save()
    genre2 = Genre(name='genre2')
    genre2.save()

    video = Video(
        title='First video',
        summary='This is first video',
        release_date=date(2020, 2, 15),
        runtime=110,
        genres=[genre1, genre2]
    )
    video.save()

    assert Video.objects.first().title == video.title
    assert Video.objects.first().genres[0].name == genre1.name


def teardown_module(module):
    testdb.drop_database('testdb')
    testdb.close()
