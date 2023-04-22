<template>
    <div class="chart" style="display: flex;">
      <div style="width:80%;">
        <div id="Number_nodes" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
      </div> 
      <div style="width:20%;text-align: center;">
        <el-button type="primary" @click="onSubmit" style="margin-top:50%" >点击显示</el-button>
      </div>
    </div> 
</template>
 
<script>
import * as echarts from 'echarts'
export default {
  name: '',
  data() {
      return {
          Number_nodes: '',
          xaxis_date: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],//数据
          yaxis_value:["155", "400", "900", "800", "300", "900", "270"]
      }
  },
  methods: {
      drawLine(id) {
          this.Number_nodes = echarts.init(document.getElementById(id))
          this.Number_nodes.setOption({
          title: {
              text: 'Number of Nodes'
          },
          tooltip: {
              trigger: 'axis'
          },
          
          grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
          },
          toolbox: {
              feature: {
              saveAsImage: {}
              }
          },
          xAxis: {
              type: 'category',
              boundaryGap: false,
            //   data: xaxis_date
              data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          },
          yAxis: {
              type: 'value'
          },
          series: [
              {
              type: 'line',
            //   data: yaxis_value,
              data:["155", "400", "900", "800", "300", "900", "270"],
              smooth: true
              }
          ]

          })
      },
      onSubmit(){
        
    }
  },
  //调用
  mounted() {
      this.$nextTick(function() {
          this.drawLine('Number_nodes')
      })
  }
  
  }
</script>
 
