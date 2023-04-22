<template>
      <div id="Active_shards" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
  </template>
   
  <script>
  import * as echarts from 'echarts'
  export default {
    name: '',
    data() {
        return {
            Active_shards: '',
            opinionData: ["155", "400", "900", "800", "300", "900", "270"]//数据
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
            legend: {
                data: ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']
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
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                name: 'Email',
                type: 'line',
                stack: 'Total',
                data: [120, 132, 101, 134, 90, 230, 210],
                smooth: true

                },
                {
                name: 'Union Ads',
                type: 'line',
                stack: 'Total',
                data: [220, 182, 191, 234, 290, 330, 310],
                smooth: true
                },
                {
                name: 'Video Ads',
                type: 'line',
                stack: 'Total',
                data: [150, 232, 201, 154, 190, 330, 410],
                smooth: true
                },
                {
                name: 'Direct',
                type: 'line',
                stack: 'Total',
                data: [320, 332, 301, 334, 390, 330, 320],
                smooth: true
                },
                {
                name: 'Search Engine',
                type: 'line',
                stack: 'Total',
                data: [820, 932, 901, 934, 1290, 1330, 1320],
                smooth: true
                }
            ]

            })
        }
    },
    //调用
    mounted() {
        this.$nextTick(function() {
            this.drawLine('Active_shards')
        })
    }
    
    }
  </script>
   
