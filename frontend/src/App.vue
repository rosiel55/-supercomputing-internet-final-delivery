<template>
  <div class="dashboard">
    <!-- 顶部导航 -->
    <header class="header">
      <div class="logo">
        <h1>超算互联网</h1>
        <span class="subtitle">算力数据可视化平台</span>
      </div>
      <nav class="nav">
        <a href="#" class="active">总览</a>
        <a href="#">算力监控</a>
        <a href="#">任务调度</a>
        <a href="#">资源管理</a>
      </nav>
      <div class="user-info">
        <span>管理员</span>
      </div>
    </header>

    <!-- 主内容区 -->
    <div class="main-container">
      <!-- 侧边栏 -->
      <aside class="sidebar">
        <div class="menu-item active">
          <span class="icon">📊</span>
          <span>数据大屏</span>
        </div>
        <div class="menu-item">
          <span class="icon">🖥️</span>
          <span>节点管理</span>
        </div>
        <div class="menu-item">
          <span class="icon">⚡</span>
          <span>算力调度</span>
        </div>
        <div class="menu-item">
          <span class="icon">📈</span>
          <span>性能分析</span>
        </div>
      </aside>

      <!-- 内容区域 -->
      <main class="content">
        <!-- 统计卡片 -->
        <div class="stats-grid">
          <StatsCard
            title="总算力"
            value="2.4 PFLOPS"
            trend="+12%"
            :positive="true"
            icon="🚀"
          />
          <StatsCard
            title="在线节点"
            value="128"
            trend="+5"
            :positive="true"
            icon="🖥️"
          />
          <StatsCard
            title="运行任务"
            value="456"
            trend="-8"
            :positive="false"
            icon="⚙️"
          />
          <StatsCard
            title="资源利用率"
            value="78.5%"
            trend="+3.2%"
            :positive="true"
            icon="📊"
          />
        </div>

        <!-- 图表区域 -->
        <div class="charts-grid">
          <div class="chart-card large">
            <h3>算力使用趋势</h3>
            <div class="chart-placeholder">
              <p>📈 折线图 - 近7天算力使用趋势</p>
            </div>
          </div>
          <div class="chart-card">
            <h3>节点状态分布</h3>
            <div class="chart-placeholder">
              <p>🥧 饼图 - 节点状态分布</p>
            </div>
          </div>
        </div>

        <!-- 任务列表 -->
        <div class="task-section">
          <h3>最近任务</h3>
          <table class="task-table">
            <thead>
              <tr>
                <th>任务ID</th>
                <th>名称</th>
                <th>状态</th>
                <th>算力需求</th>
                <th>提交时间</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>T-20250406-001</td>
                <td>气象模拟计算</td>
                <td><span class="status running">运行中</span></td>
                <td>256 GFLOPS</td>
                <td>2025-04-06 10:30</td>
              </tr>
              <tr>
                <td>T-20250406-002</td>
                <td>基因序列分析</td>
                <td><span class="status pending">排队中</span></td>
                <td>512 GFLOPS</td>
                <td>2025-04-06 11:15</td>
              </tr>
              <tr>
                <td>T-20250406-003</td>
                <td>流体动力学仿真</td>
                <td><span class="status completed">已完成</span></td>
                <td>128 GFLOPS</td>
                <td>2025-04-06 09:00</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import StatsCard from './components/StatsCard.vue'
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: #0a1929;
  color: #fff;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 64px;
  background: linear-gradient(90deg, #0d2137 0%, #0a1929 100%);
  border-bottom: 1px solid #1e3a5f;
}

.logo h1 {
  font-size: 20px;
  font-weight: 600;
  color: #4fc3f7;
  margin: 0;
}

.subtitle {
  font-size: 12px;
  color: #8b9dc3;
  margin-left: 8px;
}

.nav {
  display: flex;
  gap: 32px;
}

.nav a {
  color: #8b9dc3;
  text-decoration: none;
  font-size: 14px;
  padding: 8px 0;
  border-bottom: 2px solid transparent;
  transition: all 0.3s;
}

.nav a.active,
.nav a:hover {
  color: #4fc3f7;
  border-bottom-color: #4fc3f7;
}

.main-container {
  display: flex;
  height: calc(100vh - 64px);
}

.sidebar {
  width: 200px;
  background: #0d2137;
  padding: 16px 0;
  border-right: 1px solid #1e3a5f;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  cursor: pointer;
  transition: all 0.3s;
  color: #8b9dc3;
}

.menu-item:hover,
.menu-item.active {
  background: rgba(79, 195, 247, 0.1);
  color: #4fc3f7;
  border-right: 3px solid #4fc3f7;
}

.icon {
  font-size: 18px;
}

.content {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 24px;
}

.charts-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  margin-bottom: 24px;
}

.chart-card {
  background: #0d2137;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #1e3a5f;
}

.chart-card h3 {
  margin: 0 0 16px 0;
  font-size: 16px;
  color: #4fc3f7;
}

.chart-placeholder {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(79, 195, 247, 0.05);
  border-radius: 4px;
  color: #8b9dc3;
}

.task-section {
  background: #0d2137;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #1e3a5f;
}

.task-section h3 {
  margin: 0 0 16px 0;
  font-size: 16px;
  color: #4fc3f7;
}

.task-table {
  width: 100%;
  border-collapse: collapse;
}

.task-table th,
.task-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #1e3a5f;
}

.task-table th {
  color: #8b9dc3;
  font-weight: 500;
}

.task-table td {
  color: #fff;
}

.status {
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
}

.status.running {
  background: rgba(76, 175, 80, 0.2);
  color: #4caf50;
}

.status.pending {
  background: rgba(255, 152, 0, 0.2);
  color: #ff9800;
}

.status.completed {
  background: rgba(33, 150, 243, 0.2);
  color: #2196f3;
}
</style>