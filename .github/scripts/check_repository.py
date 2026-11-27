"""Check the initial repository without third-party dependencies."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
REQUIRED = {
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitignore",
    ".github/workflows/ci.yml",
    ".github/dependabot.yml",
    "docs/repository-setup.md",
}
SECRET_PATTERNS = (
    re.compile(rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"),
    re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{50,}\b"),
)


def main():
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    )
    paths = [Path(name.decode("utf-8")) for name in result.stdout.split(b"\0") if name]
    names = {path.as_posix() for path in paths}
    errors = []

    for name in sorted(REQUIRED - names):
        errors.append(f"Required file is not tracked: {name}")

    for relative in paths:
        name = relative.name
        if (
            name == "SERVER_INFO.md"
            or relative.suffix.lower() in {".pem", ".key", ".ppk"}
            or name.startswith(("id_rsa", "id_ed25519"))
            or (name.startswith(".env") and name != ".env.example")
            or name in {"credentials.json", "secrets.json"}
            or relative.as_posix().startswith(".local/")
        ):
            errors.append(f"Local or credential file must not be tracked: {relative}")
            continue

        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            errors.append(f"Tracked path must be a regular file: {relative}")
            continue
        content = path.read_bytes()
        if any(pattern.search(content) for pattern in SECRET_PATTERNS):
            errors.append(f"Possible credential in {relative}; remove it before publishing")
        if b"\0" not in content and content and not content.endswith(b"\n"):
            errors.append(f"Text file needs a final newline: {relative}")

    for command in (["git", "diff", "--check"], ["git", "diff", "--cached", "--check"]):
        check = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if check.returncode:
            errors.append(check.stdout.strip() or check.stderr.strip())

    if errors:
        print("Repository checks failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"Repository checks passed ({len(paths)} tracked files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
