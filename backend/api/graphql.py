import graphene
from graphene_mongo import MongoengineObjectType

from . import services
from db.models import Video as VideoModel, Genre as GenreModel


class Video(MongoengineObjectType):
    class Meta:
        model = VideoModel


class Genre(MongoengineObjectType):
    class Meta:
        model = GenreModel


class Query(graphene.ObjectType):
    videos = graphene.List(
        Video,
        skip=graphene.Int(default_value=0),
        limit=graphene.Int(default_value=5)
    )
    video = graphene.Field(Video, id=graphene.String())
    genres = graphene.List(
        Genre,
        skip=graphene.Int(default_value=0),
        limit=graphene.Int(default_value=5)
    )
    genre = graphene.Field(Genre, id=graphene.String())

    def resolve_videos(self, info, skip, limit):
        return services.get_video_list(skip, limit)

    def resolve_video(self, info, id):
        return services.get_video_detail(id)

    def resolve_genres(self, info, skip, limit):
        return services.get_genre_list(skip, limit)

    def resolve_genre(self, info, id):
        return services.get_genre_detail(id)


class CreateVideo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        summary = graphene.String(default_value="")
        genres = graphene.List(graphene.String, default_value=[])
        release_date = graphene.Date()
        runtime = graphene.Int(required=True)
        url = graphene.String(required=True)

    video = graphene.Field(Video)

    def mutate(self, info, title, summary, genres, release_date, runtime, url):
        video = services.create_video(
            title=title,
            summary=summary,
            genres=genres,
            release_date=release_date,
            runtime=runtime,
            url=url
        )

        return CreateVideo(video=video)


class DeleteVideo(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    result = graphene.Boolean()

    def mutate(self, info, id):
        result = services.delete_video(id)

        return DeleteVideo(result=result)


class CreateGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, name):
        genre = services.create_genre(name=name)

        return CreateGenre(genre=genre)


class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    result = graphene.Boolean()

    def mutate(self, info, id):
        result = services.delete_genre(id)

        return DeleteGenre(result=result)


class Mutation(graphene.ObjectType):
    create_video = CreateVideo.Field()
    delete_video = DeleteVideo.Field()
    create_genre = CreateGenre.Field()
    delete_genre = DeleteGenre.Field()
