<template>
  <div class="app-layout">
    <!-- 顶部导航条 -->
    <header class="top-navbar">
      <div class="navbar-left">
        <div class="logo">
          <span class="logo-icon">⚡</span>
          <span class="logo-text">超算互联网</span>
        </div>
        <nav class="top-menu">
          <a href="#" class="menu-item active">首页</a>
          <a href="#" class="menu-item">资源管理</a>
          <a href="#" class="menu-item">任务调度</a>
          <a href="#" class="menu-item">应用市场</a>
          <a href="#" class="menu-item">监控告警</a>
        </nav>
      </div>
      <div class="navbar-right">
        <div class="search-box">
          <input type="text" placeholder="搜索..." />
          <span class="search-icon">🔍</span>
        </div>
        <div class="user-info">
          <span class="notification">🔔</span>
          <span class="username">管理员</span>
          <span class="avatar">👤</span>
        </div>
      </div>
    </header>

    <!-- 主体区域 -->
    <div class="main-container">
      <!-- 左侧菜单栏 -->
      <aside class="sidebar">
        <div class="sidebar-section">
          <div class="section-title">概览</div>
          <ul class="sidebar-menu">
            <li class="menu-item active">
              <span class="icon">📊</span>
              <span>数据大屏</span>
            </li>
            <li class="menu-item">
              <span class="icon">📈</span>
              <span>趋势分析</span>
            </li>
            <li class="menu-item">
              <span class="icon">🎯</span>
              <span>运营指标</span>
            </li>
          </ul>
        </div>

        <div class="sidebar-section">
          <div class="section-title">资源管理</div>
          <ul class="sidebar-menu">
            <li class="menu-item">
              <span class="icon">🖥️</span>
              <span>算力集群</span>
            </li>
            <li class="menu-item">
              <span class="icon">💾</span>
              <span>存储资源</span>
            </li>
            <li class="menu-item">
              <span class="icon">🌐</span>
              <span>网络拓扑</span>
            </li>
            <li class="menu-item">
              <span class="icon">📋</span>
              <span>资源调度</span>
            </li>
          </ul>
        </div>

        <div class="sidebar-section">
          <div class="section-title">任务管理</div>
          <ul class="sidebar-menu">
            <li class="menu-item">
              <span class="icon">▶️</span>
              <span>运行中任务</span>
            </li>
            <li class="menu-item">
              <span class="icon">⏸️</span>
              <span>排队任务</span>
            </li>
            <li class="menu-item">
              <span class="icon">✅</span>
              <span>历史任务</span>
            </li>
          </ul>
        </div>
      </aside>

      <!-- 主内容区 -->
      <main class="content-area">
        <!-- 统计卡片区 -->
        <div class="stats-cards-row">
          <div class="stat-card">
            <div class="card-icon storage">💾</div>
            <div class="card-content">
              <div class="card-label">存储空间</div>
              <div class="card-value">5.0<span class="unit">TB</span></div>
              <div class="card-trend up">↑ 12.5%</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon speed">⚡</div>
            <div class="card-content">
              <div class="card-label">算力速度</div>
              <div class="card-value">2.4<span class="unit">TFLOPS</span></div>
              <div class="card-trend up">↑ 8.3%</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon core">🔲</div>
            <div class="card-content">
              <div class="card-label">计算核心</div>
              <div class="card-value">28,282</div>
              <div class="card-trend up">↑ 5.2%</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon center">🏢</div>
            <div class="card-content">
              <div class="card-label">算力中心</div>
              <div class="card-value">4<span class="unit">个</span></div>
              <div class="card-trend stable">→ 持平</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon cluster">🖥️</div>
            <div class="card-content">
              <div class="card-label">接入集群</div>
              <div class="card-value">4<span class="unit">个</span></div>
              <div class="card-trend stable">→ 持平</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon app">📱</div>
            <div class="card-content">
              <div class="card-label">支撑应用</div>
              <div class="card-value">30<span class="unit">个</span></div>
              <div class="card-trend up">↑ 15.4%</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon task">📋</div>
            <div class="card-content">
              <div class="card-label">累计任务</div>
              <div class="card-value">42,322</div>
              <div class="card-trend up">↑ 23.1%</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="card-icon time">⏱️</div>
            <div class="card-content">
              <div class="card-label">累计机时</div>
              <div class="card-value">42,322</div>
              <div class="card-trend up">↑ 18.7%</div>
            </div>
          </div>
        </div>

        <!-- 第一行：集群表格 + 两个环形图 -->
        <div class="row">
          <div class="panel cluster-panel">
            <div class="panel-header">🖥️ 超算互联网网络集群</div>
            <table class="cluster-table">
              <thead>
                <tr><th>名称</th><th>状态</th><th>网络带宽</th><th>存储容量</th><th>节点数</th><th>算速</th></tr>
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

          <div class="panel chart-panel">
            <div class="panel-header">📊 计算任务运行状态</div>
            <EChart :option="taskStatusOption" height="220px" />
          </div>

          <div class="panel chart-panel">
            <div class="panel-header">✅ 计算任务完成状态</div>
            <EChart :option="taskCompleteOption" height="220px" />
          </div>
        </div>

        <!-- 第二行：4个横向条形图 -->
        <div class="row">
          <div class="panel bar-panel">
            <div class="panel-header">📱 应用调用次数</div>
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
            <div class="panel-header">⏱️ 应用机时用量</div>
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
            <div class="panel-header">🔧 算子调用次数</div>
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
            <div class="panel-header">⚡ 算力机时用量</div>
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
            <div class="panel-header">🗺️ 算力中心分布情况</div>
            <EChart :option="mapOption" height="450px" />
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
            <div class="panel-header">🏆 量化产出与部署验证</div>
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
      </main>
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
  tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
  legend: { bottom: '5%', left: 'center', textStyle: { color: '#666' } },
  series: [{
    type: 'pie', radius: ['50%', '70%'], center: ['50%', '45%'],
    avoidLabelOverlap: false, label: { show: false }, labelLine: { show: false },
    data: [
      { value: 328, name: '运行', itemStyle: { color: '#e53935' } },
      { value: 128, name: '排队', itemStyle: { color: '#ffcdd2' } }
    ]
  }]
}

// 任务完成状态环形图
const taskCompleteOption = {
  tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
  legend: { bottom: '5%', left: 'center', textStyle: { color: '#666' } },
  series: [{
    type: 'pie', radius: ['50%', '70%'], center: ['50%', '45%'],
    avoidLabelOverlap: false, label: { show: false }, labelLine: { show: false },
    data: [
      { value: 42156, name: '成功', itemStyle: { color: '#4caf50' } },
      { value: 166, name: '失败', itemStyle: { color: '#ffcdd2' } }
    ]
  }]
}

// 中国地图配置 - 使用真实geoJSON地图
const mapOption = {
  backgroundColor: 'transparent',
  tooltip: {
    trigger: 'item',
    backgroundColor: 'rgba(255,255,255,0.95)',
    borderColor: '#e8e8e8',
    borderWidth: 1,
    textStyle: { color: '#333' },
    formatter: function(params: any) {
      if (params.seriesType === 'effectScatter' || params.seriesType === 'scatter') {
        return `<div style="padding:8px;">
          <div style="font-weight:600;margin-bottom:4px;">${params.name}</div>
          <div>节点数: <span style="color:#e53935;font-weight:600;">${params.data.value[2]}</span></div>
          <div style="font-size:12px;color:#999;margin-top:4px;">点击查看详情</div>
        </div>`
      }
      return params.name
    }
  },
  // 地理坐标系 - 真实中国地图
  geo: {
    map: 'china',
    roam: true,
    zoom: 1.2,
    center: [105, 36],
    label: {
      show: true,
      color: '#666',
      fontSize: 10
    },
    itemStyle: {
      areaColor: '#f5f5f5',
      borderColor: '#ddd',
      borderWidth: 1
    },
    emphasis: {
      itemStyle: {
        areaColor: '#e8e8e8'
      },
      label: {
        color: '#333'
      }
    },
    // 中国地图各省份数据
    regions: [
      { name: '北京', itemStyle: { areaColor: '#ffebee' } },
      { name: '上海', itemStyle: { areaColor: '#ffebee' } },
      { name: '广东', itemStyle: { areaColor: '#ffebee' } },
      { name: '江苏', itemStyle: { areaColor: '#ffebee' } },
      { name: '山东', itemStyle: { areaColor: '#ffebee' } },
      { name: '湖南', itemStyle: { areaColor: '#ffebee' } }
    ]
  },
  series: [
    // 主要算力中心（带涟漪效果）
    {
      type: 'effectScatter',
      coordinateSystem: 'geo',
      symbolSize: function(val: number[]) {
        return Math.sqrt(val[2]) * 2.5
      },
      showEffectOn: 'render',
      rippleEffect: {
        brushType: 'stroke',
        scale: 3,
        period: 4
      },
      itemStyle: {
        color: {
          type: 'radial',
          x: 0.5, y: 0.5, r: 0.5,
          colorStops: [
            { offset: 0, color: '#ff8a80' },
            { offset: 0.5, color: '#e53935' },
            { offset: 1, color: '#c62828' }
          ]
        },
        shadowBlur: 20,
        shadowColor: 'rgba(229, 57, 53, 0.4)'
      },
      label: {
        show: true,
        position: 'top',
        formatter: '{b}',
        color: '#333',
        fontSize: 12,
        fontWeight: 500,
        backgroundColor: 'rgba(255,255,255,0.9)',
        padding: [4, 8],
        borderRadius: 4,
        shadowBlur: 4,
        shadowColor: 'rgba(0,0,0,0.1)'
      },
      data: [
        { name: '北京', value: [116.4, 39.9, 1000] },
        { name: '济南', value: [117.0, 36.7, 1000] },
        { name: '上海', value: [121.5, 31.2, 800] },
        { name: '长沙', value: [112.9, 28.2, 1000] },
        { name: '广州', value: [113.3, 23.1, 1000] },
        { name: '成都', value: [104.1, 30.7, 600] },
        { name: '西安', value: [108.9, 34.3, 500] }
      ]
    },
    // 次要算力节点
    {
      type: 'scatter',
      coordinateSystem: 'geo',
      symbolSize: function(val: number[]) {
        return Math.sqrt(val[2]) * 2
      },
      itemStyle: {
        color: '#ff8a80',
        opacity: 0.9
      },
      label: {
        show: true,
        position: 'bottom',
        formatter: '{b}',
        color: '#666',
        fontSize: 10
      },
      data: [
        { name: '沈阳', value: [123.4, 41.8, 300] },
        { name: '郑州', value: [113.6, 34.8, 400] },
        { name: '武汉', value: [114.3, 30.6, 350] },
        { name: '杭州', value: [120.2, 30.3, 450] },
        { name: '深圳', value: [114.1, 22.5, 500] },
        { name: '重庆', value: [106.5, 29.6, 400] },
        { name: '昆明', value: [102.8, 25.0, 250] },
        { name: '兰州', value: [103.8, 36.1, 200] }
      ]
    }
  ]
}
        color: '#666',
        fontSize: 11
      },
      data: [
        { name: '武汉', value: [114.1, 30.6, 600] },
        { name: '成都', value: [104.1, 30.7, 450] },
        { name: '西安', value: [108.9, 34.3, 400] },
        { name: '重庆', value: [106.5, 29.6, 500] },
        { name: '沈阳', value: [123.4, 41.8, 350] },
        { name: '郑州', value: [113.6, 34.8, 300] },
      ]
    },
    // 连接线（模拟网络）
    {
      type: 'lines',
      coordinateSystem: 'cartesian2d',
      effect: {
        show: true,
        period: 6,
        trailLength: 0.7,
        color: '#e53935',
        symbolSize: 3
      },
      lineStyle: {
        color: '#ffcdd2',
        width: 1,
        opacity: 0.6,
        curveness: 0.2
      },
      data: [
        { coords: [[116.4, 39.9], [117.0, 36.7]] },
        { coords: [[116.4, 39.9], [120.6, 31.3]] },
        { coords: [[117.0, 36.7], [120.6, 31.3]] },
        { coords: [[120.6, 31.3], [121.5, 31.2]] },
        { coords: [[116.4, 39.9], [112.9, 28.2]] },
        { coords: [[112.9, 28.2], [113.3, 23.1]] },
        { coords: [[113.3, 23.1], [114.1, 30.6]] },
      ]
    }
  ]
}
</script>

<style scoped>
.app-layout {
  min-height: 100vh;
  background: #f5f5f5;
}

/* 顶部导航条 */
.top-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 64px;
  background: linear-gradient(90deg, #c62828 0%, #e53935 50%, #f44336 100%);
  padding: 0 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 40px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-icon {
  font-size: 28px;
}

.logo-text {
  font-size: 20px;
  font-weight: 700;
  color: #fff;
}

.top-menu {
  display: flex;
  gap: 8px;
}

.menu-item {
  padding: 8px 16px;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-size: 14px;
  border-radius: 4px;
  transition: all 0.3s;
}

.menu-item:hover {
  color: #fff;
  background: rgba(255,255,255,0.15);
}

.menu-item.active {
  color: #fff;
  background: rgba(255,255,255,0.2);
  font-weight: 500;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.search-box {
  position: relative;
}

.search-box input {
  width: 240px;
  height: 36px;
  border: none;
  border-radius: 18px;
  padding: 0 36px 0 16px;
  background: rgba(255,255,255,0.2);
  color: #fff;
  font-size: 14px;
  outline: none;
}

.search-box input::placeholder {
  color: rgba(255,255,255,0.6);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255,255,255,0.7);
}

.user-info {
  display: flex;
  align-items: center;
  gap: 16px;
  color: #fff;
}

.notification {
  font-size: 18px;
  cursor: pointer;
}

.username {
  font-size: 14px;
}

.avatar {
  font-size: 20px;
  cursor: pointer;
}

/* 主体布局 */
.main-container {
  display: flex;
  padding-top: 64px;
  min-height: 100vh;
}

/* 左侧菜单栏 */
.sidebar {
  width: 220px;
  background: #fff;
  border-right: 1px solid #e8e8e8;
  padding: 20px 0;
  position: fixed;
  left: 0;
  top: 64px;
  bottom: 0;
  overflow-y: auto;
}

.sidebar-section {
  margin-bottom: 24px;
}

.section-title {
  padding: 0 20px 12px;
  font-size: 12px;
  color: #999;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.sidebar-menu {
  list-style: none;
}

.sidebar-menu .menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  color: #666;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.sidebar-menu .menu-item:hover {
  color: #e53935;
  background: rgba(229, 57, 53, 0.05);
}

.sidebar-menu .menu-item.active {
  color: #e53935;
  background: rgba(229, 57, 53, 0.1);
  border-right: 3px solid #e53935;
}

.sidebar-menu .icon {
  font-size: 16px;
  width: 20px;
  text-align: center;
}

/* 主内容区 */
.content-area {
  flex: 1;
  margin-left: 220px;
  padding: 20px;
}

/* 统计卡片区 */
.stats-cards-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 20px;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  border: 1px solid #e8e8e8;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.card-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}

.card-icon.storage { background: rgba(33, 150, 243, 0.1); }
.card-icon.speed { background: rgba(229, 57, 53, 0.1); }
.card-icon.core { background: rgba(156, 39, 176, 0.1); }
.card-icon.center { background: rgba(255, 152, 0, 0.1); }
.card-icon.cluster { background: rgba(0, 150, 136, 0.1); }
.card-icon.app { background: rgba(63, 81, 181, 0.1); }
.card-icon.task { background: rgba(76, 175, 80, 0.1); }
.card-icon.time { background: rgba(0, 188, 212, 0.1); }

.card-content {
  flex: 1;
}

.card-label {
  font-size: 13px;
  color: #999;
  margin-bottom: 6px;
}

.card-value {
  font-size: 24px;
  font-weight: 700;
  color: #333;
  margin-bottom: 6px;
}

.card-value .unit {
  font-size: 14px;
  font-weight: 400;
  color: #666;
  margin-left: 4px;
}

.card-trend {
  font-size: 12px;
  font-weight: 500;
}

.card-trend.up { color: #4caf50; }
.card-trend.down { color: #e53935; }
.card-trend.stable { color: #999; }

/* 响应式 */
@media (max-width: 1400px) {
  .stats-cards-row {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .sidebar { display: none; }
  .content-area { margin-left: 0; }
  .stats-cards-row { grid-template-columns: 1fr; }
  .top-menu { display: none; }
}

/* 面板样式 */
.row {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

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
  background: #fafafa;
}

.cluster-panel { flex: 2; min-width: 500px; }

.cluster-table { width: 100%; border-collapse: collapse; }
.cluster-table th, .cluster-table td {
  padding: 14px 16px;
  text-align: left;
  border-bottom: 1px solid #f0f0f0;
  font-size: 13px;
}
.cluster-table th { color: #666; font-weight: 500; background: #fafafa; }
.cluster-table td { color: #333; }

.status.online {
  color: #4caf50;
  background: rgba(76, 175, 80, 0.1);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.chart-panel { flex: 1; min-width: 280px; }

.bar-panel { flex: 1; min-width: 280px; padding: 0 20px 20px; }

.bar-list { margin-top: 10px; }
.bar-item {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}
.bar-label { width: 90px; font-size: 12px; color: #666; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.bar-wrap { flex: 1; height: 10px; background: #f0f0f0; border-radius: 5px; overflow: hidden; }
.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #e53935, #ff8a80);
  border-radius: 5px;
  transition: width 0.5s ease;
}
.bar-fill.orange { background: linear-gradient(90deg, #ff9800, #ffcc80); }
.bar-fill.purple { background: linear-gradient(90deg, #9c27b0, #ce93d8); }
.bar-fill.cyan { background: linear-gradient(90deg, #00bcd4, #80deea); }
.bar-value { width: 70px; text-align: right; font-size: 12px; color: #e53935; font-weight: 600; }

.map-panel { flex: 1; width: 100%; }

.metrics-row { display: flex; gap: 20px; flex-wrap: wrap; }
.metric-card {
  flex: 1;
  min-width: 200px;
  background: #fff;
  border-radius: 8px;
  padding: 24px;
  text-align: center;
  border: 1px solid #e8e8e8;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.metric-title { font-size: 14px; color: #666; margin-bottom: 12px; }
.metric-value { font-size: 28px; font-weight: 700; color: #e53935; }

.output-panel { flex: 1; width: 100%; padding-bottom: 20px; }
.output-grid { display: flex; justify-content: space-around; padding: 30px 20px; flex-wrap: wrap; gap: 20px; }
.output-item { text-align: center; min-width: 120px; }
.output-name { font-size: 13px; color: #666; margin-bottom: 12px; }
.output-value { font-size: 22px; font-weight: 700; color: #e53935; }

.bottom-row { display: flex; gap: 20px; flex-wrap: wrap; }
.info-card {
  flex: 1;
  min-width: 250px;
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
.info-icon {
  width: 60px;
  height: 60px;
  background: rgba(255,255,255,0.2);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
}
.info-card.red .info-title { font-size: 16px; font-weight: 600; margin-bottom: 4px; }
.info-card.red .info-desc { font-size: 13px; opacity: 0.9; }
.info-header { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; font-size: 13px; color: #999; }
.info-header .dot { width: 8px; height: 8px; background: #e53935; border-radius: 50%; }
.info-card:not(.red) .info-title { font-size: 15px; font-weight: 600; color: #333; margin-bottom: 8px; }
.info-card:not(.red) .info-desc { font-size: 13px; color: #666; line-height: 1.6; }
</style>