<template>
  <div class="chart" style="display: flex;">
    <div style="width:80%;">
      <div v-if="data_show" id="Query_time" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
      <div v-else style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;box-shadow: 0 2px 4px rgba(0, 0, 0, .4);display: flex;justify-content: center;align-items: center;">
            <h1 style="color:#9d9d9d;">暂无数据</h1>
        </div>
    </div>
    <div style="width:20%;text-align: center;">
      <el-select v-model="value" multiple collapse-tags filterable style="margin-top:50%;" placeholder="请选择"
        @change='changeSelect'>
        <el-checkbox v-model="checked" @change='selectAll' style="text-align: right;width: 90%;">全选</el-checkbox>
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-button type="primary" @click="node_query" style="margin-top:50%">查询</el-button>
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
      data_show:false,
      Query_time: '',
      node_list: [],
      xaxis_date: '',
      checked: false,
      selectedArr: [],
      options: [],
      value: [],
      cluster_name: ''
    }
  },
  methods: {
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
    node_query() {
      this.data_show=!this.data_show;
      console.log(this.options)
      console.log("here:", this.value)
      const params = new URLSearchParams();
      for (var i = 0; i < this.value.length; i++) {
        params.append("nodes_name", this.value[i])
      }
      axios.post('http://127.0.0.1:8090/show/get_node_single_data/' + this.cluster_name + '/elasticsearch_indices_search_query_time_seconds',
        params, {
        headers: { 'content-type': 'application/x-www-form-urlencoded' }
      })//单指标和多指标都哟headers
        .then((res) => {
          //获取到数据
          this.Query_time = echarts.init(document.getElementById('Query_time'))
          var option = {
            // title: {
            //   text: 'Query Time'
            // },
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
            legend: {
              data: []
            },
            xAxis:{data:[]},
            yAxis: {},
            series: []
          };
          var item = function () {
            return {
              smooth: true,
              name: '',
              type: 'line',
              stack: 'Total',
              data: []
            }
          };
          var legends = [];// 准备存放图例数据
          var Series = []; // 准备存放图表数据
        console.log(res.data)

          for(var i = 0;i< Object.keys(res.data).length;i++){
            var key = Object.keys(res.data)[i];
            console.log(key)
            var it = new item;
            it.name = key;
            legends.push(key);
            console.log(res.data[key])
            it.data = res.data[key].y_data_list;
            Series.push(it);

          }
          option.xAxis.data = res.data[Object.keys(res.data)[0]].x_data_list;
          option.legend.data = legends;
          option.series = Series;
          this.Query_time.setOption(option);

        })

    }
  },
  //调用
  mounted() {
    
  }

}
</script>
