<template>
  <div class="landing">
    <div class="container">
    <h1>This is the landing page</h1>
    <button v-on:click="navigate('Store')">Store!</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Landing',
  props: {
    navigate: Function
  }
}
</script>

<style scoped>
</style>
