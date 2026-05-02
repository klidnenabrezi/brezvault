from dataclasses import dataclass, field
from datetime import datetime, timezone

from models.vault_entry import VaultEntry

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Vault:
    vault_name: str
    entries: list[VaultEntry] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict:
        return {
            "vault_name": self.vault_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "entries": [entry.to_dict() for entry in self.entries]
        }
    
    @classmethod
    def from_dict(cls,data: dict) -> "Vault":
        return cls(
            vault_name=data["vault_name"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            entries=[
                VaultEntry.from_dict(entry_data) for entry_data in data.get("entries",[])
            ],
        )