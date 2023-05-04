<template>
    <div class="chart">
  
        <div class="panelgroup" style="width:100%;height:200px;font-size:30px;margin-top: 30px;">
      筛选范围
      <el-select v-model="value" clearable placeholder="请选择" style="margin-left: 5%;">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
      <el-button type="primary" @click="compare_query">查询</el-button>
      
    </div>
  
       
    </div>
    </template>
     
    <script>
    import * as echarts from 'echarts'
    import axios from 'axios'
    export default {
      name: '',
      data() {
        return {
          options: [{
          
          value: 'top-5',
          label: 'top-5'
        }, {
          value: 'top-10',
          label: 'top-10'
        }],
        value: ''
        }
      },
      methods: {
        compare_query(){
          
        }
        }
        
      }
    
    
    </script>
    