# DolphinScheduler 集成研究 - 超算互联网项目任务调度

**研究时间**: 2026-04-07 16:28-16:38  
**研究目标**: 将Apache DolphinScheduler集成到超算互联网项目，实现任务调度功能  
**状态**: ✅ 可行性已验证，开发思路已明确

---

## 1. DolphinScheduler 简介

Apache DolphinScheduler 是一款**云原生分布式工作流任务调度平台**，特点：
- **可视化DAG**: 拖拽式工作流编排
- **分布式架构**: Master/Worker分离，支持集群部署
- **高可用**: Zookeeper协调，Master故障自动切换
- **多任务类型**: Shell、Python、SQL、Spark、Flink等
- **Apache开源**: 活跃社区，企业级应用广泛

---

## 2. 架构分析

```
┌─────────────────────────────────────────────────────────┐
│  Web UI (Vue.js) - 可视化工作流编辑、监控                    │
├─────────────────────────────────────────────────────────┤
│  API Server - RESTful接口，提供Web和第三方调用               │
├─────────────────────────────────────────────────────────┤
│  Master Server - 任务调度、工作流管理、资源分配              │
│  (可集群部署，无中心化设计)                                  │
├─────────────────────────────────────────────────────────┤
│  Worker Server - 任务执行节点                               │
│  (可水平扩展，执行具体任务)                                  │
├─────────────────────────────────────────────────────────┤
│  ZooKeeper - 服务注册、协调、Master选举                      │
├─────────────────────────────────────────────────────────┤
│  MySQL/PostgreSQL - 元数据存储                              │
└─────────────────────────────────────────────────────────┘
```

### 核心技术栈
- **后端**: Java + Spring Boot + Spring Cloud
- **前端**: Vue.js (与超算项目一致 ✅)
- **数据库**: MySQL/PostgreSQL
- **协调**: ZooKeeper
- **构建**: Maven

---

## 3. 集成方案设计

### 方案A: 独立部署 + iframe嵌入（推荐）

```
超算互联网项目 (Vue3 + Vite)
    │
    ├── 首页 Dashboard
    │   └── 菜单: "任务调度" → 点击打开 DolphinScheduler
    │
    ├── 任务调度页面 (iframe嵌入)
    │   └── src/views/Scheduler/index.vue
    │       └── <iframe src="http://localhost:12345/dolphinscheduler">
    │
    └── 后端 API 服务
        └── 与 DolphinScheduler API 对接

DolphinScheduler (独立部署)
    │
    ├── Web UI: http://localhost:12345
    ├── API Server: 提供REST接口
    ├── Master: 调度任务
    └── Worker: 执行超算任务
```

**优点**:
- 与超算项目解耦，独立升级维护
- DolphinScheduler原生功能完整保留
- 开发成本低，无需修改DS源码
- 可通过API与超算项目数据互通

**缺点**:
- 需要独立部署一套DS服务
- 用户需要登录两套系统（可通过SSO解决）

### 方案B: 源码集成 + 组件化（深度定制）

```
超算互联网项目
    │
    ├── 集成 DolphinScheduler 前端组件
    │   └── 工作流编辑器、任务监控等
    │
    └── 后端集成 DS Java代码
        └── 调度逻辑、任务执行等
```

**优点**:
- 完全一体化体验
- 可深度定制UI和功能

**缺点**:
- 技术栈冲突（Vue3 vs DS前端）
- 开发成本极高
- 维护困难，升级麻烦

**结论**: 采用方案A（独立部署 + iframe嵌入 + API对接）

---

## 4. 详细开发计划

### 第一阶段: DolphinScheduler 部署 (明天上午)

#### 4.1 环境准备
```bash
# 检查依赖
- JDK 1.8+
- MySQL 5.7+ / PostgreSQL
- ZooKeeper 3.4.6+
```

#### 4.2 下载安装
```bash
# 下载 DolphinScheduler 3.2.0
cd /root/.openclaw/workspace/projects/超算互联网项目/
mkdir scheduler && cd scheduler
wget https://dlcdn.apache.org/dolphinscheduler/3.2.0/apache-dolphinscheduler-3.2.0-bin.tar.gz
tar -zxvf apache-dolphinscheduler-3.2.0-bin.tar.gz
```

#### 4.3 配置数据库
```sql
-- 创建数据库
CREATE DATABASE dolphinscheduler DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

-- 创建用户
CREATE USER 'dscheduler'@'%' IDENTIFIED BY 'dscheduler123';
GRANT ALL PRIVILEGES ON dolphinscheduler.* TO 'dscheduler'@'%';
FLUSH PRIVILEGES;
```

#### 4.4 启动服务
```bash
# 初始化数据库
bash tools/bin/upgrade-schema.sh

# 启动所有服务
bash ./bin/start-all.sh

# 访问 http://localhost:12345/dolphinscheduler
# 默认账号: admin / dolphinscheduler123
```

### 第二阶段: 超算项目前端集成 (明天下午)

#### 5.1 添加菜单项
```typescript
// src/router/index.ts
{
  path: '/scheduler',
  name: 'TaskScheduler',
  component: () => import('@/views/Scheduler/index.vue'),
  meta: {
    title: '任务调度',
    icon: 'Calendar',
    requiresAuth: true
  }
}
```

#### 5.2 创建调度器页面
```vue
<!-- src/views/Scheduler/index.vue -->
<template>
  <div class="scheduler-container">
    <iframe
      ref="schedulerFrame"
      :src="schedulerUrl"
      width="100%"
      height="100%"
      frameborder="0"
      allowfullscreen
    />
  </div>
</template>

<script setup lang="ts">
const schedulerUrl = ref('http://localhost:12345/dolphinscheduler')

// TODO: 单点登录集成，自动传递token
</script>

<style scoped>
.scheduler-container {
  width: 100%;
  height: calc(100vh - 60px); /* 减去header高度 */
}
</style>
```

#### 5.3 侧边栏添加入口
```typescript
// 在侧边栏菜单中添加
{
  title: '任务调度',
  icon: 'Calendar',
  path: '/scheduler'
}
```

### 第三阶段: API对接与数据互通 (后天)

#### 6.1 DolphinScheduler API 封装
```typescript
// src/api/scheduler.ts
import axios from 'axios'

const schedulerClient = axios.create({
  baseURL: 'http://localhost:12345/dolphinscheduler',
  timeout: 10000
})

// 获取工作流列表
export const getWorkflowList = (projectCode: string) => {
  return schedulerClient.get(`/projects/${projectCode}/process-definition`)
}

// 获取任务实例状态
export const getTaskInstances = (processInstanceId: number) => {
  return schedulerClient.get(`/process-instances/${processInstanceId}/tasks`)
}

// 启动工作流
export const startWorkflow = (projectCode: string, processDefinitionCode: string) => {
  return schedulerClient.post(`/projects/${projectCode}/executors/start-process-instance`, {
    processDefinitionCode
  })
}
```

#### 6.2 首页Dashboard数据集成
```typescript
// 在首页显示任务统计
const taskStats = ref({
  running: 0,    // 运行中任务
  completed: 0,  // 已完成
  failed: 0,     // 失败
  queued: 0      // 排队中
})

// 从DolphinScheduler API获取
const fetchTaskStats = async () => {
  const res = await getTaskInstancesOverview()
  taskStats.value = res.data
}
```

---

## 5. 关键配置项

### 5.1 DolphinScheduler 配置
```properties
# conf/application.yaml
server:
  port: 12345

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/dolphinscheduler
    username: dscheduler
    password: dscheduler123

# 配置Worker执行超算任务
worker:
  task:
    types: SHELL,PYTHON,SQL,SPARK,FLINK
```

### 5.2 超算任务工作流示例
```json
{
  "processDefinitionName": "超算作业调度",
  "tasks": [
    {
      "name": "数据预处理",
      "type": "SHELL",
      "command": "python /opt/hpc/data_prep.py"
    },
    {
      "name": "MPI并行计算",
      "type": "SHELL",
      "command": "mpirun -n 64 /opt/hpc/mpi_job"
    },
    {
      "name": "结果上传",
      "type": "SHELL",
      "command": "scp results.txt user@storage:/data/"
    }
  ]
}
```

---

## 6. 开发资源

### 官方资源
- **官网**: https://dolphinscheduler.apache.org/
- **GitHub**: https://github.com/apache/dolphinscheduler
- **文档**: https://dolphinscheduler.apache.org/zh-cn/docs/latest/user_doc/guide/quick-start.html

### 版本选择
- **推荐**: 3.2.0 (最新稳定版)
- **JDK**: 1.8+
- **Node**: 16+ (前端构建)

---

## 7. 明日开发计划

| 时间 | 任务 | 产出 |
|:---|:---|:---|
| 09:00-10:30 | 下载部署DolphinScheduler | 本地DS服务运行 |
| 10:30-12:00 | 配置数据库、初始化、测试 | DS Web可访问 |
| 14:00-15:30 | 超算项目前端集成（菜单+页面）| 首页可点击进入调度器 |
| 15:30-17:00 | iframe嵌入+样式调整 | 无缝集成效果 |
| 17:00-18:00 | API对接测试 | 首页显示任务统计 |

---

## 8. 风险评估

| 风险 | 概率 | 应对 |
|:---|:---:|:---|
| ZooKeeper部署复杂 | 中 | 使用单节点ZooKeeper简化 |
| 跨域问题（iframe）| 中 | 配置CORS或使用nginx反向代理 |
| 登录状态同步 | 中 | 预留SSO接口，先用两套登录 |
| Java环境依赖 | 低 | 服务器已有JDK |

---

## 9. 预期效果

### 用户流程
1. 登录超算互联网平台
2. 点击左侧菜单"任务调度"
3. 右侧打开DolphinScheduler工作流编辑器
4. 拖拽创建超算任务工作流
5. 设置定时调度或手动触发
6. 在首页Dashboard查看任务执行状态

### 截图示意
```
┌──────────────────────────────────────────────────────┐
│  超算互联网平台                    [用户] [退出]      │
├──────────┬───────────────────────────────────────────┤
│          │                                           │
│ 首页     │   ┌───────────────────────────────────┐   │
│ 资源管理  │   │  任务调度 (DolphinScheduler)       │   │
│ 作业管理  │   │                                   │   │
│ 任务调度◄─┼───┤  ┌─────┐   ┌─────┐   ┌─────┐     │   │
│ 监控告警  │   │  │任务A├─┬►│任务B├─┬►│任务C│     │   │
│ 个人中心  │   │  └─────┘   └─────┘   └─────┘     │   │
│          │   │       DAG工作流可视化编辑器         │   │
│          │   └───────────────────────────────────┘   │
└──────────┴───────────────────────────────────────────┘
```

---

**可行性结论**: ✅ **完全可行**  
**技术难度**: 中等（主要是部署配置）  
**开发周期**: 2-3天完成基础集成  
**优先级**: 高（公司项目需求）

**下一步**: 明天上午开始部署DolphinScheduler
