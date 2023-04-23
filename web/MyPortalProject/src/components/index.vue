<template>
  <div class="cluster_container">
    <div class="panelgroup" style="width:100%;height:200px;font-size:30px;">
      集群名称
      <el-select v-model="value" clearable placeholder="请选择" style="margin-left: 5%;">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
      <el-button type="primary" @click="cluster_query">查询</el-button>
      <el-button type="success" icon="el-icon-refresh-left" @click="refresh"
        style="float:right;margin-right:100px;font-size: 30px;"></el-button>
    </div>
    <div class="cluster_title" style="display: flex;height:200px;">
      <div style="width:80%;background-color: aqua;">
        <h1 style="margin-left:25%;margin-top: 4%;">集群健康状态监测</h1>
      </div>
      <div style="width:20%;text-align: center;background-color: blue;">
        <el-button type="primary" @click="clustor_show" style="margin-top:15%" >点击显示</el-button>
      </div>
    </div>
      <Active_shards ref="Active_shards_datashow" />
      <Number_nodes ref="Number_nodes_datashow" />
      <Status ref="Status_datashow"/>
    
    
    <div class="node_title">
      <h1>节点监测--单指标</h1>
    </div>
    <Index_time ref="Index_time_node"/>
    <Query_time ref="Query_time_node"/>
    <Os_load ref="Os_load_node"/>
    <CPU_percent ref="CPU_percent_node"/>
    <Transport_rx ref="Transport_rx_node"/>
    <Transport_tx ref="Transport_tx_node"/> 
    <div class="node_title">
      <h1>节点监测--多指标</h1>
    </div>
    <Fs_available ref="Fs_available_node"/>
    <GC_runtime ref="GC_runtime_node"/>

  </div>
</template>
<script>
import axios from 'axios'
import Active_shards from './Active_shards.vue'
import Number_nodes from './Number_nodes.vue'
import Status from './Status.vue'
import Index_time from './Index_time.vue'
import Query_time from './Query_time.vue'
import Os_load from './Os_load.vue'
import CPU_percent from './CPU_percent.vue'
import Transport_rx from './Transport_rx.vue'
import Transport_tx from './Transport_tx.vue'
import Fs_available from './Fs_available.vue'
import GC_runtime from './GC_runtime.vue'

export default {
  // name: 'DashboardAdmin',
  components: {
    Active_shards,
    Number_nodes,
    Status,
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
      data_show:false,
      options: [{
        
          value: 'cc-cc408-hya',
          label: 'cc-cc408-hya'
        }, {
          value: 'cc-cc553-interestPrice',
          label: 'cc-cc553-interestPrice'
        }],
        value: '',
        truth_value:'',
        Index_time_node:'',
    }


  },
  created() {

  },

  methods: {
    refresh(){
      this.$refs.Active_shards_datashow.data_show=false;
      this.$refs.Number_nodes_datashow.data_show=false;
      this.$refs.Status_datashow.data_show=false;
      axios.post('http://127.0.0.1:8090/upload/upload_all_files')
      .then((res)=>{
        // console.log(res.data)
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
          message: "选择不能为空！",
          type: 'warning'
        });
      }
      else{
        axios.get('http://127.0.0.1:8090/show//choose_cluster/'+this.truth_value)
      .then((res)=>{
        console.log(res.data);
        console.log(res.data.elasticsearch_indices_indexing_index_time_seconds_total);

        this.$refs.Index_time_node.cluster_name=this.truth_value;
        this.$refs.Query_time_node.cluster_name=this.truth_value;
        this.$refs.Os_load_node.cluster_name=this.truth_value;
        this.$refs.CPU_percent_node.cluster_name=this.truth_value;
        this.$refs.Transport_rx_node.cluster_name=this.truth_value;
        this.$refs.Transport_tx_node.cluster_name=this.truth_value;

        this.$refs.Fs_available_node.cluster_name=this.truth_value;
        this.$refs.GC_runtime_node.cluster_name=this.truth_value;

        
        var list1 = res.data.elasticsearch_indices_indexing_index_time_seconds_total;
        for(var i = 0;i<list1.length;i++){
          var tmp={
            label:list1[i],
            value:list1[i]
          }
          this.$refs.Index_time_node.options.push(tmp);
        }
        var list2 = res.data.elasticsearch_indices_search_query_time_seconds;
        for(var i = 0;i<list2.length;i++){
          var tmp={
            label:list2[i],
            value:list2[i]
          }
          this.$refs.Query_time_node.options.push(tmp);
        }
        var list3 = res.data.elasticsearch_os_load5;
        for(var i = 0;i<list3.length;i++){
          var tmp={
            label:list3[i],
            value:list3[i]
          }
          this.$refs.Os_load_node.options.push(tmp);
        }
        var list4 = res.data.elasticsearch_process_cpu_percent;
        for(var i = 0;i<list4.length;i++){
          var tmp={
            label:list4[i],
            value:list4[i]
          }
          this.$refs.CPU_percent_node.options.push(tmp);
        }
        var list5 = res.data.elasticsearch_transport_rx_size_bytes_total;
        for(var i = 0;i<list5.length;i++){
          var tmp={
            label:list5[i],
            value:list5[i]
          }
          this.$refs.Transport_rx_node.options.push(tmp);
        }
        var list6 = res.data.elasticsearch_transport_tx_size_bytes_total;
        for(var i = 0;i<list6.length;i++){
          var tmp={
            label:list6[i],
            value:list6[i]
          }
          this.$refs.Transport_tx_node.options.push(tmp);
        }



        var mlist1 = res.data.elasticsearch_filesystem_data_available_bytes;
        for(var i = 0;i<mlist1.length;i++){
          var tmp={
            label:mlist1[i],
            value:mlist1[i]
          }
          this.$refs.Fs_available_node.options.push(tmp);
        }
        var mlist2 = res.data.elasticsearch_jvm_gc_collection_seconds_sum;
        for(var i = 0;i<mlist2.length;i++){
          var tmp={
            label:mlist2[i],
            value:mlist2[i]
          }
          this.$refs.GC_runtime_node.options.push(tmp);
        }
        
      })

      }
    },
    clustor_show(){
      this.$refs.Active_shards_datashow.data_show=true;
      this.$refs.Number_nodes_datashow.data_show=true;
      this.$refs.Status_datashow.data_show=true;
      console.log(this.$refs.Active_shards_datashow.data_show);
      this.$refs.Active_shards_datashow.drawLine('Active_shards');
    }


  }
}
</script>


