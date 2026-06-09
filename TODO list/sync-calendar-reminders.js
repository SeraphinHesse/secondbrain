#!/usr/bin/env node
// Morning Calendar Sync — run at 06:30 via Windows Task Scheduler
// Reads Google Calendar events for the next 24 hours (all calendars),
// replaces the "##### Reminders / ###### Calendar" section in ToDo.md,
// then commits and pushes to main.
//
// Requires: GOOGLE_CALENDAR_TOKEN_PATH env var pointing to a stored OAuth token JSON,
// OR (preferred) run via Claude Code cron which has MCP access — see schedule in CLAUDE.md.
//
// Usage (manual):  node "TODO list/sync-calendar-reminders.js"
// Usage (cron):    scheduled via CronCreate in Claude Code — see CLAUDE.md

const fs   = require('fs');
const path = require('path');
const http  = require('https');
const { execSync } = require('child_process');

const BASE_DIR = __dirname;
const TODO     = path.join(BASE_DIR, '..', 'ToDo.md');
const TOKEN_PATH = process.env.GOOGLE_CALENDAR_TOKEN_PATH
  || path.join(BASE_DIR, '..', '.google-calendar-token.json');

// ── Fetch events from Google Calendar API ─────────────────────────────────
async function fetchEventsWithToken(accessToken) {
  const now = new Date();
  const end = new Date(now.getTime() + 24 * 60 * 60 * 1000);
  const timeMin = now.toISOString();
  const timeMax = end.toISOString();

  // 1. Get list of all calendars
  const cals = await apiGet(accessToken, `https://www.googleapis.com/calendar/v3/users/me/calendarList`);
  const events = [];

  for (const cal of (cals.items || [])) {
    const params = new URLSearchParams({ timeMin, timeMax, singleEvents: 'true', orderBy: 'startTime' });
    const data = await apiGet(accessToken, `https://www.googleapis.com/calendar/v3/calendars/${encodeURIComponent(cal.id)}/events?${params}`);
    for (const ev of (data.items || [])) {
      if (!ev.summary) continue;
      const start = ev.start.dateTime || ev.start.date;
      events.push({ summary: ev.summary, start, calName: cal.summary || cal.id });
    }
  }

  events.sort((a, b) => a.start.localeCompare(b.start));
  return events;
}

function apiGet(token, url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, { headers: { Authorization: `Bearer ${token}` } }, res => {
      let body = '';
      res.on('data', d => body += d);
      res.on('end', () => {
        try { resolve(JSON.parse(body)); } catch (e) { reject(new Error(body)); }
      });
    });
    req.on('error', reject);
  });
}

function formatEventLine(ev) {
  const d = new Date(ev.start);
  const isAllDay = ev.start.length === 10; // date-only
  if (isAllDay) {
    return `* [${ev.start} all-day] ${ev.summary}`;
  }
  const yyyy = d.getFullYear();
  const mm   = String(d.getMonth() + 1).padStart(2, '0');
  const dd   = String(d.getDate()).padStart(2, '0');
  const hh   = String(d.getHours()).padStart(2, '0');
  const mi   = String(d.getMinutes()).padStart(2, '0');
  return `* [${yyyy}-${mm}-${dd} ${hh}:${mi}] ${ev.summary}`;
}

// ── Rewrite ToDo.md calendar section ──────────────────────────────────────
function updateCalendarSection(lines) {
  // Find ###### Calendar under ##### Reminders
  let inReminders = false;
  let calStart = -1, calEnd = -1;

  for (let i = 0; i < lines.length; i++) {
    const s = lines[i].trim();
    if (s === '##### Reminders') { inReminders = true; continue; }
    if (inReminders && s === '###### Calendar') { calStart = i; continue; }
    if (calStart >= 0 && calEnd < 0) {
      if (/^#{5,6} /.test(s) && i > calStart) { calEnd = i; break; }
    }
    if (inReminders && /^##### /.test(s) && s !== '##### Reminders') { break; }
  }

  return { calStart, calEnd };
}

async function main() {
  if (!fs.existsSync(TOKEN_PATH)) {
    console.error(`No token file found at ${TOKEN_PATH}`);
    console.error('Run Google OAuth flow first, or use Claude Code cron with MCP access.');
    process.exit(1);
  }

  const tokenJson = JSON.parse(fs.readFileSync(TOKEN_PATH, 'utf8'));
  const accessToken = tokenJson.access_token;

  console.log('Fetching Google Calendar events (next 24h)…');
  const events = await fetchEventsWithToken(accessToken);
  console.log(`Found ${events.length} events`);

  const lines = fs.readFileSync(TODO, 'utf8').split('\n');
  const { calStart, calEnd } = updateCalendarSection(lines);

  const eventLines = events.length
    ? events.map(formatEventLine)
    : ['* (no events in next 24 hours)'];

  if (calStart >= 0) {
    // Replace existing section content
    const endIdx = calEnd >= 0 ? calEnd : lines.length;
    // Remove old event lines between calStart+1 and endIdx
    const before = lines.slice(0, calStart + 1);
    const after  = lines.slice(endIdx);
    lines.splice(0, lines.length, ...before, '', ...eventLines, '', ...after);
  } else {
    // Append Calendar sub-section under Reminders
    let remIdx = lines.findIndex(l => l.trim() === '##### Reminders');
    if (remIdx < 0) {
      lines.push('', '##### Reminders', '', '###### Calendar', '', ...eventLines, '');
    } else {
      // Find end of Reminders section
      let insertAt = remIdx + 1;
      for (let i = remIdx + 1; i < lines.length; i++) {
        const s = lines[i].trim();
        if (/^##### /.test(s)) { insertAt = i; break; }
        insertAt = i + 1;
      }
      lines.splice(insertAt, 0, '', '###### Calendar', '', ...eventLines, '');
    }
  }

  fs.writeFileSync(TODO, lines.join('\n'), 'utf8');
  console.log('ToDo.md updated with calendar events.');

  // Commit and push
  const repoDir = path.join(BASE_DIR, '..');
  try {
    execSync('git add ../ToDo.md', { cwd: BASE_DIR, stdio: 'inherit' });
    execSync(`git commit -m "chore: morning calendar sync ${new Date().toISOString().slice(0,10)}"`, { cwd: repoDir, stdio: 'inherit' });
    execSync('git push origin main', { cwd: repoDir, stdio: 'inherit' });
    console.log('Pushed to main ✓');
  } catch (e) {
    console.error('Git push failed:', e.message);
  }
}

main().catch(e => { console.error(e); process.exit(1); });
