import json

from models.vault import Vault
from models.vault_entry import VaultEntry


vault = Vault(vault_name="BrezVault")

github_entry = VaultEntry(
    title="GitHub",
    username="brez",
    password="myVeryStrongPassword123!",
    url="https://github.com",
    notes="personal GitHub account",
)

vault.entries.append(github_entry)

vault_dict = vault.to_dict()

print("=== Vault as dict ===")
print(vault_dict)

print("\n=== Vault as JSON ===")
print(json.dumps(vault_dict, indent=4))

rebuilt_vault = Vault.from_dict(vault_dict)

print("\n=== Rebuilt vault ===")
print(rebuilt_vault)