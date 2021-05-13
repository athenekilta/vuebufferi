<template>
  <div id="app">
    <section class="section">
      <div class="container">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
      </div>
    </section>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
</style>
