<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item">
            <strong>Namubufferi</strong>
        </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-end">
        <div class="navbar-item">
            <div class="buttons">
            <a v-if="!user" class="button is-primary">
                Kirjaudu sisään
            </a>
            </div>
        </div>
        </div>
    </div>
    </nav>
</template>

<script>
export default {
  name: 'Navigation',
  props: { 
      user: Object
   }
}
</script>

<style scoped>
</style>
