<template>






  <div class="cluster_container">
  
   
      <div class="panelgroup" style="width:100%;height:200px;font-size:30px;margin-top: 20px;">
        <span style="margin-left: 10%;">集群名称</span>
        <el-select v-model="value" clearable placeholder="请选择" style="margin-left:5%;">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <el-button type="primary" @click="cluster_query">查询</el-button>
        <el-button type="success" style="float:right;margin-top:10px;margin-right:10%;width:120px" @click="refresh" :loading="loadingbut" >
           {{loading_text}}
        </el-button>
      </div>
  
  <!-- 集群 -->
  
      <Cluster_charts ref="Cluster_charts_data_show"/>
  
  <!-- 节点 -->
      
      <div class="node_title">
        <h1>节点监测--单指标</h1>
      </div>
      <div style="width:100%;height:40px;">
          <h2 style="text-align: left">Index Time</h2>
      </div>
      <div>
        <Index_time ref="Index_time_node"/>
  
  
      </div>
      <div style="width:100%;height:40px">
        <h2 style="text-align: left">Query Time</h2>
      </div>
      <Query_time ref="Query_time_node"/>
      <div style="width:100%;height:40px">
        <h2 style="text-align: left">OS Load</h2>
      </div>
      <Os_load ref="Os_load_node"/>
      <div style="width:100%;height:40px">
        <h2 style="text-align: left">CPU Percent</h2>
      </div>
      <CPU_percent ref="CPU_percent_node"/>
      <div style="width:100%;height:40px">
        <h2 style="text-align: left">Transport_rx</h2>
      </div>
      <Transport_rx ref="Transport_rx_node"/>
      <div style="width:100%;height:40px">
        <h2 style="text-align:left">Transport_tx</h2>
      </div>
      <Transport_tx ref="Transport_tx_node"/> 
      <div class="node_title">
        <h1>节点监测--多指标</h1>
      </div>
      <div style="width:100%;height:40px">
        <h2 style="text-align:left">FS Available</h2>
      </div>
      <Fs_available ref="Fs_available_node"/>
      <div style="width:100%;height:40px">
        <h2 style="text-align:left">GC Runtime</h2>
      </div>
      <GC_runtime ref="GC_runtime_node"/>
  
  
  
    </div>
  </template>
  <script>
  import * as echarts from 'echarts'
  import axios from 'axios'
  
  import Cluster_charts from './Cluster_charts.vue'
  import Index_time from './Index_time.vue'
  import Query_time from './Query_time.vue'
  import Os_load from './Os_load.vue'
  import CPU_percent from './CPU_percent.vue'
  import Transport_rx from './Transport_rx.vue'
  import Transport_tx from './Transport_tx.vue'
  import Fs_available from './Fs_available.vue'
  import GC_runtime from './GC_runtime.vue'
  
  export default {
    components: {
      Cluster_charts,
      Index_time,
      Query_time,
      Os_load,
      CPU_percent,
      Transport_rx,
      Transport_tx,
      Fs_available,
      GC_runtime
    },
    data() {
      return {
        options: [{
          
            value: 'cc-cc408-hya',
            label: 'cc-cc408-hya'
          }, {
            value: 'cc-cc553-interestPrice',
            label: 'cc-cc553-interestPrice'
          }],
          value: '',
          truth_value:'',
          loadingbut:false,
          loading_text:'刷新'
  
      }
    },
    created() {
  
    },
  
    methods: {
      refresh(){
        this.loadingbut=true
        this.loading_text='加载中...'
        
        axios.post('http://127.0.0.1:8090/upload/upload_all_files')
        .then((res)=>{
          // console.log(res.data)
          this.loadingbut=false
          this.loading_text='刷新'
          this.$message({
            message: res.data,
            type: 'success'
          });
  
        })
      },
      cluster_query() {
        console.log(this.value);
        this.truth_value=this.value;
  
        if(this.truth_value==''){
          this.$message({
            message: "请选择集群名称！",
            type: 'warning'
          });
        }
        else{
          axios.get('http://127.0.0.1:8090/show/choose_cluster/'+this.truth_value)
        .then((res)=>{
          console.log(res.data)
          console.log("metric")
  
         //集群
         this.$refs.Cluster_charts_data_show.cluster_name=this.truth_value;
  
          //节点
          this.$refs.Index_time_node.cluster_name=this.truth_value;
          this.$refs.Query_time_node.cluster_name=this.truth_value;
          this.$refs.Os_load_node.cluster_name=this.truth_value;
          this.$refs.CPU_percent_node.cluster_name=this.truth_value;
          this.$refs.Transport_rx_node.cluster_name=this.truth_value;
          this.$refs.Transport_tx_node.cluster_name=this.truth_value;
  
          this.$refs.Fs_available_node.cluster_name=this.truth_value;
          this.$refs.GC_runtime_node.cluster_name=this.truth_value;
  
          
          //单节点
          this.$refs.Index_time_node.options=[]
          var list1 = res.data.elasticsearch_indices_indexing_index_time_seconds_total;
          for(var i = 0;i<list1.length;i++){
            var tmp={
              label:list1[i],
              value:list1[i]
            }
            this.$refs.Index_time_node.options.push(tmp);
            if(i==1){
              console.log("tmp")
              console.log(tmp)
            }
          }
          this.$refs.Query_time_node.options=[]
          var list2 = res.data.elasticsearch_indices_search_query_time_seconds;
          for(var i = 0;i<list2.length;i++){
            var tmp={
              label:list2[i],
              value:list2[i]
            }
            this.$refs.Query_time_node.options.push(tmp);
          }
          this.$refs.Os_load_node.options=[]
          var list3 = res.data.elasticsearch_os_load5;
          for(var i = 0;i<list3.length;i++){
            var tmp={
              label:list3[i],
              value:list3[i]
            }
            this.$refs.Os_load_node.options.push(tmp);
          }
          this.$refs.CPU_percent_node.options=[]
          var list4 = res.data.elasticsearch_process_cpu_percent;
          for(var i = 0;i<list4.length;i++){
            var tmp={
              label:list4[i],
              value:list4[i]
            }
            this.$refs.CPU_percent_node.options.push(tmp);
          }
          this.$refs.Transport_rx_node.options=[]
          var list5 = res.data.elasticsearch_transport_rx_size_bytes_total;
          for(var i = 0;i<list5.length;i++){
            var tmp={
              label:list5[i],
              value:list5[i]
            }
            this.$refs.Transport_rx_node.options.push(tmp);
          }
          this.$refs.Transport_tx_node.options=[]
          var list6 = res.data.elasticsearch_transport_tx_size_bytes_total;
          for(var i = 0;i<list6.length;i++){
            var tmp={
              label:list6[i],
              value:list6[i]
            }
            this.$refs.Transport_tx_node.options.push(tmp);
          }
  
  
          //多节点
          this.$refs.Fs_available_node.options=[]
          var mlist1 = res.data.elasticsearch_filesystem_data_available_bytes;
          for(var i = 0;i<mlist1.length;i++){
            var tmp={
              label:mlist1[i],
              value:mlist1[i]
            }
            this.$refs.Fs_available_node.options.push(tmp)
          }
          this.$refs.GC_runtime_node.options=[]
          var mlist2 = res.data.elasticsearch_jvm_gc_collection_seconds_sum
          for(var i = 0;i<mlist2.length;i++){
            var tmp={
              label:mlist2[i],
              value:mlist2[i]
            }
            this.$refs.GC_runtime_node.options.push(tmp)
          }
          
        })
  
        }
      },
  
      handleSelect(key, keyPath) {
          console.log(key, keyPath);
      }
  
  
    }
  }
  </script>
  
  
  