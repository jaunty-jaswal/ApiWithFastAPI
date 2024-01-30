import os
import shutil
import yaml
from userauth import generatekey
call = generatekey.run()
call.generate_uid()
mongo_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"userauth","mn.env"))
jwy_path = os.path.join(os.path.dirname(__file__),"userauth",".env")
collectiondata= ["userdata","usercreds"]
yamlformat = {
    "ENV":{
        'MONGOENV':mongo_path,
        'JWTENV':jwy_path
    },
    'ALGO': "HS256",
    'COLLECTIONS':{
        "DATACOLLECTION": str(collectiondata[0]),
        "USERCREDENTIALSCOLLECTION": str(collectiondata[1]),
        
    }
}
filepath = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__),"config"))):
    shutil.rmtree(os.path.abspath(os.path.join(os.path.dirname(__file__),"config")))

os.mkdir(os.path.join(filepath,"config"))
folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"config"))
file = os.path.join(os.path.dirname(__file__),"config","config.yaml")

with open(file,"w+") as f:
    yaml.dump(yamlformat,f,allow_unicode=False,default_flow_style=False)

 


