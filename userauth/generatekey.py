import uuid
import os

def generate_uid():
    id = uuid.uuid4()
    return str(id)

id = generate_uid()

path = os.path.join('/home/shantanujaswal/api/userauth','.env')

with open (path,"w+") as f:
    f.write("KEY = ")
    f.write(f"'{id}'")