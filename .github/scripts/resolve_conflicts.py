import re
import subprocess

CONFLICT = re.compile(
    r"<<<<<<< [^\n]*\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n",
    re.S,
)


def resolve_config(ours: str, theirs: str) -> str:
    theirs_version = re.search(r"^version:.*$", theirs, re.M)
    lines = []
    for line in ours.splitlines():
        if line.startswith("version:") and theirs_version:
            lines.append(theirs_version.group(0))
        else:
            lines.append(line)
    return "\n".join(lines) + "\n"


def resolve_other(ours: str, theirs: str) -> str:
    return theirs


unmerged = subprocess.run(
    ["git", "diff", "--name-only", "--diff-filter=U"],
    capture_output=True,
    text=True,
    check=True,
).stdout.split()

if not unmerged:
    raise SystemExit("no unmerged files found")

for path in unmerged:
    with open(path, encoding="utf-8") as f:
        text = f.read()

    if path.endswith("config.yaml"):
        replacer = resolve_config
    else:
        replacer = resolve_other

    text = CONFLICT.sub(lambda m: replacer(m.group(1), m.group(2)), text)

    if "<<<<<<<" in text or ">>>>>>>" in text:
        raise SystemExit(f"unresolved conflict markers remain in {path}")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"resolved: {path}")
