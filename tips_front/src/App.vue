<template>
<div id="app">
    <div class="logo" style="float:right; padding:20px">
        <img src="./assets/logo.png" width="150px" alt='logo'>
    </div>
    <Listpost/>
</div>
</template>

<script>
import Listpost from './components/Listpost'

export default {
    name: 'App',
    components: {
        Listpost
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
