<template>
    <div class="chart" style="display: flex;">
      <div style="width:80%;">
        <div id="Transport_tx" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
      </div> 
      <div style="width:20%;text-align: center;">
        <el-select
            v-model="selectedArr"
            multiple
            collapse-tags
            filterable
            style="margin-top:50%;"
            placeholder="请选择"
            @change='changeSelect'>
            <el-checkbox v-model="checked" @change='selectAll' style="text-align: right;width: 90%;">全选</el-checkbox>
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
        </el-select>
        <el-button type="primary" @click="onSubmit" style="margin-top:50%" >查询</el-button>
      </div>
    </div> 
</template>
 
<script>
import * as echarts from 'echarts'
export default {
  name: '',
  data() {
      return {
          Transport_tx: '',
          node_list:[],
          xaxis_date:'',
          checked: false,
          selectedArr: [],
          options: [{
          value: '选项1',
          label: 'node1'
        }, {
          value: '选项2',
          label: 'node2'
        }, {
          value: '选项3',
          label: 'node3'
        }, {
          value: '选项4',
          label: 'node4'
        }, {
          value: '选项5',
          label: 'node5'
        }]

      }
  },
  methods: {
    drawLine(id) {
        this.Transport_tx = echarts.init(document.getElementById(id))
        this.Transport_tx.setOption({
        title: {
            text: 'Transport tx'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['node1', 'node2', 'node3', 'node4', 'node5']
        //   data:node_list
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
        //   data:xaxis_date
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            smooth: true,
            name: 'node1',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
            smooth: true,
            name: 'node2',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
            smooth: true,
            name: 'node3',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
            smooth: true,
            name: 'node4',
            type: 'line',
            stack: 'Total',
            data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
            smooth: true,
            name: 'node5',
            type: 'line',
            stack: 'Total',
            data: [820, 932, 901, 934, 1290, 1330, 1320]
            }
        ]

        })
    },
    selectAll() {
      this.selectedArr = []
      if (this.checked) {
        this.options.map((item) => {
          this.selectedArr.push(item.value)
        })
      } else {
        this.selectedArr = []
      }
    },
    changeSelect(val) {
      if (val.length === this.options.length) {
        this.checked = true
      } else {
        this.checked = false
      }
    },
      onSubmit(){

      }
    },
  //调用
  mounted() {
      this.$nextTick(function() {
          this.drawLine('Transport_tx')
      })
  }
  
  }
</script>
