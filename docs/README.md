# 超算互联网项目 - Dashboard前端

**项目编号**: P001  
**创建时间**: 2026-04-01  
**技术栈**: Vue3 + TypeScript + Vite + Element Plus

---

## 🚨 重要安全公告（2026-04-02）

⚠️ **本项目于 2026-04-02 凌晨遭遇代码丢失灾难事件**（E0017）

**事件概要**:
- `git status` 输出 1万+ 文件路径，撑爆 AI 会话上下文
- 导致会话卡死，消息重试失控
- 尝试 `git reset --hard` 回滚时误删源代码
- 代码从未推送到 GitHub，本地备份被清理
- **结果**: 16,927字节源码彻底丢失

**已采取的措施**:
1. ✅ 制定 [Git工作流安全规范](./GIT_WORKFLOW.md)
2. ✅ 建立强制备份机制
3. ✅ 禁用危险 Git 命令
4. ✅ 配置完善的 .gitignore

**必读文档**:
- [Git工作流安全规范](./GIT_WORKFLOW.md) - **所有开发者必须阅读**

---

## 📁 项目结构

```
超算互联网项目/
├── docs/                    # 项目文档
│   ├── README.md           # 本文件
│   └── GIT_WORKFLOW.md     # Git安全规范
├── src/                     # 源代码
│   ├── components/         # 组件
│   ├── views/              # 页面
│   ├── router/             # 路由
│   ├── store/              # 状态管理
│   ├── utils/              # 工具函数
│   ├── App.vue             # 根组件
│   └── main.ts             # 入口文件
├── public/                  # 静态资源
├── index.html              # HTML模板
├── package.json            # 依赖配置
├── tsconfig.json           # TypeScript配置
├── vite.config.ts          # Vite配置
└── .gitignore              # Git忽略规则（已完善）
```

---

## 🛠️ 开发环境

### 前置要求
- Node.js >= 18.0
- Git >= 2.30
- 已阅读 [Git工作流安全规范](./GIT_WORKFLOW.md)

### 安装依赖
```bash
npm install
```

### 启动开发服务器
```bash
npm run dev
```

### 构建生产版本
```bash
npm run build
```

---

## 🔄 开发工作流

**必须遵守 [Git工作流安全规范](./GIT_WORKFLOW.md)**

简述：
1. 小步快跑，频繁 commit
2. 每次 commit 后立即 push
3. 每日结束创建本地备份
4. 绝不使用 `git reset --hard`

---

## 📦 备份策略

| 层级 | 位置 | 频率 |
|:---|:---|:---:|
| GitHub远程 | origin/main | 每次commit |
| 本地压缩包 | ~/backups/ | 每日结束 |
| 会话快照 | 三色存档 | 定时/阈值触发 |

---

## 📝 变更日志

### v0.1.0 (2026-04-01) - 丢失
- ✅ Dashboard框架搭建
- ✅ Element Plus组件集成
- ✅ 基础路由配置
- ❌ **代码已丢失**

### v0.1.1 (2026-04-02) - 计划中
- [ ] 重建 Dashboard 框架
- [ ] 完善 Git 工作流
- [ ] 建立自动化备份

---

## ⚠️ 已知问题

1. **E0017**: Git操作安全风险（已制定规范）
2. **Dashboard依赖**: element-plus 图标加载问题（待修复）
3. **备份机制**: 需要自动化脚本（待实现）

---

## 📚 相关文档

- [Git工作流安全规范](./GIT_WORKFLOW.md)
- [项目规范 - AGENTS.md](../../AGENTS.md)
- [经验银行 - TOOLS.md](../../TOOLS.md) (搜索 E0017)

---

**项目负责人**: 孙珊  
**AI协作者**: 飞天皮卡球  
**最后更新**: 2026-04-02
