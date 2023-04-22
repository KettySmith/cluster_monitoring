<template>
  <div class="clustor_container">
    <div class="panelgroup" style="width:100%;height:200px;font-size:30px;">
      集群名称
      <el-select v-model="select"  placeholder="请选择集群" style="margin-left:20px">
        <el-option label="集群1" value="1"></el-option>
        <el-option label="集群2" value="2"></el-option>
      </el-select>
      <el-button type="primary" @click="onSubmit">查询</el-button>
      <el-button type="success" icon="el-icon-refresh-left" style="float:right;margin-right:100px;font-size: 30px;"></el-button>
    </div>  
    <div class="clustor_title">
      <h1>集群健康状态监测</h1>
    </div>  
    <Active_shards/>
    <Number_nodes/>
    <Status/>
    <div class="node_title">
      <h1>节点监测--单指标</h1>
    </div> 
    <Index_time/>
    <Query_time/>
    <Os_load/>
    <CPU_percent/>
    <Transport_rx/>
    <Transport_tx/>
    <div class="node_title">
      <h1>节点监测--多指标</h1>
    </div>
    <Fs_available/>
    <GC_runtime/>
    
  </div>
</template>
<script>
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
  name: 'DashboardAdmin',
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
      lineChartData: lineData,
      clustor1:"",
      clustor2:""
      }

    
  },
  created() {
    // console.log('初始化数据')
    this.handleSetLineChartData('newVisitis')

    // console.log(this.lineChartData)
  },
  
  methods: {
    handleSetLineChartData(type) {
      getLinedata(type).then(response => {
        this.lineChartData = response.data
        // console.log(this.lineChartData)
      })
    },
    onSubmit(){
      //
    }
    

  }
}
</script>


