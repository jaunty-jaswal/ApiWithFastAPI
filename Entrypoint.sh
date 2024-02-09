#!/bin/bash
<<comment
bash Entrypoint.sh

comment
#if u get error, do this
#sudo apt install python3.10-venv
echo "Welcome to this API"
for i in {0..19};
do
    echo -n "#"
    sleep 0.05
done;
echo ""
echo "---system will install libespeak1---"
for i in {0..40};
do 
    echo -n "#"
    sleep 0.05
done;
echo ""
sudo apt install libespeak1
python3 -m venv .venv
source .venv/bin/activate.csh
pip install -r requirements.txt
# cd ..
# cd kafka-server
# gnome-terminal --tab --title="Zookeeper-server" --execute ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
# pid1=$$
# gnome-terminal --tab --title="kafka-server" --execute ./bin/kafka-server-start.sh ./config/server.properties
# pid2=$$
# cd ..
# cd ApiWithFastAPI
python3 starter.py
#./kafka-server/bin/zookeeper-server-start.sh ./config/zookeeper.properties
#./kafka-server/bin/kafka-server-start.sh ./config/server.properties
uvicorn main:app --reload
#python3 main.py
