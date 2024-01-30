import os
import yaml

class pathset:
    def __init__(self):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","config","config.yaml"))
    def openyaml(self):
        with open(self.path,"r") as f:
            config = yaml.full_load(f)
        return config
    
