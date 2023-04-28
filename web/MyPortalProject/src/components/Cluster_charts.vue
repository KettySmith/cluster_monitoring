<template>
<div class="chart">
    <!-- zone_title -->
    <div class="cluster_title" style="display: flex;height:200px;">
        <div style="width:80%;">
            <h1 style="margin-left:25%;margin-top: 4%;">集群健康状态监测</h1>
        </div>
        <div style="width:20%;text-align: center;">
            <el-button type="primary" @click="cluster_show" style="margin-top:15%" >点击显示</el-button>
        </div>
    </div>



    <div style="width:100%;height:40px">
      <h2 style="float:left">Active Shards</h2>
    </div>
    <div style="width:100%;height: 520px;">
        <div v-if="Active_shards_data_show" id="Active_shards" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
      <div v-else style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;box-shadow: 0 2px 4px rgba(0, 0, 0, .4);display: flex;justify-content: center;align-items: center;">
          <h1 style="color:#9d9d9d;">暂无数据</h1>
      </div>
    </div>
      

    <div style="width:100%;height:40px">
      <h2 style="float:left">Number Nodes</h2>
    </div>
    <div style="width:100%;height: 520px;">
        <div v-if="Number_nodes_data_show" id="Number_nodes" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
      <div v-else style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;box-shadow: 0 2px 4px rgba(0, 0, 0, .4);display: flex;justify-content: center;align-items: center;">
          <h1 style="color:#9d9d9d;">暂无数据</h1>
      </div>
    </div>

    

    <div style="width:100%;height:40px">
      <h2 style="float:left">Status</h2>
    </div>

    <div style="width:100%;height: 520px;">
        <div v-if="Status_data_show" id="Status" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px"></div>
      <div v-else style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;box-shadow: 0 2px 4px rgba(0, 0, 0, .4);display: flex;justify-content: center;align-items: center;">
          <h1 style="color:#9d9d9d;">暂无数据</h1>
      </div>
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

        cluster_name:'',
        //集群图
        Active_shards_data_show:false,
        Active_shards:'',
        Number_nodes_data_show:false,
        Number_nodes:'',
        Status_data_show:false,
        Status:''
    }
  },
  methods: {
    cluster_show(){//集群数据查询 
    
    //注意！true设置一定要在get/post请求之前设置！否则invalid dom 报错
    this.Active_shards_data_show=true;
    this.Number_nodes_data_show=true;
    this.Status_data_show=true;

    axios.get('http://127.0.0.1:8090/show/get_cluster_data/'+this.cluster_name
    ).then((res)=>{
      
    console.log(res.data)

     //集群表格初始化Status
     let myChart1 = echarts.getInstanceByDom(document.getElementById("Active_shards"));
     let myChart2 = echarts.getInstanceByDom(document.getElementById("Number_nodes"));
     let myChart3 = echarts.getInstanceByDom(document.getElementById("Status"));
    if(myChart1==null){
    this.Active_shards = echarts.init(document.getElementById('Active_shards'))
    }
    else{
    this.Active_shards.clear()
    this.Active_shards = echarts.init(document.getElementById('Active_shards'))
    }
    if(myChart2==null){
    this.Number_nodes = echarts.init(document.getElementById('Number_nodes'))
    }
    else{
    this.Number_nodes.clear()
    this.Number_nodes = echarts.init(document.getElementById('Number_nodes'))
    }
    if(myChart3==null){
    this.Status = echarts.init(document.getElementById('Status'))
    }
    else{
    this.Status.clear()
    this.Status = echarts.init(document.getElementById('Status'))
    }
   
    var option={
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
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            type: 'line',
          //   data: yaxis_value,
            data:[],
            smooth: true
            }
          ]
      }

      var option1=option
      var option2=option
      var option3=option

      option1.xAxis.data=res.data[Object.keys(res.data)[0]].x_data_list
      option1.series[0].data=res.data[Object.keys(res.data)[0]].y_data_list
      this.Active_shards.setOption(option1)
      option2.xAxis.data=res.data[Object.keys(res.data)[1]].x_data_list
      option2.series[0].data=res.data[Object.keys(res.data)[1]].y_data_list
      this.Number_nodes.setOption(option2)
      option3.xAxis.data=res.data[Object.keys(res.data)[2]].x_data_list
      option3.series[0].data=res.data[Object.keys(res.data)[2]].y_data_list
      this.Status.setOption(option3)


    }
    )


  }
  

  }
}

</script>