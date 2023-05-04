<template>
    <div>
      <Curve_all />
      <Curve_compare />
    </div>
  </template>
  
  <script>
  import * as echarts from 'echarts'
  import axios from 'axios'
  import Curve_all from './Curve_all.vue'
  import Curve_compare from './Curve_compare.vue'
  export default {
    name: '',
    components: {
      Curve_all,
      Curve_compare
    },
    data() {
      return {
      }
    },
    methods: {
  
    }
  
  }
  
  </script>