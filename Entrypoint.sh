#!/bin/bash
<<comment
bash Entrypoint.sh

comment
#if u get error, do this
#sudo apt install python3.10-venv

python3 -m venv .venv
source .venv/bin/activate.csh
pip install -r requirements.txt
python3 starter.py
python3 main.py
