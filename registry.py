#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Registry - 项目与技能档案管理
"""

import os
import sys
from datetime import datetime
from pathlib import Path

class Registry:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.projects_path = self.base_path / "projects"
        self.skills_path = self.base_path / "skills"
        
        self.projects_path.mkdir(parents=True, exist_ok=True)
        self.skills_path.mkdir(parents=True, exist_ok=True)
    
    def register_project(self, name, path, description="", status="dev"):
        project_id = f"{name[:3].upper()}-{datetime.now().strftime('%Y%m%d')}"
        
        project_file = self.projects_path / f"{name.replace(' ', '-')}.md"
        
        content = f"""# 项目档案: {name}

## 基本信息

| 属性 | 值 |
|------|------|
| ID | {project_id} |
| 名称 | {name} |
| 路径 | {path} |
| 状态 | {status} |
| 创建时间 | {datetime.now().isoformat()} |

## 描述

{description}

## 技能需求

详见 `../skills/`
"""
        
        with open(project_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        return project_id, project_file
    
    def register_skill(self, project_id, skill_name, description="", priority="medium"):
        skill_id = f"{project_id}-SK-{len(list(self.skills_path.glob('*.md')))+1}"
        
        skill_file = self.skills_path / f"{skill_name.replace(' ', '-')}.md"
        
        content = f"""# Skill 档案: {skill_name}

## 基本信息

| 属性 | 值 |
|------|------|
| ID | {skill_id} |
| 项目 | {project_id} |
| 名称 | {skill_name} |
| 优先级 | {priority} |
| 创建时间 | {datetime.now().isoformat()} |

## 描述

{description}
"""
        
        with open(skill_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        return skill_id, skill_file
    
    def list_projects(self):
        projects = []
        for file in self.projects_path.glob("*.md"):
            name = file.stem.replace('-', ' ')
            projects.append({"file": str(file), "name": name})
        return projects
    
    def list_skills(self, project_id=None):
        skills = []
        for file in self.skills_path.glob("*.md"):
            name = file.stem.replace('-', ' ')
            skills.append({"file": str(file), "name": name})
        return skills


def main():
    reg = Registry()
    
    if len(sys.argv) < 2:
        print("Project Registry - 项目/技能档案管理")
        print("")
        print("Usage:")
        print("  python registry.py add-project <名称> <路径> <描述>")
        print("  python registry.py add-skill <项目ID> <技能名> <优先级>")
        print("  python registry.py list-projects")
        print("  python registry.py list-skills")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "add-project" and len(sys.argv) >= 4:
        name = sys.argv[2]
        path = sys.argv[3]
        desc = sys.argv[4] if len(sys.argv) > 4 else ""
        
        pid, pfile = reg.register_project(name, path, desc)
        print(f"[OK] Project: {pid} -> {pfile}")
    
    elif cmd == "add-skill" and len(sys.argv) >= 4:
        pid = sys.argv[2]
        sname = sys.argv[3]
        pri = sys.argv[4] if len(sys.argv) > 4 else "medium"
        
        sid, sfile = reg.register_skill(pid, sname, pri)
        print(f"[OK] Skill: {sid} -> {sfile}")
    
    elif cmd == "list-projects":
        projects = reg.list_projects()
        print("=== Projects ===")
        for p in projects:
            print(f"{p['name']}")
    
    elif cmd == "list-skills":
        skills = reg.list_skills()
        print("=== Skills ===")
        for s in skills:
            print(f"{s['name']}")


if __name__ == "__main__":
    main()