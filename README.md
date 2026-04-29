# Project Manager Hub

> 项目与技能档案管理系统

## 简介

一个用于管理多个 AI 项目及其 Skills 的档案管理系统。支持项目注册、技能跟踪、llmwikify 知识库集成。

## 功能

- 项目档案管理 (注册/列表/搜索)
- 技能档案管理  
- llmwikify 知识库集成
- 控制面板 UI
- 开机自启动

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/quick123-666/Project-Manager-Hub.git
cd Project-Manager-Hub

# 2. 启动服务
python server.py

# 3. 访问控制面板
# http://localhost:8765
```

## 命令

```bash
# 添加项目
python registry.py add-project "项目名" "路径" "描述"

# 添加技能
python registry.py add-skill 项目ID "技能名" "优先级"

# 列出项目
python registry.py list-projects

# 知识库搜索
python wiki.py search <关键词>

# 同步项目到知识库
python wiki.py sync "项目名" "路径"
```

## 文件结构

```
Project-Manager-Hub/
├── README.md           # 说明文档
├── server.py          # HTTP 服务器
├── registry.py       # 档案管理脚本
├── wiki.py           # llmwikify 集成
├── dashboard.html    # 控制面板
├── startup.bat      # 自启动脚本
├── projects/        # 项目档案目录
└── skills/         # 技能档案目录
```

## 控制面板

访问 http://localhost:8765 查看控制面板，包含：
- 仪表盘 - 统计概览
- 项目 - 所有项目列表
- 技能 - 所有技能列表
- 设置 - 系统设置

## 项目列表

当前已注册项目：
- Mercury-Crab
- TuriX CUA
- Zero Team Engine
- Workflow Engine

##许可证

MIT