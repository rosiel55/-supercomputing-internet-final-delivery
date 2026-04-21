<template>
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
      </div>
    </main>
  </div>
</template>

<style scoped>
.main-container {
  display: flex;
  padding-top: 56px;
  min-height: 100vh;
}

.sidebar {
  width: 200px;
  background: #fff;
  border-right: 1px solid #e4e7ed;
  padding: 16px 0;
  position: fixed;
  top: 56px;
  left: 0;
  bottom: 0;
  overflow-y: auto;
}

.sidebar-section {
  margin-bottom: 8px;
}

.section-title {
  padding: 8px 20px;
  font-size: 12px;
  color: #909399;
  font-weight: 600;
  text-transform: uppercase;
}

.sidebar-menu {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar-menu .menu-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  font-size: 13px;
  color: #606266;
  cursor: pointer;
  transition: all 0.2s;
}

.sidebar-menu .menu-item:hover {
  background: #f5f7fa;
  color: #dc2626;
}

.sidebar-menu .menu-item.active {
  background: #fef2f2;
  color: #dc2626;
  border-right: 3px solid #dc2626;
}

.icon {
  font-size: 14px;
  width: 20px;
  text-align: center;
}

.content-area {
  flex: 1;
  margin-left: 200px;
  padding: 24px;
  background: #f5f7fa;
  min-height: calc(100vh - 56px);
}

.stats-cards-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}

.card-icon {
  font-size: 32px;
}

.card-content {
  flex: 1;
}

.card-label {
  font-size: 13px;
  color: #909399;
  margin-bottom: 4px;
}

.card-value {
  font-size: 24px;
  font-weight: 600;
  color: #303133;
}

.unit {
  font-size: 14px;
  color: #606266;
  margin-left: 2px;
}

.card-trend {
  font-size: 12px;
  margin-top: 4px;
}

.card-trend.up {
  color: #67c23a;
}

.card-trend.stable {
  color: #909399;
}
</style>
