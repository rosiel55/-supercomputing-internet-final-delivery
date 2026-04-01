<template>
  <div class="placeholder-page">
    <div class="page-header">
      <h1>函数服务市场</h1>
      <p class="subtitle">50+跨中心统一调用接口</p>
    </div>
    
    <el-card>
      <div class="placeholder-content">
        <el-empty description="功能开发中...">
          <template #description>
            <p>函数服务市场模块</p>
            <p class="sub">将展示50+计算单元函数接口，支持在线调用测试</p>
          </template>
        </el-empty>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
// Functions Market - TODO
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
