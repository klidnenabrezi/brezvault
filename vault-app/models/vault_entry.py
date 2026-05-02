from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4
from zoneinfo import ZoneInfo

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class VaultEntry:
    title: str
    username: str
    password: str
    url: str = ""
    notes: str = ""
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "username": self.username,
            "url": self.url,
            "notes": self.notes,
            "created_at": self.created_at,
            "updated_at": self.updated_at, 
        }
    

    @classmethod
    def from_dict(cls, data: dict) -> "VaultEntry":
        return cls(
            id=data["id"],
            title=data["title"],
            username=data["username"],
            password=data["password"],
            url=data.get("url", ""),
            notes=data.get("notes", ""),
            created_at=data["created_at"],
            updated_at=data["updated_at"],
        )
