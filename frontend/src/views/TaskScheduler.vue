<template>
  <div class="main-container">
    <!-- 左侧工具栏 -->
    <aside class="toolbar">
      <div class="toolbar-title">节点工具箱</div>
      <div class="node-palette">
        <div class="palette-section">
          <div class="section-label">基础节点</div>
          <div class="node-item" draggable="true" @dragstart="onDragStart($event, 'start')">
            <span class="node-icon">🟢</span>
            <span>开始</span>
          </div>
          <div class="node-item" draggable="true" @dragstart="onDragStart($event, 'end')">
            <span class="node-icon">🔴</span>
            <span>结束</span>
          </div>
        </div>
        <div class="palette-section">
          <div class="section-label">任务节点</div>
          <div class="node-item" draggable="true" @dragstart="onDragStart($event, 'shell')">
            <span class="node-icon">📜</span>
            <span>Shell脚本</span>
          </div>
          <div class="node-item disabled">
            <span class="node-icon">🐍</span>
            <span>Python</span>
            <span class="badge">待开发</span>
          </div>
          <div class="node-item disabled">
            <span class="node-icon">🗃️</span>
            <span>SQL</span>
            <span class="badge">待开发</span>
          </div>
          <div class="node-item disabled">
            <span class="node-icon">🖥️</span>
            <span>HPC</span>
            <span class="badge">待开发</span>
          </div>
        </div>
      </div>
    </aside>

    <!-- 中间画布区 -->
    <div class="canvas-wrapper">
      <div class="canvas-header">
        <div class="workflow-info">
          <h3>{{ workflowName || '未命名工作流' }}</h3>
          <span class="status-badge" :class="workflowStatus">{{ statusText }}</span>
        </div>
        <div class="canvas-actions">
          <button class="btn btn-secondary" @click="clearCanvas">清空</button>
          <button class="btn btn-secondary" @click="saveWorkflow">保存</button>
          <button class="btn btn-primary" @click="runWorkflow">运行</button>
        </div>
      </div>

      <VueFlow
        v-model="elements"
        :default-zoom="1"
        :min-zoom="0.2"
        :max-zoom="4"
        :snap-to-grid="true"
        :snap-grid="[15, 15]"
        @dragover="onDragOver"
        @drop="onDrop"
        @node-click="onNodeClick"
        @connect="onConnect"
        class="flow-canvas"
      >
        <Background pattern-color="#e4e7ed" :gap="20" />
        <MiniMap />
        <Controls />
        
        <!-- 自定义节点 -->
        <template #node-start="props">
          <div class="custom-node node-start" :class="{ selected: props.selected }">
            <div class="node-header">
              <span class="node-type-icon">🟢</span>
              <span class="node-title">开始</span>
            </div>
          </div>
        </template>
        
        <template #node-end="props">
          <div class="custom-node node-end" :class="{ selected: props.selected }">
            <div class="node-header">
              <span class="node-type-icon">🔴</span>
              <span class="node-title">结束</span>
            </div>
          </div>
        </template>
        
        <template #node-shell="props">
          <div class="custom-node node-shell" :class="{ selected: props.selected }">
            <div class="node-header">
              <span class="node-type-icon">📜</span>
              <span class="node-title">Shell脚本</span>
              <span v-if="props.data?.command" class="node-status" :class="props.data.status">{{ statusIcon(props.data.status) }}</span>
            </div>
            <div class="node-body" v-if="props.data?.command">
              <code class="command-preview">{{ truncate(props.data.command, 30) }}</code>
            </div>
            <div v-else class="node-empty">点击配置命令</div>
          </div>
        </template>
      </VueFlow>
    </div>

    <!-- 右侧属性面板 -->
    <aside class="property-panel" v-if="selectedNode">
      <div class="panel-header">
        <h4>节点配置</h4>
        <button class="close-btn" @click="selectedNode = null">×</button>
      </div>
      
      <div class="panel-body">
        <!-- Shell节点配置 -->
        <template v-if="selectedNode.type === 'shell'">
          <div class="form-group">
            <label>节点名称</label>
            <input v-model="selectedNode.data.name" placeholder="输入节点名称" />
          </div>
          <div class="form-group">
            <label>Shell命令</label>
            <textarea 
              v-model="selectedNode.data.command" 
              rows="6" 
              placeholder="输入Shell命令...&#10;例如: echo 'Hello World'"
            />
          </div>
          <div class="form-group">
            <label>工作目录</label>
            <input v-model="selectedNode.data.workDir" placeholder="/opt/tasks" />
          </div>
          <div class="form-group">
            <label>环境变量</label>
            <div class="env-list">
              <div v-for="(env, index) in selectedNode.data.envVars" :key="index" class="env-row">
                <input v-model="env.key" placeholder="KEY" class="env-key" />
                <span>=</span>
                <input v-model="env.value" placeholder="value" class="env-value" />
                <button class="btn-icon" @click="removeEnv(index)">🗑️</button>
              </div>
              <button class="btn btn-text" @click="addEnv">+ 添加环境变量</button>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>超时时间(秒)</label>
              <input type="number" v-model="selectedNode.data.timeout" min="1" max="86400" />
            </div>
            <div class="form-group">
              <label>重试次数</label>
              <input type="number" v-model="selectedNode.data.retries" min="0" max="10" />
            </div>
          </div>
          <div class="form-group">
            <label>失败策略</label>
            <select v-model="selectedNode.data.failurePolicy">
              <option value="fail">立即失败</option>
              <option value="continue">继续执行</option>
              <option value="retry">重试后失败</option>
            </select>
          </div>
        </template>
        
        <!-- 开始/结束节点配置 -->
        <template v-else-if="['start', 'end'].includes(selectedNode.type)">
          <div class="form-group">
            <label>节点名称</label>
            <input v-model="selectedNode.data.name" :placeholder="selectedNode.type === 'start' ? '开始' : '结束'" />
          </div>
        </template>
      </div>
      
      <div class="panel-footer">
        <button class="btn btn-danger" @click="deleteNode">删除节点</button>
        <button class="btn btn-primary" @click="saveNodeConfig">保存配置</button>
      </div>
    </aside>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { VueFlow, useVueFlow } from '@vue-flow/core'
import { Background } from '@vue-flow/background'
import { MiniMap } from '@vue-flow/minimap'
import { Controls } from '@vue-flow/controls'
import '@vue-flow/core/dist/style.css'
import '@vue-flow/core/dist/theme-default.css'

interface NodeData {
  name: string
  command?: string
  workDir?: string
  envVars?: Array<{ key: string; value: string }>
  timeout?: number
  retries?: number
  failurePolicy?: string
  status?: string
}

interface FlowNode {
  id: string
  type: string
  label: string
  position: { x: number; y: number }
  data: NodeData
}

interface FlowEdge {
  id: string
  source: string
  target: string
  animated?: boolean
  style?: Record<string, string>
}

type FlowElement = FlowNode | FlowEdge

// 工作流状态
const workflowName = ref('')
const workflowStatus = ref('draft')
const statusText = computed(() => ({
  draft: '草稿',
  running: '运行中',
  success: '成功',
  failed: '失败'
})[workflowStatus.value] || '草稿')

// Vue Flow
const { addNodes, addEdges, removeNodes } = useVueFlow()

// 节点和边
const elements = ref<FlowElement[]>([
  {
    id: '1',
    type: 'start',
    label: '开始',
    position: { x: 100, y: 200 },
    data: { name: '开始' }
  },
  {
    id: '2',
    type: 'shell',
    label: 'Shell脚本',
    position: { x: 350, y: 200 },
    data: {
      name: '示例任务',
      command: '',
      workDir: '/opt/tasks',
      envVars: [],
      timeout: 3600,
      retries: 0,
      failurePolicy: 'fail',
      status: 'pending'
    }
  },
  {
    id: '3',
    type: 'end',
    label: '结束',
    position: { x: 600, y: 200 },
    data: { name: '结束' }
  }
])

const selectedNode = ref<FlowNode | null>(null)

// 拖拽创建节点
const onDragStart = (event: DragEvent, nodeType: string) => {
  event.dataTransfer?.setData('application/vueflow', nodeType)
  event.dataTransfer?.setData('text/plain', nodeType)
  event.dataTransfer!.effectAllowed = 'move'
}

const onDragOver = (event: DragEvent) => {
  event.preventDefault()
  if (event.dataTransfer) {
    event.dataTransfer.dropEffect = 'move'
  }
}

const onDrop = (event: DragEvent) => {
  event.preventDefault()
  const type = event.dataTransfer?.getData('application/vueflow')
  if (!type) return

  const { top, left } = (event.currentTarget as HTMLElement).getBoundingClientRect()
  const position = {
    x: event.clientX - left,
    y: event.clientY - top
  }

  const newNode: FlowNode = {
    id: `${Date.now()}`,
    type,
    label: type === 'shell' ? 'Shell脚本' : type,
    position,
    data: getDefaultNodeData(type)
  }

  addNodes([newNode])
}

const getDefaultNodeData = (type: string): NodeData => {
  switch (type) {
    case 'start':
      return { name: '开始' }
    case 'end':
      return { name: '结束' }
    case 'shell':
      return {
        name: 'Shell脚本',
        command: '',
        workDir: '/opt/tasks',
        envVars: [],
        timeout: 3600,
        retries: 0,
        failurePolicy: 'fail',
        status: 'pending'
      }
    default:
      return { name: type }
  }
}

// 点击节点
const onNodeClick = (event: any) => {
  selectedNode.value = event.node as FlowNode
}

// 连接节点
const onConnect = (params: { source: string; target: string }) => {
  const newEdge: FlowEdge = {
    id: `e-${params.source}-${params.target}`,
    source: params.source,
    target: params.target,
    animated: true,
    style: { stroke: '#dc2626' }
  }
  addEdges([newEdge])
}

// 状态图标
const statusIcon = (status: string | undefined) => {
  if (!status) return '⏳'
  const icons: Record<string, string> = {
    pending: '⏳',
    running: '🔄',
    success: '✅',
    failed: '❌'
  }
  return icons[status] || '⏳'
}

// 截断文本
const truncate = (text: string | undefined, maxLength: number) => {
  if (!text) return ''
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text
}

// 环境变量操作
const addEnv = () => {
  if (selectedNode.value?.data?.envVars) {
    selectedNode.value.data.envVars.push({ key: '', value: '' })
  }
}

const removeEnv = (index: number) => {
  if (selectedNode.value?.data?.envVars) {
    selectedNode.value.data.envVars.splice(index, 1)
  }
}

// 删除节点
const deleteNode = () => {
  if (selectedNode.value) {
    removeNodes([selectedNode.value.id])
    selectedNode.value = null
  }
}

// 保存节点配置
const saveNodeConfig = () => {
  console.log('保存节点配置:', selectedNode.value)
  selectedNode.value = null
}

// 画布操作
const clearCanvas = () => {
  elements.value = []
  selectedNode.value = null
}

const saveWorkflow = () => {
  console.log('保存工作流:', elements.value)
}

const runWorkflow = () => {
  workflowStatus.value = 'running'
  console.log('运行工作流:', elements.value)
}
</script>

<style scoped>
.main-container {
  display: flex;
  padding-top: 56px;
  height: 100vh;
  overflow: hidden;
}

/* 左侧工具栏 */
.toolbar {
  width: 200px;
  background: #fff;
  border-right: 1px solid #e4e7ed;
  padding: 16px;
  overflow-y: auto;
}

.toolbar-title {
  font-size: 14px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #e4e7ed;
}

.palette-section {
  margin-bottom: 20px;
}

.section-label {
  font-size: 12px;
  color: #909399;
  margin-bottom: 10px;
  text-transform: uppercase;
  font-weight: 600;
}

.node-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-radius: 6px;
  cursor: grab;
  transition: all 0.2s;
  font-size: 13px;
  color: #606266;
  margin-bottom: 6px;
  border: 1px solid #e4e7ed;
  background: #fff;
}

.node-item:hover {
  border-color: #dc2626;
  color: #dc2626;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.1);
}

.node-item.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.node-icon {
  font-size: 16px;
}

.badge {
  margin-left: auto;
  font-size: 10px;
  padding: 2px 6px;
  background: #f5f7fa;
  color: #909399;
  border-radius: 4px;
}

/* 中间画布 */
.canvas-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #f5f7fa;
}

.canvas-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background: #fff;
  border-bottom: 1px solid #e4e7ed;
}

.workflow-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.workflow-info h3 {
  font-size: 16px;
  font-weight: 600;
  color: #303133;
}

.status-badge {
  font-size: 12px;
  padding: 4px 10px;
  border-radius: 12px;
  font-weight: 500;
}

.status-badge.draft {
  background: #f5f7fa;
  color: #909399;
}

.status-badge.running {
  background: #fef2f2;
  color: #dc2626;
}

.status-badge.success {
  background: #f0f9ff;
  color: #67c23a;
}

.status-badge.failed {
  background: #fef2f2;
  color: #f56c6c;
}

.canvas-actions {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 8px 18px;
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid transparent;
}

.btn-primary {
  background: #dc2626;
  color: #fff;
  border-color: #dc2626;
}

.btn-primary:hover {
  background: #b91c1c;
}

.btn-secondary {
  background: #fff;
  color: #606266;
  border-color: #dcdfe6;
}

.btn-secondary:hover {
  color: #dc2626;
  border-color: #dc2626;
}

.btn-danger {
  background: #fef2f2;
  color: #f56c6c;
  border-color: #fcd5d5;
}

.btn-text {
  background: transparent;
  color: #dc2626;
  padding: 6px 0;
}

.flow-canvas {
  flex: 1;
  background: #fff;
}

/* 自定义节点 */
.custom-node {
  background: #fff;
  border: 2px solid #e4e7ed;
  border-radius: 8px;
  padding: 12px 16px;
  min-width: 160px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: all 0.2s;
}

.custom-node:hover {
  border-color: #dc2626;
  box-shadow: 0 4px 16px rgba(220, 38, 38, 0.12);
}

.custom-node.selected {
  border-color: #dc2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.15);
}

.node-start {
  border-color: #67c23a;
  background: #f0f9ff;
}

.node-end {
  border-color: #f56c6c;
  background: #fef2f2;
}

.node-shell {
  border-color: #409eff;
  background: #fff;
}

.node-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.node-type-icon {
  font-size: 18px;
}

.node-title {
  font-size: 14px;
  font-weight: 600;
  color: #303133;
}

.node-status {
  margin-left: auto;
  font-size: 14px;
}

.node-body {
  padding-top: 8px;
  border-top: 1px solid #f0f0f0;
}

.command-preview {
  font-size: 12px;
  color: #606266;
  background: #f5f7fa;
  padding: 6px 10px;
  border-radius: 4px;
  display: block;
  font-family: 'Courier New', monospace;
}

.node-empty {
  font-size: 12px;
  color: #909399;
  text-align: center;
  padding: 8px;
}

/* 右侧面板 */
.property-panel {
  width: 320px;
  background: #fff;
  border-left: 1px solid #e4e7ed;
  display: flex;
  flex-direction: column;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid #e4e7ed;
}

.panel-header h4 {
  font-size: 15px;
  font-weight: 600;
  color: #303133;
}

.close-btn {
  background: none;
  border: none;
  font-size: 20px;
  color: #909399;
  cursor: pointer;
}

.panel-body {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  font-size: 13px;
  font-weight: 500;
  color: #606266;
  margin-bottom: 6px;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 13px;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  border-color: #dc2626;
  outline: none;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.env-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.env-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.env-key,
.env-value {
  flex: 1;
}

.btn-icon {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 14px;
  padding: 4px;
}

.panel-footer {
  display: flex;
  justify-content: space-between;
  padding: 16px 20px;
  border-top: 1px solid #e4e7ed;
}
</style>
