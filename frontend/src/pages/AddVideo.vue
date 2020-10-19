<template>
  <q-page>
    <div class="container q-px-md">
      <q-form
        @submit="onSubmit"
        @reset="onReset"
      >
        <h5 class="text-center text-white">Add video</h5>

        <div class="row q-mb-md">
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

        <div class="row q-mb-md">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            clearable
            clear-icon="close"
            color="teal-4"
            v-model="summary"
            label="Summary"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
          />
        </div>

        <div class="row q-mb-md">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            color="teal-4"
            v-model="releaseDate"
            label="Release date"
            mask="date"
            :rules="['date']"
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

        <div class="row q-mb-md">
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

        <div class="row q-mb-md">
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
export default {
  name: 'PageAddVideo',

  data: () => ({
    title: null,
    summary: null,
    releaseDate: null,
    runtime: null,
    url: null
  }),

  methods: {
    onSubmit () {
      console.log('TEST')
    },
    onReset () {
      this.title = null
      this.summary = null
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
