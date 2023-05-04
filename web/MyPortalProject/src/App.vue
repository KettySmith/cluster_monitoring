<template>
  <div id="app">
    <router-view/>


     <el-menu 
    :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1"><a href="#/index">集群监控中心</a></el-menu-item>
    <el-menu-item index="2"><a href="#/Similarity">相似度分析</a></el-menu-item>
      </el-menu>
      <component :is="currentView" />

 
  </div>
</template>

<script>

import index from './components/index.vue'
import Similarity from './components/Similarity.vue'
const routes = {
  '/index': index,
  '/Similarity': Similarity
}
export default {
  name: 'App',
  data() {
    return {
      currentPath: window.location.hash,
      activeIndex:'1'
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/'] || NotFound
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
		  this.currentPath = window.location.hash
		})
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
