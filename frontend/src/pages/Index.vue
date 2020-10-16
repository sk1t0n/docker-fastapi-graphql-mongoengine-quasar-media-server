<template>
  <q-page>
    <div class="container">
      <div class="row">
        <div
          class="col-lg-4 col-md-6 col-sm-12 col-xs-12 q-pa-md"
          v-for="item in videos"
          :key="item.url"
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
              <a class="text-white">{{ item.title }}</a>
            </q-card-section>

            <q-card-section class="card-summary">
              {{ item.summary }}
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
const videos = [
  {
    title: 'Are You Doing the Right Way',
    summary: 'Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.',
    genres: [
      {
        name: 'Genre 1'
      },
      {
        name: 'Genre 2'
      }
    ],
    releaseDate: '10.10.2020',
    runtime: 94,
    url: '#'
  },
  {
    title: 'Are You Doing the Right Way',
    summary: 'Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.',
    genres: [
      {
        name: 'Genre 1'
      },
      {
        name: 'Genre 2'
      }
    ],
    releaseDate: '10.10.2020',
    runtime: 94,
    url: '#'
  },
  {
    title: 'Are You Doing the Right Way',
    summary: 'Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.',
    genres: [
      {
        name: 'Genre 1'
      },
      {
        name: 'Genre 2'
      }
    ],
    releaseDate: '10.10.2020',
    runtime: 94,
    url: '#'
  },
  {
    title: 'Are You Doing the Right Way',
    summary: 'Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.',
    genres: [
      {
        name: 'Genre 1'
      },
      {
        name: 'Genre 2'
      }
    ],
    releaseDate: '10.10.2020',
    runtime: 94,
    url: '#'
  },
  {
    title: 'Are You Doing the Right Way',
    summary: 'Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.',
    genres: [
      {
        name: 'Genre 1'
      },
      {
        name: 'Genre 2'
      }
    ],
    releaseDate: '10.10.2020',
    runtime: 94,
    url: '#'
  },
  {
    title: 'Are You Doing the Right Way',
    summary: 'Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.',
    genres: [
      {
        name: 'Genre 1'
      },
      {
        name: 'Genre 2'
      }
    ],
    releaseDate: '10.10.2020',
    runtime: 94,
    url: '#'
  }
]

export default {
  name: 'PageIndex',
  data () {
    return {
      videos: videos
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
