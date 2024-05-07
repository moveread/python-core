mod boxes "1.boxes/Justfile"
mod labels "1.labels/Justfile"
mod annotations "2.annotations/Justfile"
mod core "3.core/Justfile"
mod errors "4.errors/Justfile"
mod export "5.export/Justfile"
mod sdk "5.sdk/Justfile"
mod datasets

VENV := ".venv"
BIN := ".venv/bin"
PYTHON := ".venv/bin/python"

help:
  @just --list

reset: init install

init:
  rm -drf {{VENV}} || :
  python3.11 -m venv {{VENV}}
  {{PYTHON}} -m pip install --upgrade pip
  {{PYTHON}} -m pip install verify-import

install:
  {{PYTHON}} -m pip install -r requirements.txt

verify *ARGS:
  #!/bin/bash
  for path in 1.boxes 1.labels 2.annotations 3.core 4.errors 5.export 5.sdk datasets; do
    mod=$(echo $path | cut -d '.' -f 2)
    echo "Verifying module: moveread.$mod"
    {{BIN}}/verify-import "moveread.$mod" {{ARGS}}
  done

republish:
  #!/bin/bash
  for path in 1.boxes 1.labels 2.annotations 3.core 4.errors 5.export 5.sdk datasets; do
    mod=$(echo $path | cut -d '.' -f 2)
    echo "Publishing module: moveread.$mod"
    just $mod republish
  done

verify-install *ARGS:
  #!/bin/bash
  for path in 1.boxes 1.labels 2.annotations 3.core 4.errors 5.export 5.sdk datasets; do
    mod=$(echo $path | cut -d '.' -f 2)
    echo "Verifying module: moveread.$mod"
    {{PYTHON}} -m pip install -e $path
    {{BIN}}/verify-import "moveread.$mod" {{ARGS}}
  done