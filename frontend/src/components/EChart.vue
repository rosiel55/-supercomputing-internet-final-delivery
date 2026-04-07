<template>
  <div ref="chartRef" :style="{ width: width, height: height }"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'

// 优先使用CDN加载的全局echarts
const echarts = (window as any).echarts || require('echarts')

const props = defineProps<{
  option: any
  width?: string
  height?: string
}>()

const chartRef = ref<HTMLDivElement>()
let chartInstance: any = null

onMounted(() => {
  if (chartRef.value) {
    chartInstance = echarts.init(chartRef.value)
    chartInstance.setOption(props.option)
    
    // 响应式
    const resizeObserver = new ResizeObserver(() => {
      chartInstance?.resize()
    })
    resizeObserver.observe(chartRef.value)
  }
})

onUnmounted(() => {
  chartInstance?.dispose()
})

watch(() => props.option, (newOption) => {
  chartInstance?.setOption(newOption, true)
}, { deep: true })
</script>