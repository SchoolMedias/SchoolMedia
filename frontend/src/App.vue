<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-link to="/video">视频</router-link>
    <router-link to="/meeting">会议</router-link>
    <router-link to="/live">直播</router-link>
    <router-link to="/user">用户</router-link>
    <router-link to="/123">home</router-link>
    <router-link to="/321">hello</router-link>
    <router-link to="/register">register</router-link>
    <router-view/>
  </div>
</template>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
