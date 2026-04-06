# Git工作流安全规范 v1.0

**项目**: P001 超算互联网项目  
**制定时间**: 2026-04-02  
**制定原因**: E0017 灾难事件（代码丢失 + 系统卡死）  
**适用范围**: 所有项目代码操作

---

## 🚨 安全红线（绝对禁止）

| 命令 | 危险等级 | 后果 |
|:---|:---:|:---|
| `git reset --hard` | 🔴 极高 | 永久删除未提交工作 |
| `git clean -fd` | 🔴 极高 | 删除所有未跟踪文件 |
| `rm -rf node_modules` | 🔴 极高 | 可能误删其他目录 |
| `git push --force` | 🟠 高 | 覆盖远程历史 |
| `git add .` | 🟡 中 | 可能包含敏感/大文件 |

**替代方案**:
```bash
# ❌ git reset --hard
# ✅ 使用 git stash（可恢复）
git stash push -m "临时保存"

# ❌ git clean -fd
# ✅ 手动确认删除
trash-put node_modules/  # 可回收

# ❌ git add .
# ✅ 明确指定文件
git add src/ docs/ README.md

# ❌ git push --force
# ✅ 使用 --force-with-lease
git push --force-with-lease origin main
```

---

## 📋 项目初始化清单（必须）

**Step 1: 创建 .gitignore**
```bash
# 必须在第一次 commit 前创建
cat > .gitignore << 'EOF'
# Dependencies
node_modules/
.pnp
.pnp.js

# Build outputs
dist/
build/
*.tgz

# Environment
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log
npm-debug.log*

# Testing
coverage/
.nyc_output/

# Temporary
tmp/
temp/
*.tmp
EOF
```

**Step 2: 验证 .gitignore 生效**
```bash
# 检查 node_modules 是否被忽略
git check-ignore -v node_modules/package.json
# 预期输出: .gitignore:2:node_modules/ node_modules/package.json
```

**Step 3: 首次提交前检查**
```bash
# 查看将被提交的文件（限制50行）
git status --short | head -50

# 确认没有 node_modules 出现
```

---

## 🔄 日常开发工作流

### 工作前
```bash
# 1. 获取最新代码
git pull origin main

# 2. 创建功能分支
git checkout -b feature/功能名称
```

### 工作中（小步快跑）
```bash
# 每次小改动后立即提交
# 1. 查看变更
git diff --stat

# 2. 添加指定文件（不要 add .）
git add src/components/NewFeature.vue

# 3. 检查暂存区
git diff --cached --stat

# 4. 提交（描述清晰）
git commit -m "feat: 添加用户登录表单组件"

# 5. 立即推送（备份）
git push origin feature/功能名称
```

### 工作后（当日结束）
```bash
# 1. 确认所有变更已提交
git status

# 2. 推送当前分支
git push origin feature/功能名称

# 3. 创建本地备份（双保险）
tar -czf ~/backups/项目名_$(date +%Y%m%d_%H%M).tar.gz \
  --exclude=node_modules --exclude=.git .
```

---

## 🛡️ 会话上下文保护

### 避免上下文溢出
```bash
# ❌ 危险: git status 可能输出数万行
git status

# ✅ 安全: 限制输出行数
git status --short | head -50

# ✅ 安全: 使用统计模式
git status --short | wc -l
```

### 大文件处理
```bash
# 检查大文件（>10MB）
find . -type f -size +10M -not -path "./node_modules/*" -not -path "./.git/*"

# 如果必须包含大文件，使用 Git LFS
git lfs track "*.psd"
git lfs track "*.zip"
```

---

## 📦 备份策略（强制执行）

### 三层备份体系
| 层级 | 位置 | 频率 | 保留期 |
|:---|:---|:---:|:---:|
| **本地工作区** | 项目目录 | 实时 | 当前版本 |
| **GitHub远程** | origin | 每次commit | 永久 |
| **本地压缩包** | ~/backups/ | 每日结束 | 30天 |

### 自动备份脚本
```bash
#!/bin/bash
# save-project.sh - 放到项目根目录

PROJECT_NAME=$(basename $(pwd))
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M)
BACKUP_FILE="$BACKUP_DIR/${PROJECT_NAME}_${DATE}.tar.gz"

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 创建压缩包（排除依赖和git目录）
tar -czf "$BACKUP_FILE" \
  --exclude=node_modules \
  --exclude=.git \
  --exclude=dist \
  --exclude=build \
  .

echo "备份完成: $BACKUP_FILE"
ls -lh "$BACKUP_FILE"
```

---

## 🆘 紧急恢复流程

### 场景1: 误删文件（未提交）
```bash
# 从 Git 恢复（如果已跟踪）
git checkout -- 文件路径

# 从备份恢复（如果有）
tar -xzf ~/backups/项目名_YYYYMMDD_HHMM.tar.gz -C /tmp/恢复/
```

### 场景2: 会话卡死（上下文溢出）
```bash
# 方法1: 清空上下文（推荐）
# 在对话中发送: /new

# 方法2: 删除会话文件（慎用）
rm ~/.openclaw/sessions/会话ID.jsonl
```

### 场景3: 代码从未推送且本地丢失
```bash
# 检查 GitHub 是否有历史提交
git log --oneline origin/main

# 如果有，强制拉取覆盖本地
git fetch origin
git reset --hard origin/main  # ⚠️ 这会丢失本地未推送工作

# 如果没有 → 从备份恢复
# 如果没有备份 → 代码永久丢失（教训：E0017）
```

---

## ✅ 操作确认清单

**执行任何 Git 命令前，确认**:
- [ ] .gitignore 已配置并生效
- [ ] 知道当前在哪个分支
- [ ] 知道命令的后果
- [ ] 重要代码已备份

**执行破坏性命令前（如 reset），必须**:
1. 向用户明确说明后果
2. 获得用户明确授权
3. 创建备份
4. 在测试环境验证

---

## 📚 相关文档

- **经验银行**: E0017 Git操作导致上下文溢出 + 代码双丢失
- **项目文档**: /projects/超算互联网项目/docs/
- **备份目录**: ~/backups/

---

**记住**:
> "未配置 .gitignore 的项目不进行任何 Git 操作"
> "未推送 GitHub 的代码等于不存在"
> "宁可多备份，不可丢代码"

*制定者: 飞天皮卡球*  
*制定时间: 2026-04-02*  
*版本: v1.0*
