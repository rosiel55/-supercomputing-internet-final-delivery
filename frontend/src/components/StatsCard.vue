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
  background: #0d2137;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #1e3a5f;
  transition: all 0.3s;
}

.stats-card:hover {
  border-color: #4fc3f7;
  box-shadow: 0 0 20px rgba(79, 195, 247, 0.1);
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
  color: #8b9dc3;
}

.card-value {
  font-size: 28px;
  font-weight: 600;
  color: #fff;
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
  color: #f44336;
}

.trend-label {
  color: #8b9dc3;
  font-size: 12px;
}
</style>