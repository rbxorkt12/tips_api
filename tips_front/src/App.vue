<template>
<div id="app">
    <title key="helloworld"></title>
    <img alt="Vue logo" src="./assets/logo.png">
    <Listpost msg="Welcome to Your Vue.js App" />
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
