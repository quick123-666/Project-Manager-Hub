<!-- PROJECT MANAGER HUB -->

<div align="center">
  <img src="images/logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Project Manager Hub</h3>
  <p align="center">
    项目与技能档案管理系统 | Project & Skill Registry Management
    <br />
    <a href="https://github.com/quick123-666/Project-Manager-Hub"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/quick123-666/Project-Manager-Hub/releases/latest">
      <img src="https://img.shields.io/github/v/release/quick123-666/Project-Manager-Hub?style=flat-square" alt="Version">
    </a>
    <a href="https://github.com/quick123-666/Project-Manager-Hub/issues">
      <img src="https://img.shields.io/github/issues/quick123-666/Project-Manager-Hub?style=flat-square" alt="Issues">
    </a>
    <a href="https://github.com/quick123-666/Project-Manager-Hub/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/quick123-666/Project-Manager-Hub?style=flat-square" alt="License">
    </a>
    <a href="https://github.com/quick123-666/Project-Manager-Hub/stargazers">
      <img src="https://img.shields.io/github/stars/quick123-666/Project-Manager-Hub?style=flat-square" alt="Stars">
    </a>
    <a href="https://github.com/quick123-666/Project-Manager-Hub/network/members">
      <img src="https://img.shields.io/github/forks/quick123-666/Project-Manager-Hub?style=flat-square" alt="Forks">
    </a>
  </p>
</div>

> English | [中文](#chinese)

<a name="english"></a>

## About The Project

Project Manager Hub is a comprehensive system for managing multiple AI projects and their associated Skills. It provides centralized project registration, skill tracking, and knowledge base integration with llmwikify.

### Features

- **Project Registry** - Register and track multiple projects
- **Skill Management** - Maintain skills catalog for each project
- **Knowledge Base Integration** - Connect with llmwikify for semantic search
- **Web Dashboard** - Modern dark-themed control panel
- **Auto-start** - Windows startup configuration

### Built With

- [Python 3.8+](https://www.python.org/)
- [llmwikify](https://github.com/ekegodi/llmwikify)
- HTML/CSS/JavaScript

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- llmwikify (optional, for knowledge base search)

```bash
# Check Python version
python --version
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/quick123-666/Project-Manager-Hub.git
cd Project-Manager-Hub
```

2. (Optional) Install llmwikify for knowledge base
```bash
pip install llmwikify
```

### Quick Start

1. Start the server
```bash
python server.py
```

2. Open browser
```
http://localhost:8765
```

### Usage

```bash
# Add a new project
python registry.py add-project "My AI Project" "./myproject" "Description"

# Add a skill to project
python registry.py add-skill PRP-20260429 "My Skill" "high"

# List all projects
python registry.py list-projects

# Search knowledge base
python wiki.py search "machine learning"
```

---

## Project Structure

```
Project-Manager-Hub/
├── README.md           # This file
├── LICENSE            # MIT License
├── .gitignore         # Git ignore rules
├── dashboard.html     # Web control panel
├── server.py         # HTTP server
├── registry.py       # CLI for project/skill management
├── wiki.py           # llmwikify integration
├── projects/         # Project archives (generated)
├── skills/           # Skill archives (generated)
└── wiki-sync/        # Knowledge base sync files
```

---

## Dashboard Screenshots

The dashboard provides a modern dark-themed interface with:

- **仪表盘 (Dashboard)** - Overview statistics
- **项目 (Projects)** - All registered projects
- **技能 (Skills)** - All registered skills
- **设置 (Settings)** - System configuration

---

## Configuration

### Changing Port

Edit `server.py`:
```python
PORT = 8765  # Change this value
```

### Adding to Windows Startup

```bash
# Method 1: Copy startup.bat to startup folder
# Win+R -> shell:startup

# Method 2: Use Task Scheduler
schtasks /create /tn "ProjectManagerHub" /tr "python server.py" /sc onlogon
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Acknowledgments

- [llmwikify](https://github.com/ekegodi/llmwikify) - Knowledge base
- [OpenCode](https://opencode.ai/) - AI coding assistant
- All contributors

---

<a name="chinese"></a>

## 中文说明

### 关于项目

Project Manager Hub 是一个用于管理多个 AI 项目及其关联 Skills 的综合系统。它提供集中的项目注册、技能跟踪以及与 llmwikify 知识库的集成。

### 功能特性

- **项目注册** - 注册和跟踪多个项目
- **技能管理** - 为每个项目维护技能目录
- **知识库集成** - 连接 llmwikify 进行语义搜索
- **网页控制面板** - 现代深色主题界面
- **开机自启动** - Windows 开机启动配置

### 快速开始

```bash
# 克隆项目
git clone https://github.com/quick123-666/Project-Manager-Hub.git
cd Project-Manager-Hub

# 启动服务
python server.py

# 打开浏览器
http://localhost:8765
```

### 命令行使用

```bash
# 添加项目
python registry.py add-project "我的项目" "./myproject" "项目描述"

# 添加技能
python registry.py add-skill PRP-20260429 "我的技能" "高"

# 列出项目
python registry.py list-projects

# 知识库搜索
python wiki.py search "机器学习"
```

---

<div align="center">
  Made with ❤️ by Project Manager Hub
</div>

[(Back to top)](#english)