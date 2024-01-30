import os
import shutil
import yaml
from userauth import generatekey
call = generatekey.run()
call.generate_uid()
mongo_path = os.path.join(os.path.dirname(__file__),"userauth","mn.env")
jwy_path = os.path.join(os.path.dirname(__file__),"userauth",".env")
yamlformat = {
    "ENV":{
        "MONGOENV":mongo_path,
        "JWTENV":jwy_path
    },
    "ALGO":'HS256',
    "COLLECTIONS":{
        "DATACOLLECTION":"userdata",
        "USERCREDENTIALSCOLLECTION":"usercreds"

    }
}
filepath = os.path.abspath(os.path.dirname(__file__))
folder = os.mkdir(os.path.join(filepath,"config"))
if folder:
    shutil.rmtree(folder)
    os.mkdir(os.path.join(filepath,"config"))
else :
    os.mkdir(os.path.join(filepath,"config"))

