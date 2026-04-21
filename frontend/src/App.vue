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
          <router-link to="/" class="menu-item" :class="{ active: $route.path === '/' }">首页</router-link>
          <a href="#" class="menu-item">资源管理</a>
          <router-link to="/task-scheduler" class="menu-item" :class="{ active: $route.path === '/task-scheduler' }">任务调度</router-link>
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

    <!-- 主体区域 - 路由视图 -->
    <router-view />
  </div>
</template>

<script setup lang="ts">
// App.vue - 布局组件
</script>

<style scoped>
.app-layout {
  min-height: 100vh;
  background: #f5f7fa;
}

.top-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  height: 56px;
  background: #fff;
  border-bottom: 1px solid #e4e7ed;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 32px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: 600;
  color: #dc2626;
}

.logo-icon {
  font-size: 22px;
}

.top-menu {
  display: flex;
  gap: 4px;
}

.menu-item {
  padding: 8px 16px;
  text-decoration: none;
  color: #606266;
  font-size: 14px;
  border-radius: 4px;
  transition: all 0.2s;
  cursor: pointer;
}

.menu-item:hover {
  background: #f5f7fa;
  color: #dc2626;
}

.menu-item.active {
  color: #dc2626;
  background: #fef2f2;
  font-weight: 500;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.search-box {
  position: relative;
}

.search-box input {
  padding: 6px 12px;
  padding-right: 32px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 13px;
  width: 180px;
}

.search-icon {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 14px;
  color: #909399;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.notification {
  font-size: 16px;
  cursor: pointer;
}

.username {
  font-size: 14px;
  color: #606266;
}

.avatar {
  font-size: 20px;
}
</style>
