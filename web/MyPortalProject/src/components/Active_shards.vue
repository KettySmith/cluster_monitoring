<template>
        <div v-if="data_show" id="Active_shards" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
        <div v-else style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;box-shadow: 0 2px 4px rgba(0, 0, 0, .4);display: flex;justify-content: center;align-items: center;">
            <h1 style="color:#9d9d9d;">暂无数据</h1>
        </div>
</template>
 
<script>
import * as echarts from 'echarts'
export default {
  name: '',
  data() {
      return {
          data_show:false,
          Active_shards: '',
          xaxis_date: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],//数据
          yaxis_value:["155", "400", "900", "800", "300", "900", "270"]
      }
  },
  methods: {
      drawLine(id) {
          this.Active_shards = echarts.init(document.getElementById(id))
          this.Active_shards.setOption({
          title: {
              text: 'Active shards'
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
    //   this.$nextTick(function() {
    //     if(this.data_show){
    //         this.drawLine('Active_shards')
    //     }
    //   })
  }
  
  }
</script>
 
