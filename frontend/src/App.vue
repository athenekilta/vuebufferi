<template>
  <div id="app">
    <Navigation />
    <section class="section">
      <div class="container">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
      </div>
    </section>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Navigation from './components/Navigation.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Navigation
  }
}
</script>

<style>
</style>
