<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item">
            Hei {{user.name}}!
        </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                <a class="button is-outlined currency">
                    {{currency(user.balance)}}
                </a>
                <a class="button is-danger is-outlined">
                    Kirjaudu ulos
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
   },
   methods: {
       currency(n){
        return (n/100).toLocaleString("fi", {style: "currency", currency:"EUR"})
        }
   }
}
</script>

<style scoped>
.navbar-brand {
    font-size: 1.5rem;
}
</style>
