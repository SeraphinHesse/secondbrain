# Seraphin's Secondbrain — Claude Code Workspace

## Who I Am
Indie video game producer/project manager and boutique marketing agency startup founder.
Timezone: Europe/Berlin. Based in Germany. GitHub: SeraphinHesse.

## Active Projects
- **HTBH** — current game prototype in active development (`projects/htbh/`)
- **Marketing Agency** — boutique agency in startup phase (`agency/`)
- **Disclaw** — Discord ↔ Claude Code bridge for async agent control (see `disclaw-setup-plan.md`)

## Connected Tools (always available — use these proactively)
| Tool | MCP prefix | Use for |
|------|-----------|---------|
| Google Calendar | `mcp__0bf2cda2-*` | scheduling, reminders, daily agenda |
| Gmail | `mcp__cbca4b77-*` | email management, drafts, lead outreach |
| Google Drive | `mcp__b78871ac-*` | file storage, finding assets, docs |
| GitHub | `mcp__github__*` | code repos, issues, PRs |
| Discord | plugin | async control, idea capture, daily briefings |

## Workspace Structure
```
secondbrain/
├── inbox/              # Drop zone: raw ideas, voice memo transcripts, unprocessed notes
├── projects/
│   ├── htbh/           # HTBH game project files, design docs, task tracking
│   └── _template/      # Copy this when starting a new project
├── agency/
│   ├── clients/        # One folder per client: brief, comms log, deliverables
│   ├── leads/          # Prospecting notes and outreach tracking
│   ├── campaigns/      # Active campaign work
│   └── templates/      # Reusable agency assets
├── personal/
│   ├── daily/          # Daily briefings (YYYY-MM-DD.md format)
│   └── notes/          # Personal reference notes
├── ideas/
│   ├── game-dev/       # Game ideas, mechanics experiments
│   ├── marketing/      # Marketing and growth ideas
│   └── general/        # Everything else
└── templates/          # Master templates for notes, CRM entries, briefs
```

## How I Work — Behavioral Instructions

### Ideation Pipeline
When I give you raw input (bullet points, voice memo transcript, rough notes):
1. Identify the domain (game dev / marketing / personal / general)
2. Identify if it belongs to an existing project or is a standalone idea
3. Structure it using the relevant template from `templates/`
4. Save it to the right location — **never leave ideas in inbox without processing them**
5. Tell me exactly where you put it and why

### Daily Briefing
When asked for a daily briefing or when starting a session in the morning:
1. Use Google Calendar MCP to get today's events
2. Use Gmail MCP to surface any urgent/unread threads
3. Check `inbox/` for unprocessed items
4. Check `projects/htbh/` for any open tasks
5. Format as the template in `templates/daily-briefing.md`

### Email Management
- For drafting outreach to leads: use the tone guide in `agency/templates/outreach-tone.md`
- Always write email drafts first, never send without my explicit approval
- Use Gmail labels to organize: flag anything that needs my decision as "needs-reply"
- For follow-ups: check sent threads and flag ones with no reply after 3 days

### Game Prototype Work (HTBH and others)
- All code goes in `projects/htbh/` or the relevant project folder
- Use GitHub MCP for issues and tracking
- When I say "prototype X mechanic" — build the simplest possible playable version first
- Keep a `devlog.md` in each project folder updated after major sessions

### Marketing Agency
- Lead research: use deep-research skill + web search to build lead profiles
- Store each lead as a file in `agency/leads/[company-name].md` using `templates/lead-profile.md`
- Client work lives in `agency/clients/[client-name]/`
- When I describe what a client needs, draft a scope of work using `templates/scope-of-work.md`

### Inbox Processing
When I say "process inbox" or "clear inbox":
1. Read every file in `inbox/`
2. Classify and route each one to the right location
3. Structure unstructured notes
4. Delete from inbox after moving
5. Give me a summary of what was filed where

## Tone & Style
- Be direct and concise — I'm a busy founder, not a student
- Don't explain obvious things; assume I'm technical
- When you're unsure where something belongs, ask one clear question, not several
- Flag blockers immediately rather than working around them silently
- I prefer bullet points over prose for status updates

## Recurring Tasks (via /loop skill)
- **Daily briefing**: mornings at 08:00 Europe/Berlin — pull calendar + email + inbox status
- **Lead follow-up check**: Mondays — scan Gmail for unanswered outreach threads

## Key Context
- Discord user ID: `525357928979365889`
- Discord briefing channel: `1512574864920281240`
- Disclaw setup is in progress — once live, I'll control Claude Code sessions via Discord
