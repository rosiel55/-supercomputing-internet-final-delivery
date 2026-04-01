<template>
  <div class="placeholder-page">
    <div class="page-header">
      <h1>资源监控</h1>
      <p class="subtitle">集成Grafana与scnet.cn监控数据</p>
    </div>
    
    <el-card>
      <div class="placeholder-content">
        <el-empty description="功能开发中...">
          <template #description>
            <p>资源监控模块</p>
            <p class="sub">集成济南超算Grafana、国家超算互联网等监控面板</p>
          </template>
        </el-empty>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
// Monitor - TODO
</script>

<style scoped>
.placeholder-page {
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
  
  .placeholder-content {
    min-height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
    
    .sub {
      color: #909399;
      font-size: 12px;
      margin-top: 8px;
    }
  }
}
</style>
