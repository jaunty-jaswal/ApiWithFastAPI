#!/bin/bash
<<comment
bash Entrypoint.sh
comment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
#add your path here:-
python3 starter.py
python3 main.py
