import uuid
import os
class run:
    def __init__(self):
        self.id = None
    def generate_uid(self):
        self.id = uuid.uuid4()
        path = os.path.join(os.path.dirname(__file__),'.env')
        with open (path,"w+") as f:
            f.write("KEY = ")
            f.write(f"'{self.id}'")

