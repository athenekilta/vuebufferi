<template>
    <nav class="is-flex is-justify-content-space-between is-flex-direction-row is-align-items-center" role="navigation" aria-label="main navigation">
        <div class="navbar-item title m-0">
            Hei {{user.name}}!
        </div>
        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                <a class="button is-outlined currency">
                    {{currency(user.balance)}}
                </a>
                <a v-on:click="navigate('Landing')" class="button is-danger is-outlined">
                    Kirjaudu ulos
                </a>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>

export default {
  name: 'Navigation',
  props: { 
      user: Object,
      navigate: Function
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
