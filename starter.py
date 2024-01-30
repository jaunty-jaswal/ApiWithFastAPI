import os
import yaml
from configfile import config
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
