<template>
  <transition name="fade">
    <div v-if="show" class="flex flex-center">
      <q-pagination
        v-model="current"
        :max="pages"
        :max-pages="5"
        :direction-links="true"
        :boundary-links="true"
        @input="loadData"
      />
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Pagination',

  props: {
    queryLoadData: {
      type: Object,
      required: true
    },

    queryDataCount: {
      type: Object,
      required: true
    },

    apollo: {
      type: Object,
      required: true
    }
  },

  data: () => ({
    pages: 1,
    current: 1,
    prev: 1,
    limit: 6,
    show: false
  }),

  async beforeMount () {
    this.$q.loading.show()

    this.loadData()

    const dataCount = await this.apollo.query({
      query: this.queryDataCount
    })
    if (dataCount.data) {
      const key = Object.keys(dataCount.data)[0]
      this.pages = Math.ceil(dataCount.data[`${key}`] / this.limit)
    }

    this.$q.loading.hide()
    this.show = true
  },

  methods: {
    async loadData (currPage) {
      if (this.prev === currPage || (!this.prev && currPage === 1)) {
        return
      }
      this.prev = currPage

      const result = await this.apollo.query({
        query: this.queryLoadData,
        variables: {
          skip: (currPage - 1) * this.limit,
          limit: this.limit
        }
      })
      if (result.data) {
        const key = Object.keys(result.data)[0]
        const items = key.charAt(0).toUpperCase() + key.slice(1)
        this.$store.commit(`update${items}`, result.data[`${key}`])
      }
    }
  }
}
</script>

<style lang="scss">
@media screen and (max-width: 767px) {
  .q-pagination {
    padding-top: 12px;
    padding-bottom: 24px;
  }
}

@media screen and (min-width: 768px) {
  .q-pagination {
    padding-top: 24px;
    padding-bottom: 24px;
  }
}

.no-wrap {
  flex-wrap: wrap;
  justify-content: center;
}

.q-pagination {
  .bg-primary {
    background-color: $pagination-btn-active !important;
  }

  .text-primary {
    color: $pagination-btn-text-color !important;
  }

  .q-btn {
    border-radius: 0px;
    width: 35px;
    height: 35px;
    margin: 5px;
    background-color: $pagination-btn;
    color: white;

    &:hover {
      background-color: $pagination-btn-hover;
    }
  }
}

.fade-enter-active {
  transition: opacity 1s;
}

.fade-enter {
  opacity: 0;
}
</style>
