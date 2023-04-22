在自己的图表业务页面中按需引入chart-tm中的组件，即可使用，组件中有默认数据，API返回数据参考默认数据格式处理。

```html
<el-col :xs="24" :sm="16" :md="16" :lg="16" :xl="16">
  <el-card shadow="always">
    <div slot="header" class="clearfix">
      <span>销售趋势</span>
      <span class="card-div-desc">{{ lineCardTitle }}</span>
      <el-radio-group style="float: right; padding: 3px 0" v-model="lineDataType"
                      size="mini" @change="handleLineChange">
        <el-radio-button label="order">订单数</el-radio-button>
        <el-radio-button label="sale">销售额</el-radio-button>
      </el-radio-group>
    </div>
    <div>
      <LineHeapChart
          height="600px"
          :xAxisData="lineXAxisData"
          :seriesData="lineSeriesData"
      />
    </div>
  </el-card>
</el-col>

import LineHeapChart from '@/views/dashboard/LineHeapChart'
import PieFlatChart from '@/views/dashboard/PieFlatChart'

export default {
  name: 'index',
  components: {
    LineHeapChart,
    PieFlatChart
  },
}
```

