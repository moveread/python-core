mod boxes "1.boxes/Justfile"
mod labels "1.labels/Justfile"
mod annotations "2.annotations/Justfile"
mod core "3.core/Justfile"
mod errors "4.errors/Justfile"
mod export "5.export/Justfile"
mod sdk "5.sdk/Justfile"
mod datasets

VENV := ".venv"
PYTHON := ".venv/bin/python"

init:
  rm -drf {{VENV}} || :
  python3.11 -m venv {{VENV}}
  {{PYTHON}} -m pip install --upgrade pip
  {{PYTHON}} -m pip install -r requirements.txt