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

    def resolve_videos(self, info, skip, limit):
        return services.get_video_list(skip, limit)

    def resolve_video(self, info, id):
        return services.get_video_detail(id)


class CreateVideo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        summary = graphene.String(default_value="")
        genres = graphene.List(graphene.String, default_value=[])
        release_date = graphene.Date()
        runtime = graphene.Int(required=True)

    video = graphene.Field(Video)

    def mutate(self, info, title, summary, genres, release_date, runtime):
        video = services.create_video(
            title=title,
            summary=summary,
            genres=genres,
            release_date=release_date,
            runtime=runtime
        )

        return CreateVideo(video=video)


class DeleteVideo(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    result = graphene.Boolean()

    def mutate(self, info, id):
        result = services.delete_video(id)

        return DeleteVideo(result=result)


class Mutation(graphene.ObjectType):
    create_video = CreateVideo.Field()
    delete_video = DeleteVideo.Field()
