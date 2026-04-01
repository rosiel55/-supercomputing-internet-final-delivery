# 超算互联网应用解算平台

> 国家科研课题交付项目 — 长沙超算/湖南大学

## 项目概述

超算互联网应用解算平台，作为课题参与方的统一门户，集成各子系统能力，实现跨中心资源调度与函数服务。

### 核心功能
- 📊 全局资源视图（4中心拓扑展示）
- 🔧 函数服务市场（50+函数接口）
- 📦 工作流编排（跨中心任务卸载）
- 📈 资源监控（Grafana/scnet.cn集成）
- 🔬 数学库/求解器数据展示

### 技术指标覆盖
| 指标编号 | 内容 | 平台体现 |
|:---:|:---|:---|
| 1.1-1.5 | 资源建模与全局文件系统 | 资源视图模块 |
| 2.1-2.5 | 资源感知与自适应调优 | 监控与数据展示模块 |
| 3.1-3.5 | 函数接口与工作流 | 函数市场、工作流编排模块 |
| 4.1-4.5 | 云原生与函数计算 | 部署架构与集成网关 |

---

## 技术架构

```
┌─────────────────────────────────────────┐
│           Frontend (Vue3)               │
│  - Element Plus UI组件                  │
│  - ECharts可视化                        │
│  - Axios HTTP客户端                     │
└──────────────┬──────────────────────────┘
               │ REST API
┌──────────────▼──────────────────────────┐
│           Backend (Node.js)             │
│  - Express框架                          │
│  - JWT认证                              │
│  - API网关（代理外部系统）               │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│        External Systems                 │
│  - 济南超算Grafana                      │
│  - 国家超算互联网(scnet.cn)             │
│  - 中科院网络中心函数服务                │
│  - 方心科技求解器平台                    │
│  - 北京九所协同仿真平台                  │
└─────────────────────────────────────────┘
```

---

## 项目结构

```
supercomputing-platform/
├── frontend/                 # 前端项目 (Vue3)
│   ├── src/
│   │   ├── components/       # 公共组件
│   │   ├── views/            # 页面视图
│   │   │   ├── Dashboard/    # 全局资源视图
│   │   │   ├── Functions/    # 函数服务市场
│   │   │   ├── Workflow/     # 工作流编排
│   │   │   ├── Monitor/      # 资源监控
│   │   │   └── Libraries/    # 数学库/求解器
│   │   ├── router/           # 路由配置
│   │   ├── store/            # Pinia状态管理
│   │   ├── api/              # API接口封装
│   │   └── utils/            # 工具函数
│   ├── public/
│   └── package.json
│
├── backend/                  # 后端项目 (Node.js)
│   ├── src/
│   │   ├── routes/           # API路由
│   │   ├── controllers/      # 控制器
│   │   ├── services/         # 业务服务
│   │   ├── middleware/       # 中间件（认证等）
│   │   ├── models/           # 数据模型
│   │   └── config/           # 配置文件
│   ├── package.json
│   └── .env.example
│
├── docs/                     # 项目文档
│   ├── requirements/         # 需求文档
│   ├── design/               # 设计文档
│   └── api/                  # API文档
│
├── docker/                   # Docker配置
│   ├── frontend.Dockerfile
│   └── backend.Dockerfile
│
├── docker-compose.yml        # 本地开发编排
├── README.md
└── CHANGELOG.md              # 变更记录
```

---

## 开发环境

### 前置要求
- Node.js >= 18
- npm >= 9
- Git

### 快速启动

```bash
# 1. 克隆仓库
git clone https://github.com/rosiel55/-supercomputing-internet-final-delivery.git
cd -supercomputing-internet-final-delivery

# 2. 启动后端
cd backend
npm install
npm run dev

# 3. 启动前端（新终端）
cd frontend
npm install
npm run dev

# 4. 访问
open http://localhost:5173
```

### Docker启动

```bash
docker-compose up -d
```

---

## 协作规范

### Git工作流
- `main` 分支：稳定版本
- `develop` 分支：开发版本
- `feature/*` 分支：功能开发
- `fix/*` 分支：Bug修复

### 提交规范
```
feat: 新增功能
fix: 修复问题
docs: 文档更新
style: 代码格式（不影响功能）
refactor: 重构
chore: 构建/工具变动
```

### 需求追踪
所有需求变更记录于 `docs/requirements/` 和 `CHANGELOG.md`

---

## 参与方对接

| 参与方 | 对接内容 | 状态 |
|:---|:---|:---:|
| 济南超算 | Grafana监控面板 | 🟡 待对接 |
| 国家超算互联网 | scnet.cn门户 | 🟡 待对接 |
| 中科院网络中心 | 函数服务接口 | 🟡 待对接 |
| 方心科技 | 求解器适配数据 | 🟡 待对接 |
| 北京九所 | 自动测量/协同仿真 | 🟡 待对接 |

---

## 许可证

科研项目内部使用

---

**项目负责人**: 孙珊 (湖南大学/长沙超算)  
**技术实现**: 飞天皮卡球 (AI开发助手)  
**项目周期**: 2026.04 - 2026.09
