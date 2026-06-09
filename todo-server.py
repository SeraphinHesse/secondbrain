#!/usr/bin/env python3
"""
Secondbrain Todo Dashboard Server
Run: python3 todo-server.py
Then open: http://localhost:8765
"""
import json, os, re, webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8765
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_PATH = os.path.join(BASE_DIR, 'ToDo.md')
HTML_PATH = os.path.join(BASE_DIR, 'todo-dashboard.html')

# Maps dashboard category names → exact header strings in ToDo.md
CAT_MAP = {
    'HTBH / Producing':        ('##### How to be Human', '###### Producing'),
    'HTBH / Design':           ('##### How to be Human', '###### Design'),
    'HTBH / Claude Build':     ('##### How to be Human', '###### Claude Build'),
    'HTBH / Balancing':        ('##### How to be Human', '###### Balancing'),
    'Addictive Media Agency':  ('##### Addictive Media Agency', None),
    'Admin':                   ('##### Admin', None),
    'University':              ('##### University', None),
    'Bureaucracy & Chores':    ('##### Bureaucracy \\& Chores', None),
}


def _header_matches(line, header):
    return line.strip().rstrip() == header.rstrip()


def parse_todo():
    tasks = []
    task_id = 1
    with open(TODO_PATH, encoding='utf-8') as f:
        lines = f.readlines()

    current_project = None
    current_sub = None

    for line in lines:
        s = line.strip()
        if s.startswith('###### '):
            current_sub = s[7:].strip()
        elif s.startswith('##### '):
            label = s[6:].strip()
            if label:
                current_project = label
            current_sub = None
        elif s.startswith('* '):
            text = s[2:].strip()
            if not text:
                continue
            high = text.startswith('!')
            if high:
                text = text[1:].strip()

            # Build dashboard category name
            proj = current_project or 'General'
            proj_short = proj.replace('How to be Human', 'HTBH')
            # Unescape markdown backslash-ampersand
            proj_short = proj_short.replace('\\&', '&')
            cat = f"{proj_short} / {current_sub}" if current_sub else proj_short

            tasks.append({
                'id': task_id,
                'cat': cat,
                'text': text,
                'high': high,
            })
            task_id += 1

    return tasks


def add_task(text, cat, high):
    parent_h, sub_h = CAT_MAP.get(cat, (f'##### {cat}', None))
    prefix = '* !' if high else '* '
    new_line = prefix + text + '\n'

    with open(TODO_PATH, encoding='utf-8') as f:
        lines = f.readlines()

    # Find the target section header index
    target_idx = None
    if sub_h:
        in_parent = False
        for i, line in enumerate(lines):
            if _header_matches(line, parent_h):
                in_parent = True
            elif in_parent and _header_matches(line, sub_h):
                target_idx = i
                break
    else:
        for i, line in enumerate(lines):
            if _header_matches(line, parent_h):
                target_idx = i
                break

    if target_idx is None:
        # Section missing — append at end
        if not lines[-1].endswith('\n'):
            lines.append('\n')
        lines.append(f'\n{parent_h}\n\n')
        if sub_h:
            lines.append(f'\n{sub_h}\n\n')
        lines.append(new_line)
        lines.append('\n')
    else:
        # Scan forward to find last task line in this section
        insert_pos = target_idx + 1
        for i in range(target_idx + 1, len(lines)):
            s = lines[i].strip()
            # Stop at next section header of same or higher level
            if sub_h and re.match(r'^#{5,6} ', s) and i != target_idx:
                break
            if not sub_h and re.match(r'^#{5} ', s) and i != target_idx:
                break
            if s.startswith('* '):
                insert_pos = i + 1
        lines.insert(insert_pos, new_line)

    with open(TODO_PATH, 'w', encoding='utf-8') as f:
        f.writelines(lines)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence request logs

    def send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/tasks':
            try:
                self.send_json(parse_todo())
            except Exception as e:
                self.send_json({'error': str(e)}, 500)
        elif self.path in ('/', '/index.html', '/todo-dashboard.html'):
            try:
                with open(HTML_PATH, 'rb') as f:
                    body = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(body))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/tasks':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            text = body.get('text', '').strip()
            cat  = body.get('cat', 'Admin')
            high = bool(body.get('high', False))
            if not text:
                self.send_json({'error': 'text required'}, 400)
                return
            try:
                add_task(text, cat, high)
                self.send_json(parse_todo())
            except Exception as e:
                self.send_json({'error': str(e)}, 500)
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':
    server = HTTPServer(('localhost', PORT), Handler)
    url = f'http://localhost:{PORT}'
    print(f'  Secondbrain Dashboard → {url}')
    print(f'  Serving from: {BASE_DIR}')
    print(f'  Ctrl+C to stop\n')
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
