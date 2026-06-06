# Plan: Implement disclaw to control my agent via Discord

A brief plan for wiring up [**disclaw**](https://github.com/six-ddc/disclaw) so I can drive my Claude agent from Discord.

## What disclaw is

A single lightweight Node/Bun process that bridges Discord ↔ Claude Code. You `@mention`
a bot in a channel; it spawns a Claude session inside a thread, with button-based tool
approvals, multimodal input (images, PDFs, code files), and an MCP server exposing Discord
+ cron tools. State (thread↔session maps, channel configs, cron jobs) lives in local
SQLite — no Redis, no HTTP server, no exposed ports, outbound Discord gateway only.

## Steps

### 1. Create a dedicated Discord bot
> ⚠️ Don't reuse the existing Claude Code plugin token — a single bot token can only hold
> one gateway connection, so they'd kick each other.

- Discord Developer Portal → New Application → Bot → copy token
- Enable **Message Content Intent** (Bot settings)
- OAuth2 → URL Generator → scope `bot` + permissions: Send Messages, Create Public
  Threads, Send Messages in Threads, Read Message History, Add Reactions → invite to server

### 2. Install
Prerequisites: Bun runtime + an authenticated Claude Code CLI.

```bash
git clone https://github.com/six-ddc/disclaw.git
cd disclaw
bun install
cp .env.example .env
```

### 3. Configure `.env`

| Variable | Value |
|----------|-------|
| `DISCORD_BOT_TOKEN` | `<new bot token>` |
| `CLAUDE_WORKING_DIR` | `<project dir>` (default `~/.disclaw`) |
| `DISCLAW_ALLOWED_DIRS` | comma-separated allowlist — scope what it can touch |
| `DISCLAW_PERMISSION_MODE` | `default` — keep button approvals on at first |
| `TZ` | `Europe/Berlin` — correct cron/time |

### 4. Run

```bash
bun run start   # production
bun run dev     # development (hot reload)
```

### 5. Use it
`@bot <task>` in a channel → session opens in a thread. Useful slash commands:

- `/disclaw cd` — change working directory
- `/disclaw config` — model / permissions / display mode
- `/disclaw clear` — fresh session
- `/disclaw resume` — restore a previous session
- `/disclaw fork` — branch conversation to a new thread
- `/disclaw cron` — list / manage scheduled tasks

### 6. First test
Have it send a morning briefing to this Discord channel (`1512574864920281240`)
set up via `/disclaw cron`.

## Safety notes

- Keep `DISCLAW_PERMISSION_MODE=default` until trusted; tighten `DISCLAW_ALLOWED_DIRS`.
- Use a separate bot identity so it doesn't clobber the Claude Code Discord plugin.
- To keep it running while the PC sleeps, consider a small always-on box / VPS.

## Reference

- Repo: https://github.com/six-ddc/disclaw
- Existing plugin token (do not reuse for disclaw): `C:\Users\serap\.claude\channels\discord\.env`
- Discord channel ID: `1512574864920281240`
- Discord user ID (for DMs): `525357928979365889`
