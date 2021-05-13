<template>
  <div id="app">
      <component
        v-bind:is="this.view"
        v-bind:user="this.user"
        v-bind:msg="this.view"
        v-bind:navigate="this.navigate"
      />
  </div>
</template>

<script>
import Landing from './components/Landing.vue'
import Store from './components/Store.vue'

export default {
  name: 'App',
  components: {
    Landing,
    Store
  },
  data: () => {
    return {
      view: 'Landing',
      user: {
        name: 'Velho',
        balance: 2770
      }
    }
  },
  methods: {
    navigate(x){
      this.view = x;
    }
  }
}
</script>

<style>
</style>
