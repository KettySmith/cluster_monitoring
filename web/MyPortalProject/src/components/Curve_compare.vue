<template>
  <div class="chart">
    <div style="margin-top: 80px;margin-bottom: 50px;">
      <h1>相似度对比分析</h1>
    </div>
    <div class="panelgroup" style="width:100%;height:200px;font-size:30px;margin-top: 30px;">
      筛选范围
      <el-select v-model="value" clearable placeholder="请选择" style="margin-left: 5%;">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-button type="primary" @click="compare_query">查询</el-button>

    </div>

    <div v-if="if_top5">


      <!-- 循环元素 -->
      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_1" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[0]}}</h4>
              <h4>simivalue: {{similar[0]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_2" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[1]}}</h4>
              <h4>simivalue: {{similar[1]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_3" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[2]}}</h4>
              <h4>simivalue: {{similar[2]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_4" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[3]}}</h4>
              <h4>simivalue: {{similar[3]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_5" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[4]}}</h4>
              <h4>simivalue: {{similar[4]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>
      

     
      
    </div>
    <div v-else>
    
    <div v-if="if_top10">
      <!-- 循环元素 -->
      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_1" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[0]}}</h4>
              <h4>simivalue: {{similar[0]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_2" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[1]}}</h4>
              <h4>simivalue: {{similar[1]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_3" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[2]}}</h4>
              <h4>simivalue: {{similar[2]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_4" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[3]}}</h4>
              <h4>simivalue: {{similar[3]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_5" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[4]}}</h4>
              <h4>simivalue: {{similar[4]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <!-- 循环元素 -->
      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_6" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[5]}}</h4>
              <h4>simivalue: {{similar[5]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_7" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[6]}}</h4>
              <h4>simivalue: {{similar[6]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_8" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[7]}}</h4>
              <h4>simivalue: {{similar[7]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_9" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[8]}}</h4>
              <h4>simivalue: {{similar[8]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>

      <div class="chart" style="display: flex;">
        <div style="width:80%;">
          <div id="top5_10" style="width: 100%;height: 520px;margin-top: 50px;margin-bottom: 50px;"></div>
        </div>
        <div style="width:20%;">
          <el-card class="box-card" style="margin-top:20%;margin-left:10%;width:80%">
            <div slot="header" class="clearfix">
              <h3>异常曲线信息</h3>
            </div>
            <div style="text-align: left;">
              <h4>相似曲线名称: {{curvelist[9]}}</h4>
              <h4>simivalue: {{similar[9]}}</h4>
              <h4>异常曲线start: {{ ablist_start }}</h4>
              <h4>异常曲线end: {{ ablist_end }}</h4>
              <h4>相似曲线start: {{ slist_start }}</h4>
              <h4>相似曲线end: {{ slist_end }}</h4>
            </div>
          </el-card>
        </div>
      </div>


    </div>
    <div v-else></div>

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

        value: '5',
        label: 'top-5'
      }, {
        value: '10',
        label: 'top-10'
      }],
      value: '',
      com_length:'',
      curvelist:[],
      similar:[],
      ablist_start:'2023/4/23 15:20',
      ablist_end:'2023/4/23 17:20',
      slist_start:'2023/4/23 15:16',
      slist_end:'2023/4/23 17:24',
      // slist:[{
      //   start:111,
      //   end:222
      //   }
      // ],

      if_top5:false,
      if_top10:false,
      ab_name:'',
      ab_x_data_list:'',
      ab_y_data_list:'',

      top5_1:'',
      top5_2:'',
      top5_3:'',
      top5_4:'',
      top5_5:'',
      top5_6:'',
      top5_7:'',
      top5_8:'',
      top5_9:'',
      top5_10:''
     

    }
  },
  methods: {
    compare_query() {
      this.com_length=this.value
      if(this.com_length==5){
        this.if_top5=true
        this.if_top10=false
      }
      else if(this.com_length==10){
        this.if_top10=true
        this.if_top5=false

      }
      else{
        this.if_top10=false
        this.if_top5=false

        this.$message({
            message: "选择不能为空！",
            type: 'warning'
          })
          return
      }
      console.log(this.com_length)
      const params = new URLSearchParams();
      params.append("rank", this.com_length)
      params.append("ab_node", 'abnormal0')
      params.append("start_time", this.ablist_start)
      params.append("end_time", this.ablist_end)
      
      axios.post('http://127.0.0.1:8090/search/similarity_search',
      params,
      {
        headers: { 'content-type': 'application/x-www-form-urlencoded' }
      })
        .then((res)=>{
          console.log(res.data)
          console.log(res.data[0])
          console.log(Object.keys(res.data))

          //图标信息
          this.curvelist=[]
          this.similar=[]
          for(var i=0;i<Object.keys(res.data).length-1;i++){
            this.curvelist.push(res.data[i].node_name)
            this.similar.push(res.data[i].simi_value)
          }

          //绘图数据

          if(this.com_length==5){
            this.ab_name=res.data[5].node_name
            this.ab_x_data_list=res.data[5].x_data_list
            this.ab_y_data_list=res.data[5].y_data_list

            this.ab_y_data_list[0]=''
            this.ab_y_data_list[1]=''
            var ylength=this.ab_y_data_list.length
            this.ab_y_data_list[ylength-2]=''
            this.ab_y_data_list[ylength-1]=''
            


            this.drawline('top5_1',this.top5_1,res.data[0].node_name,res.data[0].y_data_list)
            this.drawline('top5_2',this.top5_2,res.data[1].node_name,res.data[1].y_data_list)
            this.drawline('top5_3',this.top5_3,res.data[2].node_name,res.data[2].y_data_list)
            this.drawline('top5_4',this.top5_4,res.data[3].node_name,res.data[3].y_data_list)
            this.drawline('top5_5',this.top5_5,res.data[4].node_name,res.data[4].y_data_list)
          }
          else{
            this.ab_name=res.data[10].node_name
            this.ab_x_data_list=res.data[10].x_data_list
            this.ab_y_data_list=res.data[10].y_data_list

            this.ab_y_data_list[0]=''
            this.ab_y_data_list[1]=''
            var ylength=this.ab_y_data_list.length
            this.ab_y_data_list[ylength-2]=''
            this.ab_y_data_list[ylength-1]=''
            


            this.drawline('top5_1',this.top5_1,res.data[0].node_name,res.data[0].y_data_list)
            this.drawline('top5_2',this.top5_2,res.data[1].node_name,res.data[1].y_data_list)
            this.drawline('top5_3',this.top5_3,res.data[2].node_name,res.data[2].y_data_list)
            this.drawline('top5_4',this.top5_4,res.data[3].node_name,res.data[3].y_data_list)
            this.drawline('top5_5',this.top5_5,res.data[4].node_name,res.data[4].y_data_list)
            this.drawline('top5_6',this.top5_6,res.data[5].node_name,res.data[5].y_data_list)
            this.drawline('top5_7',this.top5_7,res.data[6].node_name,res.data[6].y_data_list)
            this.drawline('top5_8',this.top5_8,res.data[7].node_name,res.data[7].y_data_list)
            this.drawline('top5_9',this.top5_9,res.data[8].node_name,res.data[8].y_data_list)
            this.drawline('top5_10',this.top5_10,res.data[9].node_name,res.data[9].y_data_list)

          }
          
    
        })


    },
    drawline(id,curvename,si_name,si_y_data_list){
      let myChart = echarts.getInstanceByDom(document.getElementById(id))
                  if(myChart==null){
                    curvename= echarts.init(document.getElementById(id))
                  }
                  else{
                    curvename.clear()
                  curvename = echarts.init(document.getElementById(id))
                  }
                  var option = {
                    // title: {
                    //   text: 'Abnormal data'
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
                    xAxis:{
                      data:[]
                    },
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
                  
                  var it1=new item
                  it1.name=this.ab_name
                  legends.push(it1.name)
                  it1.data=this.ab_y_data_list
                  Series.push(it1)

                  var it2=new item
                  it2.name=si_name
                  legends.push(it2.name)
                  it2.data=si_y_data_list
                  Series.push(it2)

                
                  option.xAxis.data = this.ab_x_data_list;
                  option.legend.data = legends;
                  option.series = Series;
                  curvename.setOption(option);

    }
  }

}


</script>

<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>