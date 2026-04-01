<template>
  <div class="dashboard-container">
    <!-- 页面标题 -->
    <div class="page-header">
      <h1>全局资源视图</h1>
      <p class="subtitle">覆盖长沙、广州、昆山、济南四大超算中心资源概览</p>
    </div>
    
    <!-- 统计卡片 -->
    <el-row :gutter="20" class="stat-row">
      <el-col :span="6" v-for="stat in statistics" :key="stat.title">
        <el-card class="stat-card">
          <div class="stat-content">
            <div class="stat-icon" :style="{ backgroundColor: stat.color }">
              <el-icon :size="24" color="#fff">
                <component :is="stat.icon" />
              </el-icon>
            </div>
            <div class="stat-info">
              <div class="stat-value">{{ stat.value }}</div>
              <div class="stat-title">{{ stat.title }}</div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    
    <!-- 资源拓扑图 -->
    <el-card class="topology-card">
      <template #header>
        <div class="card-header">
          <span>超算中心资源拓扑</span>
          <el-radio-group v-model="topologyType" size="small">
            <el-radio-button label="all">全部</el-radio-button>
            <el-radio-button label="compute">算力</el-radio-button>
            <el-radio-button label="storage">存储</el-radio-button>
          </el-radio-group>
        </div>
      </template>
      
      <div class="topology-chart" ref="topologyChart">
        <!-- ECharts 拓扑图将渲染在这里 -->
        <div class="placeholder-chart">
          <v-chart class="chart" :option="topologyOption" autoresize />
        </div>
      </div>
    </el-card>
    
    <!-- 中心资源详情 -->
    <el-row :gutter="20" class="center-row">
      <el-col :span="12" v-for="center in centers" :key="center.name">
        <el-card class="center-card">
          <template #header>
            <div class="center-header">
              <span class="center-name">{{ center.name }}</span>
              <el-tag :type="center.status.type" size="small">{{ center.status.text }}</el-tag>
            </div>
          </template>
          
          <div class="center-info">
            <div class="info-item">
              <span class="label">体系架构：</span>
              <span class="value">{{ center.architecture }}</span>
            </div>
            <div class="info-item">
              <span class="label">计算节点：</span>
              <span class="value">{{ center.nodes }}</span>
            </div>
            <div class="info-item">
              <span class="label">存储容量：</span>
              <span class="value">{{ center.storage }}</span>
            </div>
            <div class="info-item">
              <span class="label">活跃任务：</span>
              <span class="value">{{ center.tasks }}</span>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { GraphChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart from 'vue-echarts'
import { Cpu, Document, OfficeBuilding, Monitor } from '@element-plus/icons-vue'

use([CanvasRenderer, GraphChart, TitleComponent, TooltipComponent, LegendComponent])

// 统计数据
const statistics = ref([
  { title: '超算中心', value: '4个', icon: 'OfficeBuilding', color: '#409EFF' },
  { title: '计算节点', value: '100,000+', icon: 'Cpu', color: '#67C23A' },
  { title: '存储容量', value: '10 PB+', icon: 'Document', color: '#E6A23C' },
  { title: '活跃任务', value: '1,234', icon: 'Monitor', color: '#F56C6C' },
])

// 拓扑图类型
const topologyType = ref('all')

// 拓扑图配置
const topologyOption = ref({
  title: {
    text: '超算互联网资源拓扑',
    left: 'center',
  },
  tooltip: {},
  series: [
    {
      type: 'graph',
      layout: 'force',
      data: [
        { name: '长沙超算', symbolSize: 80, category: 0 },
        { name: '广州超算', symbolSize: 80, category: 0 },
        { name: '昆山超算', symbolSize: 80, category: 0 },
        { name: '济南超算', symbolSize: 80, category: 0 },
        { name: '调度中心', symbolSize: 100, category: 1 },
      ],
      links: [
        { source: '调度中心', target: '长沙超算' },
        { source: '调度中心', target: '广州超算' },
        { source: '调度中心', target: '昆山超算' },
        { source: '调度中心', target: '济南超算' },
      ],
      categories: [{ name: '超算中心' }, { name: '调度节点' }],
      roam: true,
      label: {
        show: true,
        position: 'bottom',
      },
      force: {
        repulsion: 1000,
        edgeLength: 200,
      },
    },
  ],
})

// 中心数据
const centers = ref([
  {
    name: '长沙超算中心',
    architecture: '天河',
    nodes: '40,000+',
    storage: '5 PB',
    tasks: '456',
    status: { type: 'success', text: '正常运行' },
  },
  {
    name: '广州超算中心',
    architecture: '天河',
    nodes: '35,000+',
    storage: '3 PB',
    tasks: '389',
    status: { type: 'success', text: '正常运行' },
  },
  {
    name: '昆山超算中心',
    architecture: '神威',
    nodes: '15,000+',
    storage: '1.5 PB',
    tasks: '234',
    status: { type: 'warning', text: '维护中' },
  },
  {
    name: '济南超算中心',
    architecture: '神威',
    nodes: '10,000+',
    storage: '1 PB',
    tasks: '155',
    status: { type: 'success', text: '正常运行' },
  },
])
</script>

<style scoped lang="scss">
.dashboard-container {
  .page-header {
    margin-bottom: 24px;
    
    h1 {
      font-size: 24px;
      font-weight: 600;
      color: #303133;
      margin-bottom: 8px;
    }
    
    .subtitle {
      color: #909399;
      font-size: 14px;
    }
  }
  
  .stat-row {
    margin-bottom: 20px;
    
    .stat-card {
      .stat-content {
        display: flex;
        align-items: center;
        
        .stat-icon {
          width: 56px;
          height: 56px;
          border-radius: 8px;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-right: 16px;
        }
        
        .stat-info {
          .stat-value {
            font-size: 24px;
            font-weight: 600;
            color: #303133;
            margin-bottom: 4px;
          }
          
          .stat-title {
            font-size: 14px;
            color: #909399;
          }
        }
      }
    }
  }
  
  .topology-card {
    margin-bottom: 20px;
    
    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    
    .topology-chart {
      height: 400px;
      
      .placeholder-chart {
        height: 100%;
        
        .chart {
          height: 100%;
        }
      }
    }
  }
  
  .center-row {
    .center-card {
      .center-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        
        .center-name {
          font-size: 16px;
          font-weight: 600;
        }
      }
      
      .center-info {
        .info-item {
          display: flex;
          justify-content: space-between;
          padding: 12px 0;
          border-bottom: 1px solid #ebeef5;
          
          &:last-child {
            border-bottom: none;
          }
          
          .label {
            color: #909399;
          }
          
          .value {
            color: #303133;
            font-weight: 500;
          }
        }
      }
    }
  }
}
</style>
