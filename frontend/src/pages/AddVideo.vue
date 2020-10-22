<template>
  <q-page>
    <div class="container q-px-md">
      <q-form
        @submit="addVideo"
        @reset="resetForm"
      >
        <h5 class="text-center text-white">Add video</h5>

        <div class="row">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            clearable
            clear-icon="close"
            color="teal-4"
            v-model="title"
            label="Title"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
          />
        </div>

        <div class="row">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            clearable
            clear-icon="close"
            color="teal-4"
            v-model="summary"
            label="Summary"
          />
        </div>

        <div class="row">
          <q-select
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            multiple
            dark
            outlined
            clearable
            clear-icon="close"
            color="teal-4"
            v-model="genresSelected"
            :options="genreNames"
            label="Genres"
          />
        </div>

        <div class="row">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            color="teal-4"
            v-model="releaseDate"
            label="Release date"
            mask="date"
            :rules="[val => new Date(val) <= new Date() || 'You cannot choose a date in the future']"
          >
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-menu
                  transition-show="scale"
                  transition-hide="scale"
                  fit
                  anchor="center left"
                  self="center right"
                >
                  <q-date v-model="releaseDate">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-menu>
              </q-icon>
            </template>
          </q-input>
        </div>

        <div class="row">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            color="teal-4"
            v-model.number="runtime"
            type="number"
            label="Runtime"
            lazy-rules
            :rules="[ val => val && val > 0 || 'Runtime must be greater than zero']"
          />
        </div>

        <div class="row">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            clearable
            clear-icon="close"
            color="teal-4"
            v-model="url"
            label="Url"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Specify the path to the video inside the storage folder (example: folder1/1.mp4 or 1.mp4)']"
          />
        </div>

        <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-8 offset-md-2 buttons">
            <q-btn size="20px" label="Submit" type="submit" color="primary" no-caps />
            <q-btn size="20px" label="Reset" type="reset" color="secondary" no-caps />
          </div>
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import gql from 'graphql-tag'

// Date - type graphene-python
const addVideoMutation = gql`
  mutation CreateVideo(
    $title: String!, $summary: String, $genres: [String!], $releaseDate: Date!, $runtime: Int!, $url: String!
  ) {
      createVideo(
        title: $title,
        summary: $summary,
        genres: $genres,
        releaseDate: $releaseDate,
        runtime: $runtime,
        url: $url
      ) {
          video {
            id
            title
            summary
            genres {
              name
            }
            releaseDate
            runtime
            url
          }
      }
  }
`

const genresQuery = gql`
  query AllGenres($skip: Int, $limit: Int) {
    genres(skip: $skip, limit: $limit) {
      id
      name
    }
  }
`

export default {
  name: 'PageAddVideo',

  data: () => ({
    title: null,
    summary: null,
    genreIds: [],
    genreNames: [],
    genresSelected: [],
    releaseDate: null,
    runtime: null,
    url: null
  }),

  async beforeMount () {
    const result = await this.$apollo.query({
      query: genresQuery,
      variables: {
        skip: 0,
        limit: 10
      }
    })
    if (result.data.genres) {
      result.data.genres.forEach(genre => {
        this.genreIds.push(genre.id)
        this.genreNames.push(genre.name)
      })
    }
  },

  methods: {
    getReleaseDate () {
      const dt = new Date(this.releaseDate)
      const month = String(dt.getMonth() + 1).padStart(2, '0')
      const day = String(dt.getDate()).padStart(2, '0')
      const result = `${dt.getFullYear()}-${month}-${day}`
      return result
    },

    getGenres () {
      const result = []
      this.genresSelected.forEach(genre => {
        const indexGenre = this.genreNames.indexOf(genre)
        if (indexGenre >= 0) {
          result.push(this.genreIds[indexGenre])
        }
      })
      return result
    },

    async addVideo () {
      await this.$apollo.mutate({
        mutation: addVideoMutation,
        variables: {
          title: this.title,
          summary: this.summary,
          genres: this.getGenres(),
          releaseDate: this.getReleaseDate(),
          runtime: this.runtime,
          url: this.url
        }
      })

      this.$router.push('/')
    },

    resetForm () {
      this.title = null
      this.summary = null
      this.genresSelected = []
      this.releaseDate = null
      this.runtime = null
      this.url = null
    }
  }
}
</script>

<style lang="scss" scoped>
h5 {
  margin-top: 6rem;
  margin-bottom: 1rem;
}

.q-field--with-bottom {
  padding-bottom: 0px;
}

.row {
  padding-bottom: 16px;
}

@media screen and (max-width: 991px) {
  .buttons .q-btn {
    width: 100%;

    &:first-child {
      margin-bottom: 36px;
    }
  }
}

@media screen and (min-width: 992px) {
  .buttons {
    display: flex;
    justify-content: flex-end;

    .q-btn:last-child {
      margin-left: 20px;
    }
  }
}
</style>
