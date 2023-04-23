<template>

    <div id="Status" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
     
</template>
 
<script>
import * as echarts from 'echarts'
export default {
  name: '',
  data() {
      return {
          Status: '',
          xaxis_date: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],//数据
          yaxis_value:["155", "400", "900", "800", "300", "900", "270"]
      }
  },
  methods: {
      drawLine(id) {
          this.Status = echarts.init(document.getElementById(id))
          this.Status.setOption({
          title: {
              text: 'Status'
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
      }
  },
  //调用
  mounted() {
      this.$nextTick(function() {
          this.drawLine('Status')
      })
  }
  
  }
</script>
 
