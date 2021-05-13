<template>
  <div class="store">
    <Navigation v-bind:user="this.user" v-bind:navigate="this.navigate" />
    <div class="container">
      <h1>This is the store page</h1>
    </div>
  </div>
</template>

<script>
import Navigation from './Navigation.vue'

export default {
  name: 'Store',
  components: {
    Navigation
  },
  props: {
    user: Object,
    navigate: Function
  }
}
</script>

<style scoped>
</style>
