<template>
  <div class="stats-card">
    <div class="card-header">
      <span class="card-icon">{{ icon }}</span>
      <span class="card-title">{{ title }}</span>
    </div>
    <div class="card-value">{{ value }}</div>    
    <div class="card-trend" :class="{ positive: positive, negative: !positive }">
      <span>{{ trend }}</span>
      <span class="trend-label">较上周</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  value: string
  trend: string
  positive: boolean
  icon: string
}>()
</script>

<style scoped>
.stats-card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #e0e0e0;
  border-top: 3px solid #e53935;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: all 0.3s;
}

.stats-card:hover {
  border-color: #e53935;
  box-shadow: 0 4px 12px rgba(229, 57, 53, 0.15);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.card-icon {
  font-size: 20px;
}

.card-title {
  font-size: 14px;
  color: #666;
}

.card-value {
  font-size: 28px;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
}

.card-trend {
  font-size: 13px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-trend.positive {
  color: #4caf50;
}

.card-trend.negative {
  color: #e53935;
}

.trend-label {
  color: #999;
  font-size: 12px;
}
</style>