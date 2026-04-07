<template>
  <div class="dashboard">
    <!-- 顶部统计栏 -->
    <header class="top-stats">
      <div class="stat-item">
        <div class="stat-label">存储空间</div>
        <div class="stat-value">5.0<span class="unit">TB</span></div>
      </div>
      <div class="stat-item">
        <div class="stat-label">算力速度</div>
        <div class="stat-value">2.4<span class="unit">TFLOPS</span></div>
      </div>
      <div class="stat-item">
        <div class="stat-label">计算核心</div>
        <div class="stat-value">28,282</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">算力中心</div>
        <div class="stat-value">4<span class="unit">个</span></div>
      </div>
      <div class="stat-item">
        <div class="stat-label">接入集群</div>
        <div class="stat-value">4<span class="unit">个</span></div>
      </div>
      <div class="stat-item">
        <div class="stat-label">支撑应用</div>
        <div class="stat-value">30<span class="unit">个</span></div>
      </div>
      <div class="stat-item">
        <div class="stat-label">累计任务</div>
        <div class="stat-value">42,322</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">累计机时</div>
        <div class="stat-value">42,322</div>
      </div>
    </header>

    <!-- 主内容区 -->
    <div class="main-content">
      <!-- 第一行：集群表格 + 两个环形图 -->
      <div class="row">
        <!-- 超算互联网网络集群 -->
        <div class="panel cluster-panel">
          <div class="panel-header">
            <span class="icon">🖥️</span>
            <span>超算互联网网络集群</span>
          </div>
          <table class="cluster-table">
            <thead>
              <tr>
                <th>名称</th>
                <th>状态</th>
                <th>网络带宽</th>
                <th>存储容量</th>
                <th>节点数</th>
                <th>算速</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="cluster in clusters" :key="cluster.name">
                <td>{{ cluster.name }}</td>
                <td><span class="status online">{{ cluster.status }}</span></td>
                <td>{{ cluster.bandwidth }}</td>
                <td>{{ cluster.storage }}</td>
                <td>{{ cluster.nodes }}</td>
                <td>{{ cluster.speed }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 计算任务运行状态 -->
        <div class="panel chart-panel">
          <div class="panel-header">
            <span class="icon">📊</span>
            <span>计算任务运行状态</span>
          </div>
          <EChart :option="taskStatusOption" height="220px" />
        </div>

        <!-- 计算任务完成状态 -->
        <div class="panel chart-panel">
          <div class="panel-header">
            <span class="icon">✅</span>
            <span>计算任务完成状态</span>
          </div>
          <EChart :option="taskCompleteOption" height="220px" />
        </div>
      </div>

      <!-- 第二行：4个横向条形图 -->
      <div class="row">
        <div class="panel bar-panel">
          <div class="panel-header">
            <span class="icon">📱</span>
            <span>应用调用次数</span>
          </div>
          <div class="bar-list">
            <div v-for="app in appCalls" :key="app.name" class="bar-item">
              <div class="bar-label">{{ app.name }}</div>
              <div class="bar-wrap">
                <div class="bar-fill" :style="{ width: app.percent + '%' }"></div>
              </div>
              <div class="bar-value">{{ app.value }}</div>
            </div>
          </div>
        </div>

        <div class="panel bar-panel">
          <div class="panel-header">
            <span class="icon">⏱️</span>
            <span>应用机时用量</span>
          </div>
          <div class="bar-list">
            <div v-for="app in appTime" :key="app.name" class="bar-item">
              <div class="bar-label">{{ app.name }}</div>
              <div class="bar-wrap">
                <div class="bar-fill orange" :style="{ width: app.percent + '%' }"></div>
              </div>
              <div class="bar-value">{{ app.value }}</div>
            </div>
          </div>
        </div>

        <div class="panel bar-panel">
          <div class="panel-header">
            <span class="icon">🔧</span>
            <span>算子调用次数</span>
          </div>
          <div class="bar-list">
            <div v-for="op in operatorCalls" :key="op.name" class="bar-item">
              <div class="bar-label">{{ op.name }}</div>
              <div class="bar-wrap">
                <div class="bar-fill purple" :style="{ width: op.percent + '%' }"></div>
              </div>
              <div class="bar-value">{{ op.value }}</div>
            </div>
          </div>
        </div>

        <div class="panel bar-panel">
          <div class="panel-header">
            <span class="icon">⚡</span>
            <span>算力机时用量</span>
          </div>
          <div class="bar-list">
            <div v-for="power in powerTime" :key="power.name" class="bar-item">
              <div class="bar-label">{{ power.name }}</div>
              <div class="bar-wrap">
                <div class="bar-fill cyan" :style="{ width: power.percent + '%' }"></div>
              </div>
              <div class="bar-value">{{ power.value }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 第三行：中国地图 -->
      <div class="row">
        <div class="panel map-panel">
          <div class="panel-header">
            <span class="icon">🗺️</span>
            <span>算力中心分布情况</span>
          </div>
          <EChart :option="mapOption" height="400px" />
        </div>
      </div>

      <!-- 第四行：指标卡片 -->
      <div class="row metrics-row">
        <div class="metric-card">
          <div class="metric-title">资源感知准确率</div>
          <div class="metric-value">≥95%</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">资源调度响应时间</div>
          <div class="metric-value"><200ms</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">资源利用率提升</div>
          <div class="metric-value">20%</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">节能效果达成率</div>
          <div class="metric-value">≥90%</div>
        </div>
      </div>

      <!-- 第五行：产出验证 -->
      <div class="row">
        <div class="panel output-panel">
          <div class="panel-header">
            <span class="icon">🏆</span>
            <span>量化产出与部署验证</span>
          </div>
          <div class="output-grid">
            <div v-for="item in outputs" :key="item.name" class="output-item">
              <div class="output-name">{{ item.name }}</div>
              <div class="output-value">{{ item.value }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 第六行：底部信息 -->
      <div class="row bottom-row">
        <div class="info-card red">
          <div class="info-icon">⚡</div>
          <div class="info-content">
            <div class="info-title">算力网络互联体系</div>
            <div class="info-desc">北京 · 济南 · 广州 · 成都</div>
          </div>
        </div>

        <div class="info-card">
          <div class="info-header">
            <span class="dot"></span>
            <span>核心目标</span>
          </div>
          <div class="info-title">技术突破与能力构建</div>
          <div class="info-desc">实现跨中心资源管理、全面调度等关键技术，构建跨平台、跨地域、跨架构的超算服务能力。</div>
        </div>

        <div class="info-card">
          <div class="info-header">
            <span class="dot"></span>
            <span>覆盖范围</span>
          </div>
          <div class="info-title">四大中心与主流架构</div>
          <div class="info-desc">覆盖长沙、广州、昆山、济南四大国家超算中心，全面适配天津、曙光、华为等主流算力服务商。</div>
        </div>

        <div class="info-card">
          <div class="info-header">
            <span class="dot"></span>
            <span>未来愿景</span>
          </div>
          <div class="info-title">统一接入与高效协同</div>
          <div class="info-desc">实现算力中心资源统一接入与调度，形成可复制、可推广的技术体系与应用示范。</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import EChart from './components/EChart.vue'

// 集群数据
const clusters = ref([
  { name: '广州超算集群', status: '在线', bandwidth: '100 Mb/s', storage: '30 TB', nodes: '1000个', speed: '600 TFLOPS' },
  { name: '昆山超算集群', status: '在线', bandwidth: '100 Mb/s', storage: '20 TB', nodes: '800个', speed: '500 TFLOPS' },
  { name: '济南超算集群', status: '在线', bandwidth: '100 Mb/s', storage: '30 TB', nodes: '1000个', speed: '700 TFLOPS' },
  { name: '长沙超算集群', status: '在线', bandwidth: '100 Mb/s', storage: '30 TB', nodes: '1000个', speed: '800 TFLOPS' },
])

// 应用调用次数
const appCalls = ref([
  { name: 'VASP', value: '83522', percent: 95 },
  { name: 'LAMMPS', value: '69074', percent: 78 },
  { name: 'Materials', value: '68442', percent: 75 },
  { name: 'Abinit', value: '54395', percent: 60 },
  { name: 'Pytorch', value: '53891', percent: 58 },
])

// 应用机时用量
const appTime = ref([
  { name: 'VASP', value: '1086488', percent: 100 },
  { name: 'LAMMPS', value: '1019074', percent: 94 },
  { name: 'FFmpeg', value: '9750845', percent: 90 },
  { name: 'Gaussian', value: '8544588', percent: 79 },
  { name: 'Pytorch', value: '6884606', percent: 63 },
])

// 算子调用次数
const operatorCalls = ref([
  { name: '矩阵运算', value: '48666', percent: 88 },
  { name: '卷积运算', value: '32438', percent: 58 },
  { name: '激活函数', value: '30694', percent: 55 },
  { name: '归一化', value: '30190', percent: 54 },
  { name: '池化', value: '28506', percent: 51 },
])

// 算力机时用量
const powerTime = ref([
  { name: 'AI训练', value: '5869855', percent: 92 },
  { name: '科学计算', value: '4956778', percent: 78 },
  { name: '数据处理', value: '4758798', percent: 75 },
  { name: '图像渲染', value: '4688534', percent: 73 },
  { name: '仿真模拟', value: '3974995', percent: 62 },
])

// 产出数据
const outputs = ref([
  { name: '高水平学术论文', value: '≥5篇' },
  { name: '申请发明专利', value: '≥10件' },
  { name: '获得软件著作权', value: '≥10项' },
  { name: '超算中心部署验证', value: '4个' },
  { name: '科技报告提交', value: '4份' },
])

// 任务运行状态环形图
const taskStatusOption = {
  tooltip: {
    trigger: 'item',
    formatter: '{b}: {c} ({d}%)'
  },
  legend: {
    bottom: '5%',
    left: 'center',
    textStyle: { color: '#666' }
  },
  series: [{
    type: 'pie',
    radius: ['50%', '70%'],
    center: ['50%', '45%'],
    avoidLabelOverlap: false,
    label: { show: false },
    labelLine: { show: false },
    data: [
      { value: 328, name: '运行', itemStyle: { color: '#e53935' } },
      { value: 128, name: '排队', itemStyle: { color: '#ffcdd2' } }
    ]
  }]
}

// 任务完成状态环形图
const taskCompleteOption = {
  tooltip: {
    trigger: 'item',
    formatter: '{b}: {c} ({d}%)'
  },
  legend: {
    bottom: '5%',
    left: 'center',
    textStyle: { color: '#666' }
  },
  series: [{
    type: 'pie',
    radius: ['50%', '70%'],
    center: ['50%', '45%'],
    avoidLabelOverlap: false,
    label: { show: false },
    labelLine: { show: false },
    data: [
      { value: 42156, name: '成功', itemStyle: { color: '#4caf50' } },
      { value: 166, name: '失败', itemStyle: { color: '#ffcdd2' } }
    ]
  }]
}

// 模拟中国地图（使用散点图+轮廓）
const mapOption = {
  tooltip: {
    trigger: 'item',
    formatter: '{b}: {c}个节点'
  },
  grid: {
    left: '5%',
    right: '5%',
    top: '5%',
    bottom: '5%'
  },
  xAxis: {
    type: 'value',
    show: false,
    min: 75,
    max: 135
  },
  yAxis: {
    type: 'value',
    show: false,
    min: 18,
    max: 54
  },
  series: [
    // 中国轮廓（简化版，使用多边形）
    {
      type: 'line',
      smooth: false,
      symbol: 'none',
      lineStyle: {
        color: '#ffcdd2',
        width: 2
      },
      areaStyle: {
        color: 'rgba(229, 57, 53, 0.08)'
      },
      data: [
        [85, 48], [90, 50], [95, 52], [100, 52], [105, 52], [110, 50], [115, 48], [120, 45], [125, 42],
        [128, 40], [130, 38], [128, 35], [125, 32], [122, 30], [120, 28], [118, 26], [116, 24], [114, 22],
        [112, 20], [110, 22], [108, 24], [106, 26], [104, 28], [102, 30], [100, 32], [98, 34], [96, 36],
        [94, 38], [92, 40], [90, 42], [88, 44], [86, 46], [85, 48]
      ]
    },
    // 城市节点
    {
      type: 'effectScatter',
      symbolSize: function(val: number[]) {
        return Math.sqrt(val[2]) * 1.2
      },
      rippleEffect: {
        brushType: 'stroke',
        scale: 3
      },
      data: [
        { value: [116.4, 39.9, 1000], name: '北京', label: { show: true, formatter: '北京\n1000', position: 'top' } },
        { value: [121.5, 31.2, 800], name: '上海', label: { show: true, formatter: '上海\n800', position: 'right' } },
        { value: [113.3, 23.1, 1000], name: '广州', label: { show: true, formatter: '广州\n1000', position: 'bottom' } },
        { value: [120.6, 31.3, 1000], name: '昆山', label: { show: true, formatter: '昆山\n1000', position: 'bottom' } },
        { value: [117.0, 36.7, 1000], name: '济南', label: { show: true, formatter: '济南\n1000', position: 'top' } },
        { value: [112.9, 28.2, 1000], name: '长沙', label: { show: true, formatter: '长沙\n1000', position: 'bottom' } },
        { value: [114.1, 30.6, 600], name: '武汉', label: { show: true, formatter: '武汉\n600', position: 'left' } },
        { value: [108.9, 34.3, 400], name: '西安', label: { show: true, formatter: '西安\n400', position: 'left' } },
        { value: [106.5, 29.6, 500], name: '重庆', label: { show: true, formatter: '重庆\n500', position: 'bottom' } },
        { value: [104.1, 30.7, 450], name: '成都', label: { show: true, formatter: '成都\n450', position: 'left' } },
      ],
      itemStyle: {
        color: '#e53935',
        shadowBlur: 10,
        shadowColor: 'rgba(229, 57, 53, 0.5)'
      },
      label: {
        color: '#333',
        fontSize: 11,
        lineHeight: 16
      }
    }
  ]
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: #f5f5f5;
}

/* 顶部统计栏 */
.top-stats {
  display: flex;
  background: linear-gradient(90deg, #c62828 0%, #e53935 50%, #f44336 100%);
  padding: 20px 40px;
  gap: 40px;
  justify-content: center;
}

.stat-item {
  text-align: center;
  color: #fff;
}

.stat-label {
  font-size: 13px;
  opacity: 0.9;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
}

.stat-value .unit {
  font-size: 14px;
  font-weight: 400;
  margin-left: 4px;
  opacity: 0.9;
}

/* 主内容区 */
.main-content {
  padding: 20px;
  max-width: 1920px;
  margin: 0 auto;
}

.row {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

/* 面板 */
.panel {
  background: #fff;
  border-radius: 8px;
  border: 1px solid #e8e8e8;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.panel-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 16px 20px;
  border-bottom: 1px solid #f0f0f0;
  font-weight: 500;
  color: #333;
}

.panel-header .icon {
  font-size: 16px;
}

/* 集群面板 */
.cluster-panel {
  flex: 2;
}

.cluster-table {
  width: 100%;
  border-collapse: collapse;
}

.cluster-table th,
.cluster-table td {
  padding: 14px 16px;
  text-align: left;
  border-bottom: 1px solid #f0f0f0;
  font-size: 13px;
}

.cluster-table th {
  color: #666;
  font-weight: 500;
  background: #fafafa;
}

.cluster-table td {
  color: #333;
}

.status.online {
  color: #4caf50;
  background: rgba(76, 175, 80, 0.1);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}

/* 图表面板 */
.chart-panel {
  flex: 1;
  min-width: 280px;
}

/* 条形图面板 */
.bar-panel {
  flex: 1;
  min-width: 280px;
  padding: 0 20px 20px;
}

.bar-list {
  margin-top: 10px;
}

.bar-item {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}

.bar-label {
  width: 80px;
  font-size: 12px;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.bar-wrap {
  flex: 1;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: #e53935;
  border-radius: 4px;
  transition: width 0.3s;
}

.bar-fill.orange { background: #ff9800; }
.bar-fill.purple { background: #9c27b0; }
.bar-fill.cyan { background: #00bcd4; }

.bar-value {
  width: 70px;
  text-align: right;
  font-size: 12px;
  color: #e53935;
  font-weight: 500;
}

/* 地图面板 */
.map-panel {
  flex: 1;
  width: 100%;
}

/* 指标行 */
.metrics-row {
  display: flex;
  gap: 20px;
}

.metric-card {
  flex: 1;
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  border: 1px solid #e8e8e8;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.metric-title {
  font-size: 14px;
  color: #666;
  margin-bottom: 12px;
}

.metric-value {
  font-size: 24px;
  font-weight: 700;
  color: #e53935;
}

/* 产出面板 */
.output-panel {
  flex: 1;
  width: 100%;
  padding-bottom: 20px;
}

.output-grid {
  display: flex;
  justify-content: space-around;
  padding: 30px 20px;
}

.output-item {
  text-align: center;
}

.output-name {
  font-size: 13px;
  color: #666;
  margin-bottom: 12px;
}

.output-value {
  font-size: 20px;
  font-weight: 700;
  color: #e53935;
}

/* 底部信息 */
.bottom-row {
  display: flex;
  gap: 20px;
}

.info-card {
  flex: 1;
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #e8e8e8;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.info-card.red {
  background: linear-gradient(135deg, #e53935 0%, #c62828 100%);
  color: #fff;
  display: flex;
  align-items: center;
  gap: 16px;
}

.info-card.red .info-icon {
  width: 60px;
  height: 60px;
  background: rgba(255,255,255,0.2);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
}

.info-card.red .info-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 4px;
}

.info-card.red .info-desc {
  font-size: 13px;
  opacity: 0.9;
}

.info-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  font-size: 13px;
  color: #999;
}

.info-header .dot {
  width: 8px;
  height: 8px;
  background: #e53935;
  border-radius: 50%;
}

.info-card:not(.red) .info-title {
  font-size: 15px;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
}

.info-card:not(.red) .info-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.6;
}
</style>