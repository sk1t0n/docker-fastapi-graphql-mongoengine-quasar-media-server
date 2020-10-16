<template>
  <q-item
    clickable
    tag="a"
    :href="url"
  >
    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: 'MobileMenu',
  props: {
    title: {
      type: String,
      required: true
    },
    url: {
      type: String,
      default: '#'
    }
  }
}
</script>
