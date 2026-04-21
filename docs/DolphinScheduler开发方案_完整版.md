# DolphinScheduler 集成开发方案 - 完整版

**文档状态**: 开发方案确认  
**目标**: 多Worker分布式集群 + 自研前端 + 超算项目集成

---

## 一、整体架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                        超算互联网项目                                │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  首页 Dashboard                                              │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌───────────┐ │   │
│  │  │ 运行中: 3  │ │ 成功: 12   │ │ 失败: 0    │ │ 待执行: 2 │ │   │
│  │  └────────────┘ └────────────┘ └────────────┘ └───────────┘ │   │
│  │  [最近工作流列表]                              [查看全部 →]  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  任务调度页面（自研前端）                                     │   │
│  │  ┌──────────┬─────────────────────────────┬──────────────┐  │   │
│  │  │          │                             │              │  │   │
│  │  │ 节点库   │      DAG画布区域            │   属性面板    │  │   │
│  │  │ ┌──────┐ │  ┌───┐    ┌─────┐          │  名称: [   ]  │  │   │
│  │  │ │Shell │ │  │开始├───►│任务A├────┐     │  类型: [   ]  │  │   │
│  │  │ │Python│ │  └───┘    └─────┘    │     │  脚本: [   ]  │  │   │
│  │  │ │SQL   │ │                      ▼     │       [   ]  │  │   │
│  │  │ │HPC   │ │                   ┌─────┐  │       [   ]  │  │   │
│  │  │ └──────┘ │                   │任务B│  │              │  │   │
│  │  │          │                   └──┬──┘  │ [保存][运行] │  │   │
│  │  │          │                      │     │              │  │   │
│  │  │          │                      ▼     │              │  │   │
│  │  │          │                   ┌─────┐  │              │  │   │
│  │  │          │                   │ 结束 │  │              │  │   │
│  │  │          │                   └─────┘  │              │  │   │
│  │  └──────────┴─────────────────────────────┴──────────────┘  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  API封装层 (schedulerApi.ts)                                 │   │
│  │  - 工作流定义CRUD                                            │   │
│  │  - 任务实例查询                                              │   │
│  │  - 运行控制（启动/停止/暂停）                                 │   │
│  │  - 日志查看                                                  │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                   │ RESTful API
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    DolphinScheduler 分布式集群                       │
│                                                                     │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐       │
│  │ API Server   │◄────┤   Master     │────►│   Worker A   │       │
│  │ :12345       │     │  (调度中心)   │     │  (超算节点)   │       │
│  └──────────────┘     └──────┬───────┘     └──────────────┘       │
│                              │                                      │
│  ┌──────────────┐           │         ┌──────────────┐             │
│  │   MySQL      │◄──────────┴────────►│   Worker B   │             │
│  │ (元数据存储)  │                     │  (数据节点)   │             │
│  └──────────────┘                     └──────────────┘             │
│                              │                                      │
│                              │         ┌──────────────┐             │
│  ┌──────────────┐           └────────►│   Worker C   │             │
│  │  ZooKeeper   │                      │  (备份节点)   │             │
│  │ (服务协调)   │                      └──────────────┘             │
│  └──────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 二、需要做的事情清单

### 2.1 DS后端部署

#### 基础设施准备
- [ ] 确认服务器清单（IP、操作系统、资源配置）
- [ ] 确认MySQL数据库（版本、账号、网络连通性）
- [ ] 确认ZooKeeper部署方式（独立部署/复用现有）
- [ ] 确认服务器间网络互通（端口开放：12345, 2181, 3306）

#### Master节点部署
- [ ] 下载DS 3.2.0二进制包
- [ ] 解压并配置环境变量
- [ ] 修改`conf/application.yaml`配置
  - [ ] MySQL连接信息
  - [ ] ZooKeeper连接信息
  - [ ] Master节点标识
- [ ] 初始化数据库（执行`tools/bin/upgrade-schema.sh`）
- [ ] 启动API Server
- [ ] 启动Master Server

#### Worker节点部署（每台Worker服务器）
- [ ] 复制DS二进制包到Worker服务器
- [ ] 配置`conf/application.yaml`
  - [ ] Master地址列表
  - [ ] Worker分组标识（如：hpc-group, data-group）
  - [ ] 日志路径
- [ ] 启动Worker Server
- [ ] 验证Worker注册到ZooKeeper

#### 验证测试
- [ ] API接口测试（curl/ping）
- [ ] Master状态检查
- [ ] Worker心跳检查
- [ ] 简单任务测试（Shell脚本执行）

### 2.2 前端开发

#### 技术准备
- [ ] 安装@vue-flow/core及相关依赖
- [ ] 配置TypeScript类型定义
- [ ] 配置样式变量（统一配色）

#### DAG编辑器核心组件
- [ ] `FlowCanvas.vue` - DAG画布容器
- [ ] `NodeLibrary.vue` - 左侧节点库面板
- [ ] `PropertyPanel.vue` - 右侧属性配置面板
- [ ] `Toolbar.vue` - 顶部工具栏（保存/运行/撤销）
- [ ] `MiniMap.vue` - 画布缩略图

#### 节点类型组件
- [ ] `StartNode.vue` - 开始节点
- [ ] `EndNode.vue` - 结束节点
- [ ] `ShellNode.vue` - Shell脚本节点
- [ ] `PythonNode.vue` - Python节点
- [ ] `SQLNode.vue` - SQL节点
- [ ] `HPCNode.vue` - 超算作业节点（自定义）

#### 页面集成
- [ ] 路由配置（`/scheduler`）
- [ ] 侧边栏菜单添加
- [ ] 页面布局（三栏式：节点库/画布/属性）
- [ ] 配色统一（白底红色企业风）

#### Dashboard集成
- [ ] 任务统计卡片组件
- [ ] 最近工作流列表组件
- [ ] 快速操作按钮

### 2.3 API对接

#### API客户端封装
- [ ] 创建`schedulerApi.ts`
- [ ] 配置axios实例（baseURL, timeout, interceptors）
- [ ] 实现工作流定义API
- [ ] 实现任务实例API
- [ ] 实现日志查看API

#### 状态管理
- [ ] Pinia store设计（workflowStore）
- [ ] 工作流列表状态
- [ ] 当前编辑工作流状态
- [ ] 任务执行状态

#### 错误处理
- [ ] API错误统一处理
- [ ] 网络异常提示
- [ ] 业务错误提示

### 2.4 数据转换层

#### 前端数据 → DS数据
- [ ] DAG图转DS工作流JSON
- [ ] 节点位置信息处理
- [ ] 依赖关系计算

#### DS数据 → 前端数据
- [ ] DS工作流JSON转DAG图
- [ ] 节点渲染位置计算
- [ ] 状态映射

---

## 三、集成方案细节

### 3.1 前后端交互流程

```
用户操作 → 前端组件 → Pinia Store → schedulerApi → DS REST API
                ↓           ↓              ↓
            状态更新    数据转换      错误处理
```

### 3.2 工作流生命周期

```
1. 创建
   用户点击"新建" → 初始化空白DAG → 添加开始/结束节点

2. 编辑
   拖拽节点 → 连接节点 → 配置节点属性 → 自动保存草稿

3. 保存
   点击"保存" → 前端DAG转DS JSON → 调用API创建/更新 → 返回code

4. 发布
   点击"发布" → 调用release API → 工作流上线可执行

5. 运行
   点击"运行" → 调用start API → 返回instanceId → 轮询状态

6. 监控
   轮询任务状态 → 更新节点颜色（运行中/成功/失败）

7. 查看日志
   点击节点 → 调用log API → 显示执行日志
```

### 3.3 配色方案（与超算首页统一）

```css
/* 全局背景 */
--bg-page: #f5f5f5;
--bg-card: #ffffff;

/* 主色调 */
--primary: #c62828;        /* 深红 */
--primary-light: #f44336;  /* 亮红 */
--gradient: linear-gradient(135deg, #c62828 0%, #f44336 100%);

/* 功能色 */
--success: #52c41a;
--warning: #faad14;
--error: #f5222d;
--info: #1890ff;

/* 文字 */
--text-primary: #333333;
--text-secondary: #666666;
--text-muted: #999999;

/* 边框 */
--border: #e0e0e0;

/* 节点状态色 */
--node-pending: #d9d9d9;
--node-running: #1890ff;
--node-success: #52c41a;
--node-failed: #f5222d;
```

### 3.4 节点类型定义

```typescript
// 基础节点
interface BaseNode {
  id: string;
  type: 'start' | 'end' | 'shell' | 'python' | 'sql' | 'hpc';
  position: { x: number; y: number };
  data: {
    name: string;
    description?: string;
    config: NodeConfig;
    status?: TaskStatus;
  };
}

// Shell节点配置
type ShellConfig = {
  script: string;           // 脚本内容
  resources?: string[];     // 资源文件
  timeout?: number;         // 超时时间（分钟）
  retryTimes?: number;      // 重试次数
};

// Python节点配置
type PythonConfig = {
  script: string;
  pythonVersion?: '2' | '3';
  requirements?: string[];  // pip依赖
};

// SQL节点配置
type SQLConfig = {
  sql: string;
  datasourceId: string;     // 数据源ID
  queryType: 'SELECT' | 'INSERT' | 'UPDATE' | 'DELETE';
};

// HPC超算节点配置（自定义）
type HPCConfig = {
  jobScript: string;        // PBS/Slurm作业脚本
  queue?: string;           // 队列名
  nodes?: number;           // 节点数
  cores?: number;           // 核数
  wallTime?: string;        // 运行时限（如：01:00:00）
};
```

---

## 四、部署内容清单

### 4.1 Master节点（1台）

```yaml
# 服务器配置
CPU: 4核+
内存: 8GB+
磁盘: 50GB+
操作系统: CentOS 7+/Ubuntu 18.04+

# 部署组件
- API Server (端口: 12345)
- Master Server (端口: 5678)
- 日志路径: /opt/dolphinscheduler/logs

# 配置文件
- conf/application.yaml
- conf/common.properties
- conf/env/dolphinscheduler_env.sh
```

### 4.2 Worker节点（N台）

```yaml
# 每台Worker服务器
CPU: 根据任务需求
内存: 根据任务需求
磁盘: 根据日志和输出数据量

# 部署组件
- Worker Server (端口: 1234)
- 日志路径: /opt/dolphinscheduler/logs

# Worker分组配置
worker.groups: hpc-group, data-group, backup-group
```

### 4.3 数据库

```sql
-- MySQL数据库
CREATE DATABASE dolphinscheduler DEFAULT CHARACTER SET utf8mb4;

-- 用户
CREATE USER 'ds_user'@'%' IDENTIFIED BY '密码';
GRANT ALL PRIVILEGES ON dolphinscheduler.* TO 'ds_user'@'%';
```

### 4.4 ZooKeeper

```yaml
# 独立部署或复用现有
端口: 2181
数据目录: /data/zookeeper

# DS配置
registry:
  type: zookeeper
  zookeeper:
    quorum: zk1:2181,zk2:2181,zk3:2181
```

---

## 五、关键API清单

### 5.1 工作流定义

```typescript
// 创建工作流
POST /projects/{projectCode}/process-definition
Body: {
  name: string;
  description?: string;
  globalParams?: Parameter[];
  tasks: TaskDefinition[];
  taskRelation: TaskRelation[];
}

// 更新工作流
PUT /projects/{projectCode}/process-definition/{code}

// 删除工作流
DELETE /projects/{projectCode}/process-definition/{code}

// 发布/下线
POST /projects/{projectCode}/process-definition/{code}/release
Body: { releaseState: 'ONLINE' | 'OFFLINE' }

// 获取工作流详情
GET /projects/{projectCode}/process-definition/{code}

// 获取工作流列表
GET /projects/{projectCode}/process-definition?pageNo=1&pageSize=10
```

### 5.2 任务执行

```typescript
// 启动工作流
POST /projects/{projectCode}/executors/start-process-instance
Body: {
  processDefinitionCode: string;
  scheduleTime?: string;    // 定时时间
  failureStrategy?: 'END' | 'CONTINUE';
  warningType?: 'NONE' | 'SUCCESS' | 'FAILURE' | 'ALL';
  warningGroupId?: number;
}

// 停止工作流
POST /projects/{projectCode}/executors/execute
Body: {
  processInstanceId: number;
  executeType: 'STOP' | 'PAUSE' | 'REPEAT_RUNNING';
}

// 获取任务实例列表
GET /projects/{projectCode}/task-instances?pageNo=1&pageSize=10

// 获取任务日志
GET /task-instances/{taskInstanceId}/log?skipLineNum=0&limit=1000
```

---

## 六、需要确认的技术细节

### 6.1 服务器相关
- [ ] 目标服务器IP列表
- [ ] 每台服务器的资源配置（CPU/内存/磁盘）
- [ ] 每台服务器的任务类型分工（超算/数据处理/备份）
- [ ] 服务器间网络连通性
- [ ] 防火墙端口开放情况

### 6.2 数据库相关
- [ ] MySQL服务器地址和端口
- [ ] 账号密码（或创建新账号）
- [ ] 字符集要求（建议utf8mb4）

### 6.3 ZooKeeper相关
- [ ] 是否已有ZooKeeper集群可用？
- [ ] 如果没有，是否接受DS内置ZooKeeper（Standalone模式）？
- [ ] ZooKeeper地址和端口

### 6.4 任务相关
- [ ] 需要支持的任务类型（Shell/Python/SQL/HPC/其他？）
- [ ] HPC任务使用什么调度系统（PBS/Slurm/LSF？）
- [ ] 工作流数量预估（几十条还是几百条？）
- [ ] 任务并发度要求（同时运行多少个任务？）

### 6.5 安全相关
- [ ] 是否需要任务权限控制？
- [ ] 日志敏感数据处理
- [ ] 服务器SSH密钥管理

---

## 七、文件结构

```
projects/超算互联网项目/
├── docs/
│   └── DolphinScheduler简化集成方案_v2.md  # 本方案文档
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── scheduler.ts              # DS API封装
│   │   ├── components/
│   │   │   └── WorkflowEditor/
│   │   │       ├── FlowCanvas.vue        # DAG画布
│   │   │       ├── NodeLibrary.vue       # 节点库
│   │   │       ├── PropertyPanel.vue     # 属性面板
│   │   │       ├── Toolbar.vue           # 工具栏
│   │   │       └── nodes/
│   │   │           ├── StartNode.vue
│   │   │           ├── ShellNode.vue
│   │   │           ├── PythonNode.vue
│   │   │           ├── SQLNode.vue
│   │   │           └── HPCNode.vue
│   │   ├── stores/
│   │   │   └── workflowStore.ts          # Pinia状态管理
│   │   ├── types/
│   │   │   └── workflow.ts               # 类型定义
│   │   ├── views/
│   │   │   ├── Dashboard/
│   │   │   │   └── TaskStatsCard.vue     # 首页统计卡片
│   │   │   └── Scheduler/
│   │   │       └── index.vue             # 任务调度主页面
│   │   └── utils/
│   │       └── dagConverter.ts           # DAG数据转换
│   └── package.json
└── scheduler/                              # DS部署目录
    ├── apache-dolphinscheduler-3.2.0-bin/
    │   ├── bin/
    │   ├── conf/
    │   └── logs/
    └── install_env.sh
```

---

## 八、成功标准

### 8.1 功能验收
- [ ] 首页显示任务统计（运行中/成功/失败/待执行）
- [ ] 能创建、编辑、保存工作流
- [ ] 能发布、运行工作流
- [ ] 能查看任务执行状态和日志
- [ ] 配色与超算首页统一（白底红色）

### 8.2 性能验收
- [ ] DAG画布流畅（节点拖拽、缩放不卡顿）
- [ ] API响应时间 < 1秒
- [ ] 支持同时显示50+节点不卡顿

### 8.3 部署验收
- [ ] Master + 多Worker正常运行
- [ ] Worker分布在不同服务器
- [ ] 任务能在指定Worker上执行

---

**方案已完整梳理，待确认技术细节后即可开始开发。**
