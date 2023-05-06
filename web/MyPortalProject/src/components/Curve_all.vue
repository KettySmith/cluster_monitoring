<template>
    <div class="chart">

        <div class="cluster_title" style="display: flex;height:200px;">
            <div style="width:80%;">
                <h1 style="margin-left:25%;margin-top: 4%;">监控数据</h1>
            </div>
            <div style="width:20%;text-align: center;">
                <el-button type="primary" @click="Curve_show" style="margin-top:15%">点击显示</el-button>
            </div>
        </div>
        <div style="width:100%;height:40px">
          <h2 style="float:left">Abnormal Data</h2>
        </div>
        <div style="width:100%;height: 580px;">
            <div v-if="Curve_data_show" id="Curve_all"
                style="width: 100%;height: 580px;margin-top: 50px;margin-bottom: 50px;"></div>
            <div v-else
                style="width: 100%;height: 580px;margin-top: 50px;margin-bottom: 50px;box-shadow: 0 2px 4px rgba(0, 0, 0, .4);display: flex;justify-content: center;align-items: center;">
                <h1 style="color:#9d9d9d;">暂无数据</h1>
            </div>
        </div>


    </div>
</template>
     
<script>
import * as echarts from 'echarts'
import axios from 'axios'
export default {
  // setup(){

  //   return {
  //     msg,
  //     changeMsg
  //   }
  // },

    name: '',
    data() {
        return {
            Curve_data_show: false,
            Curve_all: '',
            table_arr:[]
        }
    },
    mounted:function(){
      this.get_tables();//需要触发的函数
    },
    methods: {
       get_tables(){
          axios.get('http://127.0.0.1:8090/show/get_similarity_node'
          ).then((result) => {

              console.log(result.data)
              this.table_arr =result.data

          }
          )
      },
       Curve_show() {
        this.Curve_data_show = true
          const params = new URLSearchParams();
          for (var i = 0; i < this.table_arr.length; i++) {
              params.append("nodes_name", this.table_arr[i])
          }
          axios.post('http://127.0.0.1:8090/show/get_similarity_data',
              params, {
              headers: { 'content-type': 'application/x-www-form-urlencoded' }
          })//单指标和多指标都哟headers
              .then((res) => {
                  // console.log(res.data)
                  let myChart = echarts.getInstanceByDom(document.getElementById("Curve_all"))
                  if(myChart==null){
                  this.Curve_all = echarts.init(document.getElementById('Curve_all'))
                  }
                  else{
                  this.Curve_all.clear()
                  this.Curve_all = echarts.init(document.getElementById('Curve_all'))
                  }
                  var option = {
                    // title: {
                    //   text: 'Abnormal data'
                    // },
                    tooltip: {
                      trigger: 'axis',
                      show: true,
                      formatter: function (params) {
                        let result = `${params[0].axisValueLabel}</br>`;
                        params.forEach(function (item) {
                          result += `<div style="text-align:left">${item.marker} ${item.seriesName}:<b style="float:right">${item.value}</b></div>`;
                        });
                        return result;
                      },
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
                      data: []
                    }
                  };
                  var legends = [];// 准备存放图例数据
                  var Series = []; // 准备存放图表数据

                  for(var i = 0;i< Object.keys(res.data).length;i++){
                  var key = Object.keys(res.data)[i];
                  var it = new item;
                  it.name = key;
                  legends.push(key);
                  it.data = res.data[key].y_data_list;
                  Series.push(it);

                  } 
                  option.xAxis.data = res.data[Object.keys(res.data)[0]].x_data_list;
                  option.legend.data = legends;
                  option.series = Series;
                  this.Curve_all.setOption(option);

              }
              )










      }

    }

}
</script>
    