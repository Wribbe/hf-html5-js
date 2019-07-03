#!/usr/bin/env python3
import platform
import shutil
import sys
import subprocess

from pathlib import Path


DIR_VENV = Path("venv")
SYSTEM = platform.system()
PATH_BIN = Path(DIR_VENV, "Script" if SYSTEM == "Windows" else "bin")
PATH_ACTIVATE = Path(PATH_BIN, "activate_this.py")
PY = ""


def call(command):
  """ Auto-split wrapper around the subprocess call command. """
  if type(command) == str:
    command = command.split()
  return subprocess.call(command)


def activate_virt():
  """ Activate the virtual environment, create first if missing. """
  global PY
  if not PY:
    if SYSTEM == "Windows":
      PY = Path(DIR_VENV, "Script", "python.exe")
    elif SYSTEM == "Linux":
      PY = Path(DIR_VENV, "bin", "python")
    else:
      print(f"System: {SYSTEM} not supported, aborting.", file=sys.stderr)
      sys.exit(-1)

  if not DIR_VENV.is_dir():
    call(f"python -m venv {DIR_VENV}")
    call(f"{PY} -m pip install --upgrade pip")
    call(f"{PY} -m pip install -r requirements.txt")
    shutil.copy(Path("scripts","activate_this.py"), PATH_ACTIVATE)


  with open(PATH_ACTIVATE) as f:
    exec(f.read(), {'__file__': PATH_ACTIVATE})

# Activate virtual environment when importing app.
activate_virt()
