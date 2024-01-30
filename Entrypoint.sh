#!/bin/bash
<<comment
first run the generatekey file to generate a random uuid in .env file
after that provide the paths of env files in config.yaml
lastly provide your connection string in mn.env
comment

python3 /yourpath/generatekey.py
uvicorn main:app --reload
