<template>
  <q-page>
    <div class="container">
      <div class="row">
        <div
          class="col-lg-4 col-md-6 col-sm-12 col-xs-12 q-pa-md"
          v-for="video in videos"
          :key="video.url"
        >
          <q-card
            flat
            bordered
            square
            class="mycard quattrocento-font-regular"
          >
            <q-video
              src="https://www.youtube.com/embed/k3_tw44QsZQ?rel=0"
              :ratio="16/9"
            />

            <q-card-section class="mycard-header">
              <a class="text-white">{{ video.title }}</a>
            </q-card-section>

            <q-card-section class="card-summary">
              {{ video.url }}
            </q-card-section>

            <q-card-section>
              <q-btn
                label="Read more"
                size="16px"
                class="btn-read-more text-white"
                no-caps
                unelevated
                padding="8px 20px"
              />
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { videosWithPaginationQuery } from './../graphql/queries'

export default {
  name: 'PageIndex',

  data: () => ({
    videos: []
  }),

  apollo: {
    videos: {
      query: videosWithPaginationQuery,
      variables: {
        skip: 0,
        limit: 6
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.mycard {
  background-color: $card-background;
  color: $card-text-color;

  .mycard-header {
    font-size: 1.3rem;

    a:hover {
      color: $card-header-hover-text-color !important;
      cursor: pointer;
    }
  }

  .card-summary {
    font-size: 16px !important;
    margin-top: -25px;
    margin-bottom: -15px;
  }

  .btn-read-more {
    border: 1px solid $card-btn-border-color;
    border-radius: 0px;
    font-size: 14px !important;

    &:hover {
      background-color: $card-btn-hover-bg !important;
      border-color: $card-btn-hover-bg;
    }
  }
}
</style>
