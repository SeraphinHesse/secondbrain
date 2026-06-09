$output = Join-Path $PSScriptRoot "htbh-combined-claude.md"
$htbhRoot = "C:\Users\serap\OneDrive\Documents\GitHub\HowToBeHuman\ClaudePrototype\HowToBeHuman"

$sources = @(
    @{ File = "$htbhRoot\CLAUDE.md";                    Label = "Root CLAUDE.md" },
    @{ File = "$htbhRoot\src\buildings\CLAUDE.md";      Label = "src/buildings/CLAUDE.md" },
    @{ File = "$htbhRoot\src\core\CLAUDE.md";           Label = "src/core/CLAUDE.md" },
    @{ File = "$htbhRoot\src\enemies\CLAUDE.md";        Label = "src/enemies/CLAUDE.md" },
    @{ File = "$htbhRoot\src\map\CLAUDE.md";            Label = "src/map/CLAUDE.md" },
    @{ File = "$htbhRoot\src\ui\CLAUDE.md";             Label = "src/ui/CLAUDE.md" }
)

$header = @"
# CONTEXT FOR CLAUDE CODE — HOW TO BE HUMAN PROJECT MANAGEMENT

> **You are operating inside the Secondbrain repo, which serves as the project management,
> planning, and idea-collection layer for the game "How to Be Human" (HTBH).**
>
> Your role here is NOT to write game code — that lives in the HowToBeHuman repo.
> Your role here is to help with:
> - **Project planning & task tracking** (milestones, WBS, sprints, scope)
> - **Game design documentation** (mechanics, systems, balancing, design decisions)
> - **Idea capture & processing** (inbox routing, structured notes, ideation)
> - **Producer-level oversight** (what needs doing, what's blocked, what's next)
>
> The CLAUDE.md files below are sourced directly from the HowToBeHuman game repo.
> They describe the architecture, conventions, and current state of the codebase
> so you have full context when discussing or planning work on it.
>
> **Never edit game source files from here. Always work via the HowToBeHuman repo for code.**

---

"@

$content = $header

foreach ($src in $sources) {
    $content += "## $($src.Label)`n`n"
    if (Test-Path $src.File) {
        $content += (Get-Content $src.File -Raw -Encoding UTF8)
        $content += "`n`n---`n`n"
        Write-Host "  [OK]      $($src.Label)"
    } else {
        $content += "> [FILE NOT FOUND: $($src.File)]`n`n---`n`n"
        Write-Host "  [MISSING] $($src.Label)"
    }
}

$content | Out-File -FilePath $output -Encoding UTF8
Write-Host "`nDone. Written to: $output"
