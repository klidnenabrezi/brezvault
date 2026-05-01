from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4
from zoneinfo import ZoneInfo

def utc_now_iso() -> str:
    return datetime.now().isoformat()


@dataclass
class VaultEntry:
    title: str
    username: str
    password: str
    url: str = ""