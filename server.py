#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Manager Hub - HTTP 服务器
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8765
DIRECTORY = Path(__file__).parent.absolute()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def log_message(self, format, *args):
        pass

def start_server():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Project Manager Hub 运行中: http://localhost:{PORT}")
        print(f"按 Ctrl+C 停止")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()