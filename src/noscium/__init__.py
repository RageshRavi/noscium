"""
Noscium — Institutional memory for enterprise AI assistants.

Unlike retrieval systems (RAG) or single-user memory libraries, Noscium is
designed for organizations: multiple users, teams, roles, and the governance
that comes with it.

This is an early pre-alpha scaffold. See the project README and roadmap for
the phased build plan (Phase 1: core memory + extraction + scoped retrieval;
Phase 2: consolidation + conflict resolution; Phase 3: governance + compliance).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


__version__ = "0.0.1"


class MemoryType(str, Enum):
    """What kind of knowledge a memory represents."""
    EPISODIC = "episodic"    # what happened
    SEMANTIC = "semantic"    # what is true
    PROCEDURAL = "procedural"  # how to do something


class VisibilityScope(str, Enum):
    """Who in the organization can see a memory."""
    PERSONAL = "personal"
    TEAM = "team"
    ORG = "org"


@dataclass
class Memory:
    """
    Core memory record.

    This is a Phase 1 scaffold: the shape of the data model, not yet a
    working extraction/retrieval/consolidation pipeline. See the roadmap.
    """
    id: str
    fact: str
    type: MemoryType

    user_id: Optional[str] = None
    agent_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

    team_id: Optional[str] = None
    department_id: Optional[str] = None
    visibility_scope: VisibilityScope = VisibilityScope.PERSONAL

    importance_score: float = 0.0
    invalidated: bool = False


__all__ = ["Memory", "MemoryType", "VisibilityScope", "__version__"]
