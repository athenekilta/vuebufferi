<template>
  <div id="app">
    <Navigation v-bind:user="{name: 'Sampo', balance: 2770}" />
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
