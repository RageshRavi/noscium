# Noscium

Institutional memory for enterprise AI assistants.

Unlike retrieval systems (RAG) or single-user memory libraries, Noscium is
designed for organizations: multiple users, teams, roles, and the governance
that comes with it.

> **Status: pre-alpha.** This repo currently holds the initial scaffold and
> roadmap. Follow along via the [Institutional Intelligence newsletter](#)
> for build updates.

## Why Noscium

Most AI agent memory systems (Mem0, Zep, and others) optimize for *individual
recall* — one user's memories, retrieved well over time. Noscium's focus is
different: *organizational* memory — many users, teams, and roles, and the
access control, consolidation, and conflict resolution that come with that.

## Planned Features

- **Multi-user access control** — memories scoped by role and team
- **Organizational consolidation** — individual facts become org-level knowledge
- **Conflict resolution** — when memories contradict, track and resolve
- **Compliance & retention** — configurable policies, audit trails, provenance
- **Importance judging** — LLM + user feedback decides what's worth remembering
- **Memory types** — episodic (what happened), semantic (what is true), procedural (how to do X)

## Roadmap

| Phase | Focus | Status |
|---|---|---|
| Phase 1 | Core memory model, extraction, scoped retrieval | In progress |
| Phase 2 | Organizational consolidation, conflict resolution, memory graph | Planned |
| Phase 3 | Governance, compliance, retention policies, full audit trail | Planned |

## Installation

```bash
pip install noscium
```

(Pre-alpha — API will change without notice until a 0.1.0 release.)

## Quickstart

```python
from noscium import Memory, MemoryType, VisibilityScope

m = Memory(
    id="mem_001",
    fact="Customer X prefers async standups",
    type=MemoryType.SEMANTIC,
    team_id="support-team",
    visibility_scope=VisibilityScope.TEAM,
)
```

## License

MIT
