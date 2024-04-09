mod core "lib/core/Justfile"
mod local "lib/local/Justfile"
mod labels "lib/labels/Justfile"
mod boxes "lib/boxes/Justfile"
mod errors "lib/errors/Justfile"
mod export "lib/export/Justfile"
mod sdk "lib/sdk/Justfile"
mod api "lib/api/Justfile"
mod annotations "lib/annotations/Justfile"

VENV := ".venv"
PYTHON := ".venv/bin/python"

init:
  rm -drf {{VENV}} || :
  python3.11 -m venv {{VENV}}
  {{PYTHON}} -m pip install --upgrade pip
  {{PYTHON}} -m pip install -r requirements.txt