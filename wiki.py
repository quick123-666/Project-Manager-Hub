#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
llmwikify 集成模块
"""

import sys
import subprocess

def search_llmwikify(query):
    """搜索 llmwikify 知识库"""
    print(f"搜索: {query}")
    
    result = subprocess.run(
        [sys.executable, "-m", "llmwikify", "search", query, "--limit", "5"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("请先安装 llmwikify: pip install llmwikify")

def sync_project_to_wiki(project_name, project_path):
    """记录项目到本地同步文件"""
    print(f"记录项目: {project_name}")
    
    wiki_file = Path(__file__).parent / "wiki-sync" / f"{project_name.replace(' ', '-')}.md"
    wiki_file.parent.mkdir(exist_ok=True)
    
    content = f"""# {project_name}

**路径**: {project_path}
**注册时间**: {datetime.now().isoformat()}

## 档案
详见 Project Manager Hub 系统
"""
    
    wiki_file.write_text(content, encoding="utf-8")
    print(f"已记录: {wiki_file}")

from pathlib import Path
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("llmwikify 集成")
        print("Usage:")
        print("  python wiki.py search <关键词>")
        print("  python wiki.py sync <项目名> <路径>")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "search" and len(sys.argv) >= 3:
        search_llmwikify(" ".join(sys.argv[2:]))
    
    elif cmd == "sync" and len(sys.argv) >= 4:
        sync_project_to_wiki(sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()