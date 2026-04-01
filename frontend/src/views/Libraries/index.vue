<template>
  <div class="placeholder-page">
    <div class="page-header">
      <h1>数学库/求解器</h1>
      <p class="subtitle">20种基础数学库与求解器性能数据展示</p>
    </div>
    
    <el-card>
      <div class="placeholder-content">
        <el-empty description="功能开发中...">
          <template #description>
            <p>数学库/求解器模块</p>
            <p class="sub">展示20种库的自动测量结果与自适应调优数据</p>
          </template>
        </el-empty>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
// Libraries - TODO
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
