<template>
  <q-page>
    <div class="container q-px-md">
      <q-form
        @submit="addGenre"
        @reset="resetForm"
      >
        <h5 class="text-center text-white">Add genre</h5>

        <div class="row">
          <q-input
            class="col-xs-12 col-sm-12 col-md-8 offset-md-2"
            dark
            outlined
            clearable
            clear-icon="close"
            color="teal-4"
            v-model="name"
            label="Name"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
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
import { addGenreMutation } from './../graphql/mutations'

export default {
  name: 'AddGenrePage',

  data: () => ({
    name: null
  }),

  methods: {
    async addGenre () {
      await this.$apollo.mutate({
        mutation: addGenreMutation,
        variables: {
          name: this.name
        }
      })

      this.$router.push('/')
    },

    resetForm () {
      this.name = null
    }
  }
}
</script>

<style lang="scss" scoped>
@import url('./../css/form.scss');

main {
  min-height: auto !important;
}

@media screen and (max-width: 991px) {
  .container {
    margin-top: 200px;
  }
}

@media screen and (min-width: 992px) {
  .container {
    margin-top: 250px;
  }
}
</style>
