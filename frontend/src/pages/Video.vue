<template>
  <q-page>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 offset-lg-2 q-pa-md">
          <div v-if="video">
            <h4 class="title">{{ video.title }}</h4>

            <video width="100%" controls class="q-my-lg">
              <source :src="video.url | videoUrlByExtension('webm')" type="video/webm">
              <source :src="video.url | videoUrlByExtension('mp4')" type="video/mp4">
            </video>

            <div class="field field-text-size"><span>Release date: </span><span>{{ video.releaseDate }}</span></div>

            <div class="field field-text-size"><span>Runtime: </span><span>{{ video.runtime }}</span></div>

            <p class="field">{{ video.summary }}</p>

            <div class="text-center">
              <q-chip
                v-for="genre in video.genres"
                :key="genre.id"
                :ref="genre.id"
              >
                <a
                  :href="getGenreUrl(genre.id)"
                  @mouseover="btnGenreOver(genre.id)"
                  @mouseleave="btnGenreLeave(genre.id)"
                >
                  {{ genre.name }}
                </a>
              </q-chip>
            </div>
          </div>
          <div v-else class="title">Not found</div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { videoQuery } from '../graphql/queries'
import filterVideoUrlByExtension from '../helpers'

export default {
  name: 'Video',

  data: () => ({
    video: null
  }),

  filters: {
    videoUrlByExtension: filterVideoUrlByExtension
  },

  methods: {
    getGenreUrl: id => `genre/${id}`,
    btnGenreOver (id) {
      this.$refs[id][0].$el.classList.add('animated')
      this.$refs[id][0].$el.classList.add('pulse')
    },
    btnGenreLeave (id) {
      this.$refs[id][0].$el.classList.remove('animated')
      this.$refs[id][0].$el.classList.remove('pulse')
    }
  },

  async beforeMount () {
    const result = await this.$apollo.query({
      query: videoQuery,
      variables: {
        id: this.$route.params.id
      }
    })
    if (result.data) {
      this.video = result.data.video
    }
  }
}
</script>

<style lang="scss" scoped>
.title {
  color: $video-page-title;
  font-size: 2rem;
  margin-bottom: 0px;
  text-align: center;
}

.q-chip {
  background-color: $video-page-bg-genre;
  margin: 30px 10px 0px 10px;
}

a {
  color: white;
  margin-top: -2px;

  &:hover {
    color: black;
    cursor: pointer;
  }
}

.field {
  color: $video-page-text;
  font-size: 1rem;
  margin-bottom: 5px;

  span:first-child {
    color: $video-page-title;
  }
  span:last-child {
    color: $video-page-bg-genre;
  }
}

.field-text-size {
  font-size: 1.2rem;
}

p {
  text-align: justify;
}
</style>
