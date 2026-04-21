# DolphinScheduler 简化集成方案 - 超算互联网项目

**研究时间**: 2026-04-07 16:38-16:54  
**方案目标**: 只取DS工作流引擎核心，自研前端，配色统一  
**状态**: ✅ 方案已确认，待明天开发

---

## 1. 核心思路调整

### ❌ 原方案（复杂）
- 部署完整DolphinScheduler（API + Web UI + Master + Worker）
- iframe嵌入DS前端
- 两套系统，两套UI

### ✅ 新方案（简化）
- **只部署DS后端**：API Server + Master + Worker（无前端）
- **自研前端**：在超算项目里直接开发工作流编辑器
- **统一配色**：白底红色企业风，与超算首页一致
- **API对接**：通过REST API操作工作流

---

## 2. 简化架构

```
┌─────────────────────────────────────────────────────────┐
│  超算互联网项目 (Vue3 + Vite + TypeScript)               │
│                                                          │
│  ┌─────────────────────────────────────────────────────┐│
│  │  首页 Dashboard                                       ││
│  │  ├── 统计卡片（任务状态概览）                          ││
│  │  ├── 最近工作流列表                                   ││
│  │  └── 快捷操作按钮                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                          │
│  ┌─────────────────────────────────────────────────────┐│
│  │  任务调度页面（全新开发）                              ││
│  │  ├── DAG画布（基于Vue-Flow或自研SVG）                 ││
│  │  ├── 节点库（Shell、Python、SQL等）                   ││
│  │  ├── 属性面板（节点配置）                             ││
│  │  └── 工具栏（保存、运行、定时）                        ││
│  └─────────────────────────────────────────────────────┘│
│                                                          │
│  ┌─────────────────────────────────────────────────────┐│
│  │  API封装层                                            ││
│  │  └── schedulerApi.ts（调用DS后端接口）                ││
│  └─────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘
                            │ REST API
                            ▼
┌─────────────────────────────────────────────────────────┐
│  DolphinScheduler 后端（无前端）                          │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ API Server   │  │ Master       │  │ Worker       │  │
│  │ (REST接口)   │  │ (调度引擎)   │  │ (任务执行)   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                          │
│  依赖: MySQL + ZooKeeper（可简化）                        │
└─────────────────────────────────────────────────────────┘
```

---

## 3. 前端技术选型

### DAG编辑器方案对比

| 方案 | 优点 | 缺点 | 推荐度 |
|:---|:---|:---|:---:|
| **@vue-flow/core** | Vue3原生、轻量、易定制 | 功能较基础 | ⭐⭐⭐⭐⭐ |
| **LogicFlow** | 阿里开源、功能全、中文好 | 体积较大 | ⭐⭐⭐⭐ |
| **自研SVG** | 完全可控、无依赖 | 开发成本高 | ⭐⭐⭐ |
| **X6 (AntV)** | 功能强大、生态好 | 学习曲线陡 | ⭐⭐⭐ |

**推荐**: **@vue-flow/core** + 自定义节点样式

### 安装
```bash
cd /root/.openclaw/workspace/projects/超算互联网项目/frontend
npm install @vue-flow/core @vue-flow/background @vue-flow/controls @vue-flow/minimap
```

---

## 4. 配色方案统一

### 超算项目当前配色（白底红色企业风）
```css
/* 背景 */
--bg-primary: #f5f5f5;      /* 浅灰背景 */
--bg-white: #ffffff;        /* 白色卡片 */

/* 主色调 */
--primary-red: #c62828;     /* 深红 */
--primary-light: #f44336;   /* 亮红 */
--primary-gradient: linear-gradient(135deg, #c62828 0%, #f44336 100%);

/* 文字 */
--text-primary: #333333;    /* 主文字 */
--text-secondary: #666666;  /* 次要文字 */
--text-muted: #999999;      /* 辅助文字 */

/* 边框 */
--border-color: #e0e0e0;    /* 浅灰边框 */
--border-light: #f0f0f0;    /* 更浅边框 */
```

### DAG编辑器配色适配
```css
/* 画布背景 */
.vue-flow__background {
  background-color: #f5f5f5;
}

/* 节点样式 */
.node-task {
  background: #ffffff;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.node-task:hover {
  border-color: #f44336;
  box-shadow: 0 4px 12px rgba(244,67,54,0.15);
}

.node-task.selected {
  border-color: #c62828;
  box-shadow: 0 0 0 3px rgba(198,40,40,0.1);
}

/* 连接线 */
.vue-flow__edge-path {
  stroke: #c62828;
  stroke-width: 2;
}

/* 开始/结束节点 */
.node-start {
  background: linear-gradient(135deg, #c62828 0%, #f44336 100%);
  color: white;
}
```

---

## 5. 核心功能模块

### 5.1 DAG画布组件
```vue
<!-- src/components/WorkflowEditor/FlowCanvas.vue -->
<template>
  <div class="workflow-canvas">
    <VueFlow
      v-model="elements"
      :default-zoom="1"
      :min-zoom="0.2"
      :max-zoom="4"
      fit-view-on-init
      @node-click="onNodeClick"
      @edge-click="onEdgeClick"
    >
      <Background pattern-color="#e0e0e0" :gap="20" />
      <MiniMap />
      <Controls />
      
      <!-- 自定义节点 -->
      <template #node-shell="props">
        <ShellNode :data="props.data" />
      </template>
      <template #node-python="props">
        <PythonNode :data="props.data" />
      </template>
      <template #node-sql="props">
        <SqlNode :data="props.data" />
      </template>
    </VueFlow>
  </div>
</template>
```

### 5.2 节点类型定义
```typescript
// src/types/workflow.ts
export interface WorkflowNode {
  id: string
  type: 'shell' | 'python' | 'sql' | 'start' | 'end'
  position: { x: number; y: number }
  data: {
    name: string
    config: NodeConfig
    status?: 'pending' | 'running' | 'success' | 'failed'
  }
}

export interface NodeConfig {
  // Shell节点
  script?: string
  
  // Python节点
  pythonScript?: string
  
  // SQL节点
  sql?: string
  datasource?: string
  
  // 通用
  timeout?: number
  retryTimes?: number
  priority?: 'high' | 'medium' | 'low'
}
```

### 5.3 DS API封装
```typescript
// src/api/scheduler.ts
import axios from 'axios'

const dsClient = axios.create({
  baseURL: 'http://localhost:12345/dolphinscheduler',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 工作流定义API
export const workflowApi = {
  // 创建工作流
  create: (projectCode: string, data: WorkflowDefinition) => 
    dsClient.post(`/projects/${projectCode}/process-definition`, data),
  
  // 更新工作流
  update: (projectCode: string, code: string, data: WorkflowDefinition) =>
    dsClient.put(`/projects/${projectCode}/process-definition/${code}`, data),
  
  // 获取工作流列表
  list: (projectCode: string) =>
    dsClient.get(`/projects/${projectCode}/process-definition`),
  
  // 获取工作流详情
  detail: (projectCode: string, code: string) =>
    dsClient.get(`/projects/${projectCode}/process-definition/${code}`),
  
  // 发布工作流
  release: (projectCode: string, code: string) =>
    dsClient.post(`/projects/${projectCode}/process-definition/${code}/release`, { releaseState: 'ONLINE' }),
  
  // 运行工作流
  start: (projectCode: string, code: string) =>
    dsClient.post(`/projects/${projectCode}/executors/start-process-instance`, {
      processDefinitionCode: code
    }),
  
  // 停止工作流
  stop: (projectCode: string, processInstanceId: number) =>
    dsClient.post(`/projects/${projectCode}/executors/execute`, {
      processInstanceId,
      executeType: 'STOP'
    })
}

// 任务实例API
export const taskInstanceApi = {
  // 获取任务实例列表
  list: (projectCode: string, processInstanceId?: number) =>
    dsClient.get('/task-instances', {
      params: { projectCode, processInstanceId }
    }),
  
  // 获取任务日志
  log: (taskInstanceId: number, skipLineNum?: number, limit?: number) =>
    dsClient.get(`/task-instances/${taskInstanceId}/log`, {
      params: { skipLineNum, limit }
    })
}
```

---

## 6. 页面结构设计

### 6.1 任务调度主页面
```
┌─────────────────────────────────────────────────────────────┐
│  任务调度                                     [新建工作流]  │
├──────────┬──────────────────────────────────────────────────┤
│          │                                                  │
│ 节点库   │  ┌────────────────────────────────────────────┐  │
│          │  │              DAG画布                        │  │
│  ┌───┐   │  │                                             │  │
│  │Shell│   │  │   ┌─────────┐      ┌─────────┐           │  │
│  └───┘   │  │   │  开始   ├──────►│ Shell   ├──────►    │  │
│          │  │   └─────────┘      └─────────┘           │  │
│  ┌───┐   │  │                                             │  │
│  │Python│  │  │        ┌─────────┐      ┌─────────┐     │  │
│  └───┘   │  │        └───────►│ Python  ├──────►│ 结束 │  │
│          │  │                  └─────────┘      └─────────┘  │
│  ┌───┐   │  │                                             │  │
│  │SQL │   │  └────────────────────────────────────────────┘  │
│  └───┘   │  │                                              │
│          │  └───────────────────────────────────────────────┘
│          │                                                  │
├──────────┤  ┌────────────────────────────────────────────┐  │
│ 属性面板  │  │ 节点配置                                     │  │
│          │  │ 名称: [任务A                    ]           │  │
│ 脚本:    │  │ 类型: [Shell                    ]           │  │
│ [      ] │  │ 超时: [30] 分钟                              │  │
│ [      ] │  │ 重试: [3] 次                                │  │
│ [      ] │  │                                             │  │
│          │  │ [保存] [运行] [定时] [删除]                  │  │
└──────────┴──┴─────────────────────────────────────────────┘
```

### 6.2 首页集成（Dashboard卡片）
```vue
<!-- src/views/Dashboard/TaskStatsCard.vue -->
<template>
  <div class="stats-card">
    <div class="card-header">
      <h3>任务调度概览</h3>
      <router-link to="/scheduler" class="view-all">查看全部 →</router-link>
    </div>
    <div class="stats-grid">
      <div class="stat-item">
        <div class="stat-value running">{{ stats.running }}</div>
        <div class="stat-label">运行中</div>
      </div>
      <div class="stat-item">
        <div class="stat-value success">{{ stats.success }}</div>
        <div class="stat-label">今日成功</div>
      </div>
      <div class="stat-item">
        <div class="stat-value failed">{{ stats.failed }}</div>
        <div class="stat-label">今日失败</div>
      </div>
      <div class="stat-item">
        <div class="stat-value pending">{{ stats.pending }}</div>
        <div class="stat-label">待执行</div>
      </div>
    </div>
    <div class="recent-workflows">
      <div class="workflow-item" v-for="wf in recentWorkflows" :key="wf.code">
        <span class="wf-name">{{ wf.name }}</span>
        <span :class="['wf-status', wf.status]">{{ formatStatus(wf.status) }}</span>
      </div>
    </div>
  </div>
</template>
```

---

## 7. 明日开发计划

### 上午（DS后端部署）
| 时间 | 任务 | 产出 |
|:---|:---|:---|
| 09:00-10:00 | 下载DolphinScheduler 3.2.0 standalone包 | DS压缩包 |
| 10:00-11:00 | 配置MySQL数据库、初始化 | DS元数据表 |
| 11:00-12:00 | 启动API+Master+Worker服务 | DS后端可访问 |

### 下午（前端开发）
| 时间 | 任务 | 产出 |
|:---|:---|:---|
| 14:00-15:00 | 安装@vue-flow/core，创建DAG画布基础组件 | 可拖拽画布 |
| 15:00-16:00 | 开发节点组件（Shell/Python/SQL）、统一配色 | 红色主题节点 |
| 16:00-17:00 | 开发属性面板、工具栏 | 可配置节点 |
| 17:00-18:00 | API对接：工作流CRUD、运行控制 | 可保存运行工作流 |

---

## 8. 关键配置

### 8.1 DS Standalone模式配置（简化部署）
```bash
# standalone模式不需要ZooKeeper，单节点运行
# 修改 conf/application.yaml
server:
  port: 12345

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/dolphinscheduler
    username: ds_user
    password: ds_password

# 单机模式配置
registry:
  type: jdbc  # 用数据库代替ZooKeeper
```

### 8.2 启动命令
```bash
cd apache-dolphinscheduler-3.2.0-bin

# 初始化数据库
bash tools/bin/upgrade-schema.sh

# 启动standalone模式
bash bin/start-all.sh

# 访问 http://localhost:12345/dolphinscheduler
# 默认账号: admin / dolphinscheduler123
```

---

## 9. 风险控制

| 风险 | 概率 | 应对方案 |
|:---|:---:|:---|
| Vue-Flow学习成本 | 低 | 官方文档完善，有示例 |
| DS API兼容性问题 | 中 | 先测试API，再开发前端 |
| DAG布局算法 | 中 | 使用Vue-Flow自动布局或自研 |
| 性能问题（大工作流） | 低 | 节点分页加载、虚拟滚动 |

---

## 10. 预期效果

### 用户流程
1. 登录超算互联网平台
2. 首页Dashboard显示任务调度概览卡片
3. 点击"查看全部"或侧边栏"任务调度"菜单
4. 进入工作流编辑器（白底红色主题，与首页统一）
5. 拖拽节点、连接、配置、保存、运行
6. 回到首页查看任务执行状态

### 界面预览
```
┌────────────────────────────────────────────────────────────┐
│  超算互联网平台                                             │
├────────┬───────────────────────────────────────────────────┤
│        │                                                   │
│ 首页   │   任务调度                        [+ 新建工作流]  │
│ 资源   │  ┌─────────┬─────────────────┬───────────────┐   │
│ 作业   │  │ 节点库   │                 │  属性面板     │   │
│ 调度◄──┼──┤  ┌───┐  │   DAG画布       │  名称: [   ]  │   │
│ 监控   │  │  │Shell│  │  ┌───┐  ┌───┐  │  脚本: [   ]  │   │
│        │  │  └───┘  │  │开始│──►│Shell│  │       [   ]  │   │
│        │  │  ┌───┐  │  └───┘  └───┘  │       [   ]  │   │
│        │  │  │SQL │  │       │        │              │   │
│        │  │  └───┘  │       ▼        │ [保存][运行] │   │
│        │  │         │     ┌───┐      │              │   │
│        │  │         │     │SQL│      │              │   │
│        │  │         │     └───┘      │              │   │
│        │  └─────────┴─────────────────┴───────────────┘   │
└────────┴───────────────────────────────────────────────────┘
```

---

**方案确认**: ✅ 简化版，只取DS后端引擎，自研前端，统一配色  
**技术栈**: Vue3 + @vue-flow/core + DS REST API  
**开发周期**: 1天（后端半天 + 前端半天）  
**风险**: 低（技术成熟，文档完善）

**待确认问题**:
1. 是否需要定时调度功能？（DS原生支持Quartz）
2. 节点类型只需要Shell/Python/SQL三种？
3. 工作流数量预估多少？（影响性能优化策略）

**明天9点开始部署DS后端！**
