import json
import subprocess
import sys
from pathlib import Path


def run(command: str) -> int:
    return subprocess.call(
        command,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


have_git = run("command -v git") == 0

if not have_git:
    print('"git" not found in your PATH. Please install git or add it to your PATH.')
    sys.exit(1)

root_path = Path(__file__).resolve().parent.parent
services_path = root_path / "services"
repositories_path = services_path / "repositories.json"

with open(repositories_path, "r", encoding="utf-8") as f:
    repositories = json.load(f).items()


for name, data in repositories:
    service_path = services_path / name
    repository = data["repository"]
    branch = data.get("branch", "master")

    if service_path.exists() and service_path.is_dir():
        print(f"Service {name} already cloned, skipping...")
        continue

    print(
        f"Cloning service {name} from {repository} to {service_path}, using branch {branch}..."
    )
    run(f"git clone --branch {branch} {repository} {service_path}")
