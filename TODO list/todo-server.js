#!/usr/bin/env node
// Secondbrain Todo Dashboard Server — no npm needed, Node stdlib only
// Run: node "todo-server.js" from the "TODO list" folder
// Then open: http://localhost:8765

const http = require('http');
const fs   = require('fs');
const path = require('path');

const PORT     = 8765;
const BASE_DIR = __dirname;
const TODO     = path.join(BASE_DIR, '..', 'ToDo.md');   // one level up
const HTML     = path.join(BASE_DIR, 'todo-dashboard.html');

const CAT_MAP = {
  'HTBH / Producing':       ['##### How to be Human', '###### Producing'],
  'HTBH / Design':          ['##### How to be Human', '###### Design'],
  'HTBH / Claude Build':    ['##### How to be Human', '###### Claude Build'],
  'HTBH / Balancing':       ['##### How to be Human', '###### Balancing'],
  'Addictive Media Agency': ['##### Addictive Media Agency', null],
  'Admin':                  ['##### Admin', null],
  'University':             ['##### University', null],
  'Bureaucracy & Chores':   ['##### Bureaucracy \\& Chores', null],
  // Legacy reminder subcategories (backward compat for existing ToDo.md entries)
  'Reminders / General':               ['##### Reminders', '###### General'],
  'Reminders / HTBH':                  ['##### Reminders', '###### HTBH'],
  'Reminders / Agency':                ['##### Reminders', '###### Agency'],
  'Reminders / Calendar':              ['##### Reminders', '###### Calendar'],
  // Task-category-aligned reminder subcategories (new format)
  'Reminders / HTBH / Producing':      ['##### Reminders', '###### HTBH / Producing'],
  'Reminders / HTBH / Design':         ['##### Reminders', '###### HTBH / Design'],
  'Reminders / HTBH / Claude Build':   ['##### Reminders', '###### HTBH / Claude Build'],
  'Reminders / HTBH / Balancing':      ['##### Reminders', '###### HTBH / Balancing'],
  'Reminders / Addictive Media Agency':['##### Reminders', '###### Addictive Media Agency'],
  'Reminders / Admin':                 ['##### Reminders', '###### Admin'],
  'Reminders / University':            ['##### Reminders', '###### University'],
  'Reminders / Bureaucracy & Chores':  ['##### Reminders', '###### Bureaucracy & Chores'],
};

// Returns tasks with lineNo, descLine, desc fields.
// Description convention: an indented line (2+ spaces) immediately after a * task line.
function parseTodo() {
  const lines = fs.readFileSync(TODO, 'utf8').split('\n');
  const tasks = [];
  let id = 1, project = null, sub = null, inReminders = false;

  for (let lineNo = 0; lineNo < lines.length; lineNo++) {
    const s = lines[lineNo].trim();
    if (s.startsWith('###### '))      { sub = s.slice(7).trim(); }
    else if (s.startsWith('##### ')) {
      const l = s.slice(6).trim();
      if (l) { project = l; inReminders = l === 'Reminders'; }
      sub = null;
    }
    else if (s.startsWith('* ')) {
      let text = s.slice(2).trim();
      if (!text) continue;
      const done = text.startsWith('x ');
      if (done) text = text.slice(2).trim();
      // Flags: '!' = high priority, '^' = major (canonical write order: x !^)
      let high = false, major = false;
      while (text[0] === '!' || text[0] === '^') {
        if (text[0] === '!') high = true; else major = true;
        text = text.slice(1).trim();
      }
      const proj = (project || 'General').replace('How to be Human', 'HTBH').replace(/\\&/g, '&');
      const cat  = sub ? `${proj} / ${sub}` : proj;

      // Check next line for a description (indented with 2+ spaces, not another task or header)
      const nextLine = lines[lineNo + 1];
      const descMatch = nextLine !== undefined ? nextLine.match(/^  +(.+)/) : null;
      const desc     = descMatch ? descMatch[1].trim() : '';
      const descLine = descMatch ? lineNo + 1 : -1;

      tasks.push({ id: id++, cat, text, high, major, done, reminder: inReminders, lineNo, desc, descLine });
    }
  }
  return tasks;
}

function updateTask(id, updates) {
  const tasks = parseTodo();
  const task  = tasks.find(t => t.id === id);
  if (!task) return false;

  const newText = (updates.text !== undefined && updates.text !== null)
    ? String(updates.text).trim() || task.text
    : task.text;
  const newHigh  = updates.high !== undefined ? !!updates.high : task.high;
  const newMajor = updates.major !== undefined ? !!updates.major : task.major;
  const newDone  = updates.done !== undefined ? !!updates.done : task.done;
  const newCat  = (updates.cat !== undefined && updates.cat !== null)
    ? updates.cat : task.cat;
  const newDesc = updates.desc !== undefined ? (updates.desc || '').trim() : task.desc;

  if (newCat !== task.cat) {
    // Category change: remove old task+desc, insert in new section
    const lines = fs.readFileSync(TODO, 'utf8').split('\n');
    if (task.descLine >= 0) lines.splice(task.descLine, 1); // desc first (higher index)
    lines.splice(task.lineNo, 1);
    fs.writeFileSync(TODO, lines.join('\n'), 'utf8');
    addTask(newText, newCat, newHigh, newDesc, newDone, newMajor);
  } else {
    const lines = fs.readFileSync(TODO, 'utf8').split('\n');

    // Handle description changes (desc is always at lineNo+1, so these ops don't shift lineNo)
    if (task.descLine >= 0) {
      if (newDesc) {
        lines[task.descLine] = '  ' + newDesc;
      } else {
        lines.splice(task.descLine, 1);
      }
    } else if (newDesc) {
      lines.splice(task.lineNo + 1, 0, '  ' + newDesc);
    }

    lines[task.lineNo] = '* ' + (newDone ? 'x ' : '') + (newHigh ? '!' : '') + (newMajor ? '^' : '') + newText;
    fs.writeFileSync(TODO, lines.join('\n'), 'utf8');
  }
  return true;
}

function addTask(text, cat, high, desc, done = false, major = false) {
  const lines  = fs.readFileSync(TODO, 'utf8').split('\n');
  const entry  = CAT_MAP[cat] || [`##### ${cat}`, null];
  const [parentH, subH] = entry;
  const newLine = '* ' + (done ? 'x ' : '') + (high ? '!' : '') + (major ? '^' : '') + text;

  let targetIdx = -1;
  if (subH) {
    let inParent = false;
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trim() === parentH.trim()) inParent = true;
      else if (inParent && lines[i].trim() === subH.trim()) { targetIdx = i; break; }
    }
  } else {
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trim() === parentH.trim()) { targetIdx = i; break; }
    }
  }

  if (targetIdx === -1) {
    lines.push('', parentH, '', ...(subH ? [subH, ''] : []), newLine);
    if (desc) lines.push('  ' + desc);
    lines.push('');
  } else {
    let insertPos = targetIdx + 1;
    for (let i = targetIdx + 1; i < lines.length; i++) {
      const s = lines[i].trim();
      if (subH  && /^#{5,6} /.test(s) && i !== targetIdx) break;
      if (!subH && /^#{5} /.test(s)   && i !== targetIdx) break;
      if (s.startsWith('* ')) {
        insertPos = i + 1;
        // Skip past the task's description line if present
        if (i + 1 < lines.length && lines[i + 1].match(/^  +\S/)) {
          insertPos = i + 2;
        }
      }
    }
    lines.splice(insertPos, 0, newLine);
    if (desc) lines.splice(insertPos + 1, 0, '  ' + desc);
  }

  fs.writeFileSync(TODO, lines.join('\n'), 'utf8');
}

function deleteTask(id) {
  const tasks = parseTodo();
  const task  = tasks.find(t => t.id === id);
  if (!task) return false;
  const lines = fs.readFileSync(TODO, 'utf8').split('\n');
  if (task.descLine >= 0) lines.splice(task.descLine, 1); // desc first (higher index)
  lines.splice(task.lineNo, 1);
  fs.writeFileSync(TODO, lines.join('\n'), 'utf8');
  return true;
}

const BACKLOG = path.join(BASE_DIR, 'backlog.md');

function clearCompleted() {
  const tasks = parseTodo();
  const done  = tasks.filter(t => t.done);
  if (!done.length) return 0;

  // Build a dated backlog entry grouped by category
  const now = new Date();
  const dateStr = now.toISOString().slice(0, 16).replace('T', ' ');
  const groups = {};
  const order  = [];
  for (const t of done) {
    if (!groups[t.cat]) { groups[t.cat] = []; order.push(t.cat); }
    groups[t.cat].push(t);
  }
  let entry = `\n## Cleared ${dateStr}\n\n`;
  for (const cat of order) {
    entry += `### ${cat}\n\n`;
    for (const t of groups[cat]) {
      entry += `* ${t.high ? '!' : ''}${t.major ? '^' : ''}${t.text}\n`;
      if (t.desc) entry += `  ${t.desc}\n`;
    }
    entry += '\n';
  }

  if (!fs.existsSync(BACKLOG)) fs.writeFileSync(BACKLOG, '# Backlog\n', 'utf8');
  fs.appendFileSync(BACKLOG, entry, 'utf8');

  // Remove done tasks from ToDo.md (collect line indices, remove in one pass)
  const lines = fs.readFileSync(TODO, 'utf8').split('\n');
  const remove = new Set();
  for (const t of done) {
    remove.add(t.lineNo);
    if (t.descLine >= 0) remove.add(t.descLine);
  }
  fs.writeFileSync(TODO, lines.filter((_, i) => !remove.has(i)).join('\n'), 'utf8');
  return done.length;
}

function readBacklog() {
  if (!fs.existsSync(BACKLOG)) return '';
  return fs.readFileSync(BACKLOG, 'utf8');
}

function cors(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

const server = http.createServer((req, res) => {
  cors(res);

  if (req.method === 'OPTIONS') { res.writeHead(204); res.end(); return; }

  if (req.url === '/api/tasks' && req.method === 'GET') {
    try {
      const tasks = parseTodo().map(({ lineNo, descLine, ...t }) => t);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(tasks));
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
    return;
  }

  if (req.url === '/api/tasks' && req.method === 'PATCH') {
    let body = '';
    req.on('data', d => body += d);
    req.on('end', () => {
      try {
        const { id, high, major, text, cat, desc, done } = JSON.parse(body);
        if (typeof id !== 'number') { res.writeHead(400); res.end('id required'); return; }
        updateTask(id, { high, major, text, cat, desc, done });
        const tasks = parseTodo().map(({ lineNo, descLine, ...t }) => t);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(tasks));
      } catch (e) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: e.message }));
      }
    });
    return;
  }

  if (req.url === '/api/tasks' && req.method === 'POST') {
    let body = '';
    req.on('data', d => body += d);
    req.on('end', () => {
      try {
        const { text, cat, high, major, desc } = JSON.parse(body);
        if (!text || !text.trim()) { res.writeHead(400); res.end('text required'); return; }
        addTask(text.trim(), cat, !!high, (desc || '').trim(), false, !!major);
        const tasks = parseTodo().map(({ lineNo, descLine, ...t }) => t);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(tasks));
      } catch (e) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: e.message }));
      }
    });
    return;
  }

  if (req.url === '/api/tasks' && req.method === 'DELETE') {
    let body = '';
    req.on('data', d => body += d);
    req.on('end', () => {
      try {
        const { id } = JSON.parse(body);
        if (typeof id !== 'number') { res.writeHead(400); res.end('id required'); return; }
        deleteTask(id);
        const tasks = parseTodo().map(({ lineNo, descLine, ...t }) => t);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(tasks));
      } catch (e) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: e.message }));
      }
    });
    return;
  }

  if (req.url === '/api/clear-completed' && req.method === 'POST') {
    try {
      const count = clearCompleted();
      const tasks = parseTodo().map(({ lineNo, descLine, ...t }) => t);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ count, tasks }));
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
    return;
  }

  if (req.url === '/api/backlog' && req.method === 'GET') {
    try {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ content: readBacklog() }));
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
    return;
  }

  if ((req.url === '/' || req.url === '/todo-dashboard.html') && req.method === 'GET') {
    try {
      const html = fs.readFileSync(HTML);
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(html);
    } catch (e) {
      res.writeHead(404); res.end('dashboard not found');
    }
    return;
  }

  res.writeHead(404); res.end();
});

server.listen(PORT, 'localhost', () => {
  const url = `http://localhost:${PORT}`;
  console.log(`  Spinner Questlist Dashboard → ${url}`);
  console.log(`  ToDo.md: ${TODO}`);
  console.log(`  Ctrl+C to stop\n`);

  const { exec } = require('child_process');
  const cmd = process.platform === 'win32' ? `start ${url}`
            : process.platform === 'darwin' ? `open ${url}`
            : `xdg-open ${url}`;
  exec(cmd);
});
